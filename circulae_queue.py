from itertools import count


class Queue:
    font = rear= -1
    countItem = 0
    arr =[]
    arrLength =0

    def __init__(self,arrLength):
        self.arr = [0]*arrLength
        self.arrLength = arrLength

    def isFull(self):
        if ((self.rear+1)%self.arrLength) == (self.font):
            return True
        return False
    
    def isEmpty(self):
        if self.font == self.rear == -1:
            return True
        return False
    
    def change(self , position):
        if(self.arrLength > position):
            a = int(input('enter the change VAlue'))
            self.arr[position]= a
        else:
            print('this position is not preset in stack ')
    
    def peek(self, position):
        if(self.isEmpty()):
            print('stack is empty')
            return
        elif(self.arrLength < position):
            print('position is out of index in array')
            return
        print(f"peek value of array  is {self.arr[position]}")

    def enqueue(self):
        if(self.isFull()):
            print('stack is full')
            return

        elif(self.isEmpty()):
            self.font = self.rear = 0
        else:
            self.rear =(self.rear+1)%self.arrLength

        val = int(input('enter the value that you push in  stack'))
        self.arr[self.rear] = val  
        self.countItem  += 1

    def dequeue(self):
        x =0 

        if(self.isEmpty()):
            print('stack is empty')
        elif(self.font == self.rear):
            x= self.arr[self.font]
            self.arr[self.font] =0
            self.font= self.rear = -1
        else :
            x= self.arr[self.font]
            self.arr[self.font] =0
            self.font =( self.font+1)%self.arrLength
        self.countItem  -= 1
        return x

    def count(self):
        print('count Item :' , self.countItem)
    def display(self):
        for i in range(0, self.arrLength):
            print(self.arr[i])

st = Queue(5)
while True:
    a = int(input('enter the no :'))
    match a :
        case 1:
            if(st.isEmpty()):
                print('stack is empty')
            else:
                print('stack is not empty')
        case 2:
            if(st.isFull()):
                print('stack is FUll')
            else:
                print('stack is not Full')
        case 3:
            st.enqueue()
        case 4:
            st.dequeue()
        case 5:
            pos = int(input('enter the position this will change you'))
            st.change(pos)
        case 6:
            pos = int(input('enter the position that you will give the value'))
            st.peek(pos)
        case 7:
            st.display()
        case 8:
            break
8