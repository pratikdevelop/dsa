    import hashlib
    import json
    import time
    import requests
    from flask import Flask, jsonify, request
    from urllib.parse import urlparse
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
    from cryptography.exceptions import InvalidSignature


    class Block:
        def __init__(self, index, previous_hash, timestamp, transactions, nonce):
            self.index = index
            self.previous_hash = previous_hash
            self.timestamp = timestamp
            self.transactions = transactions
            self.nonce = nonce
            self.hash = self.compute_hash()

        def compute_hash(self):
            block_string = json.dumps(self.__dict__, sort_keys=True)
            return hashlib.sha256(block_string.encode()).hexdigest()


    class Blockchain:
        def __init__(self):
            self.chain = []
            self.current_transactions = []
            self.nodes = set()
            self.difficulty = "0000"  # PoW difficulty (4 leading zeros)
            self.create_genesis_block()

        def create_genesis_block(self):
            genesis_block = Block(0, "0", time.time(), [], 0)
            self.chain.append(genesis_block)

        @property
        def last_block(self):
            return self.chain[-1]

        def new_transaction(self, sender, recipient, amount, signature=None):
            tx = {
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
            }
            if signature:
                tx['signature'] = signature
            self.current_transactions.append(tx)
            return self.last_block.index + 1

        def new_block(self, nonce, previous_hash=None):
            previous_hash = previous_hash or self.last_block.hash
            block = Block(
                index=len(self.chain),
                previous_hash=previous_hash,
                timestamp=time.time(),
                transactions=self.current_transactions,
                nonce=nonce
            )
            self.current_transactions = []
            self.chain.append(block)
            return block

        def proof_of_work(self):
            nonce = 0
            while True:
                data = {
                    'index': len(self.chain),
                    'previous_hash': self.last_block.hash,
                    'timestamp': time.time(),
                    'transactions': self.current_transactions,
                    'nonce': nonce
                }
                guess_hash = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
                if guess_hash.startswith(self.difficulty):
                    return nonce
                nonce += 1

        def valid_transaction(self, transaction):
            if transaction.get('sender') == 'network':
                return True  # Coinbase transaction has no signature

            required = ['sender', 'recipient', 'amount', 'signature']
            if not all(k in transaction for k in required):
                return False

            tx_data = {
                'sender': transaction['sender'],
                'recipient': transaction['recipient'],
                'amount': transaction['amount']
            }

            try:
                public_key = Ed25519PublicKey.from_public_bytes(bytes.fromhex(transaction['sender']))
                public_key.verify(
                    bytes.fromhex(transaction['signature']),
                    json.dumps(tx_data, sort_keys=True).encode()
                )
                return True
            except InvalidSignature:
                print("Invalid transaction signature")
                return False
            except Exception as e:
                print(f"Error verifying signature: {e}")
                return False

        def valid_block(self, block, previous_block):
            if block.previous_hash != previous_block.hash:
                return False
            if not block.hash.startswith(self.difficulty):
                return False
            if block.hash != block.compute_hash():
                return False

            for tx in block.transactions:
                if not self.valid_transaction(tx):
                    return False
            return True

        def resolve_conflicts(self):
            neighbors = self.nodes
            new_chain = None
            max_length = len(self.chain)

            for node in neighbors:
                try:
                    response = requests.get(f'http://{node}/chain', timeout=3)
                    if response.status_code == 200:
                        chain = response.json()['chain']
                        length = len(chain)
                        if length > max_length and self.check_chain_validity(chain):
                            max_length = length
                            new_chain = chain
                except:
                    continue

            if new_chain:
                self.chain = [Block(**block) for block in new_chain]
                return True
            return False

        def check_chain_validity(self, chain):
            previous_block = Block(**chain[0])
            for block_data in chain[1:]:
                block = Block(**block_data)
                if not self.valid_block(block, previous_block):
                    return False
                previous_block = block
            return True

        def register_node(self, address):
            parsed_url = urlparse(address)
            self.nodes.add(parsed_url.netloc)


    # Initialize Flask app and blockchain
    app = Flask(__name__)
    blockchain = Blockchain()
    MINER_ADDRESS = "miner_one"


    @app.route('/transactions/new', methods=['POST'])
    def new_transaction():
        values = request.get_json()
        required = ['sender', 'recipient', 'amount', 'signature']
        if not all(k in values for k in required):
            return 'Missing values', 400

        # Verify the transaction before adding
        tx_data = {
            'sender': values['sender'],
            'recipient': values['recipient'],
            'amount': values['amount']
        }

        try:
            public_key = Ed25519PublicKey.from_public_bytes(bytes.fromhex(values['sender']))
            public_key.verify(
                bytes.fromhex(values['signature']),
                json.dumps(tx_data, sort_keys=True).encode()
            )
        except InvalidSignature:
            return jsonify({'error': 'Invalid signature'}), 400
        except Exception as e:
            return jsonify({'error': f'Signature verification failed: {e}'}), 400

        blockchain.new_transaction(values['sender'], values['recipient'], values['amount'], values['signature'])
        return jsonify({'message': 'Transaction added'}), 201


    @app.route('/mine', methods=['GET'])
    def mine():
        if not blockchain.current_transactions:
            return jsonify({'message': 'No transactions to mine'}), 400

        # Add coinbase transaction
        coinbase_tx = {
            'sender': 'network',
            'recipient': MINER_ADDRESS,
            'amount': 1,
            'signature': ''
        }
        blockchain.current_transactions.append(coinbase_tx)

        nonce = blockchain.proof_of_work()
        previous_hash = blockchain.last_block.hash
        block = blockchain.new_block(nonce, previous_hash)

        response = {
            'message': 'New Block Forged',
            'index': block.index,
            'transactions': block.transactions,
            'nonce': block.nonce,
            'previous_hash': block.previous_hash,
            'hash': block.hash
        }

        # Broadcast new block
        for node in blockchain.nodes:
            try:
                requests.post(f'http://{node}/blocks/new', json=response, timeout=2)
            except:
                pass

        return jsonify(response), 200


    @app.route('/chain', methods=['GET'])
    def full_chain():
        chain_data = [block.__dict__ for block in blockchain.chain]
        return jsonify({'chain': chain_data, 'length': len(chain_data)}), 200


    @app.route('/blocks/new', methods=['POST'])
    def new_block():
        data = request.get_json()
        required = ['index', 'previous_hash', 'timestamp', 'transactions', 'nonce', 'hash']
        if not all(k in data for k in required):
            return 'Missing block fields', 400

        try:
            block = Block(**data)
        except Exception as e:
            return f'Invalid block: {e}', 400

        previous_block = blockchain.last_block
        if int(block.index) != int(previous_block.index) + 1:
            return jsonify({'message': 'Incorrect index'}), 400

        if blockchain.valid_block(block, previous_block):
            blockchain.chain.append(block)

            # Broadcast to peers
            for node in blockchain.nodes:
                try:
                    requests.post(f'http://{node}/blocks/new', json=data, timeout=2)
                except:
                    pass

            return jsonify({'message': 'Block added'}), 200
        else:
            return jsonify({'message': 'Invalid block'}), 400


    @app.route('/nodes/register', methods=['POST'])
    def register_nodes():
        values = request.get_json()
        nodes = values.get('nodes')
        if not nodes:
            return 'Error: Please supply a valid list of nodes', 400

        for node in nodes:
            blockchain.register_node(node)

        return jsonify({
            'message': 'Nodes registered',
            'total_nodes': list(blockchain.nodes)
        }), 201


    @app.route('/nodes/resolve', methods=['GET'])
    def consensus():
        replaced = blockchain.resolve_conflicts()
        if replaced:
            return jsonify({
                'message': 'Chain was replaced',
                'new_chain': [b.__dict__ for b in blockchain.chain]
            }), 200
        else:
            return jsonify({
                'message': 'Our chain is authoritative'
            }), 200


    if __name__ == '__main__':
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument('-p', '--port', default=5000, type=int)
        args = parser.parse_args()
        app.run(host='0.0.0.0', port=args.port)


# from langgraph.prebuilt import create_react_agent

# def get_weather(city: str) -> str:  
#     """Get weather for a given city."""
#     return f"It's always sunny in {city}!"

# agent = create_react_agent(
#     model="anthropic:claude-3-7-sonnet-latest",  
#     tools=[get_weather],  
#     prompt="You are a helpful assistant"  
# )
# import axios from 'axios';
# import { readFile } from 'node:fs/promises';
# import express from 'express';
# import cors from 'cors';

# const app = express();
# const PORT = process.env.PORT || 3000;

# // Middleware
# app.use(cors()); // Enable CORS for all routes
# app.use(express.json()); // Parse JSON bodies
# app.use(express.static('public')); // Serve static files

# // Health check endpoint
# app.get('/health', (req, res) => {
#   res.json({ status: 'OK', message: 'Chatbot backend is running' });
# });

# // Chat endpoint
# app.post('/api/chat', async (req, res) => {
#   try {
#     const { message } = req.body;
    
#     if (!message || message.trim() === '') {
#       return res.status(400).json({ 
#         error: 'Message is required' 
#       });
#     }

#     const invokeUrl = "https://integrate.api.nvidia.com/v1/chat/completions";
#     const stream = false;

#     const headers = {
#       "Authorization": "Bearer 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",
#       "Accept": stream ? "text/event-stream" : "application/json",
#       "Content-Type": "application/json"
#     };

#     const payload = {
#       "model": "meta/llama-4-maverick-17b-128e-instruct",
#       "messages": [
#         {
#           "role": "system",
#           "content": "You are a helpful AI assistant. Provide clear, concise, and helpful responses."
#         },
#         {
#           "role": "user",
#           "content": message
#         }
#       ],
#       "max_tokens": 512,
#       "temperature": 0.7,
#       "top_p": 1.00,
#       "frequency_penalty": 0.00,
#       "presence_penalty": 0.00,
#       "stream": stream
#     };

#     console.log('Sending request to NVIDIA API...');
#     const apiResponse = await axios.post(invokeUrl, payload, {
#       headers: headers,
#       responseType: stream ? 'stream' : 'json',
#       timeout: 30000 // 30 second timeout
#     });

#     console.log('Received response from NVIDIA API');
    
#     // Extract the assistant's response
#     const assistantMessage = apiResponse.data.choices[0]?.message?.content || 'Sorry, I could not generate a response.';
    
#     res.json({
#       success: true,
#       message: assistantMessage,
#       timestamp: new Date().toISOString()
#     });

#   } catch (error) {
#     console.error('Error in chat endpoint:', error.message);
    
#     if (error.response) {
#       // API error
#       console.error('API Error Status:', error.response.status);
#       console.error('API Error Data:', error.response.data);
      
#       res.status(error.response.status || 500).json({
#         error: 'API Error',
#         message: error.response.data?.error?.message || 'Failed to get response from AI service',
#         details: error.response.status === 401 ? 'Invalid API key' : 'API service error'
#       });
#     } else if (error.request) {
#       // Network error
#       res.status(503).json({
#         error: 'Network Error',
#         message: 'Unable to reach AI service. Please try again later.'
#       });
#     } else {
#       // Other error
#       res.status(500).json({
#         error: 'Server Error',
#         message: 'An unexpected error occurred. Please try again.'
#       });
#     }
#   }
# });

# // Legacy endpoint for compatibility
# app.get('/api/invoke', async (req, res) => {
#   res.status(405).json({
#     error: 'Method Not Allowed',
#     message: 'Please use POST /api/chat instead'
#   });
# });

# // 404 handler
# app.use('*', (req, res) => {
#   res.status(404).json({
#     error: 'Not Found',
#     message: 'The requested endpoint does not exist'
#   });
# });

# // Start server
# app.listen(PORT, '0.0.0.0', () => {
#   console.log(`Chatbot backend server is running on port ${PORT}`);
#   console.log(`Health check: http://localhost:${PORT}/health`);
#   console.log(`Chat endpoint: POST http://localhost:${PORT}/api/chat`);
# });


# # Run the agent
# agent.invoke(
#     {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
# )

import os
from langchain.chat_models import init_chat_model

os.environ["GOOGLE_API_KEY"] = "AIzaSyA9PCcl6kf6aqejqqhsiA8wlfD0p9BJyDg"

llm = init_chat_model("google_genai:gemini-2.0-flash")
output = llm.invoke( [{"role": "user", "content": "what is the weather in sf"}])
print(output)

