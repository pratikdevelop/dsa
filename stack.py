from re import A


class stack:
    top = -1
    arr =[]
    arrLength =0

    def __init__(self,arrLength):
        self.arr = [0]*arrLength
        self.arrLength = arrLength

    def isFull(self):
        if self.top == (self.arrLength-1):
            return True
        return False
    
    def isEmpty(self):
        if self.top == -1:
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

    def push(self):
        if(self.isFull()):
            print('stack is full')
        else:
            val = int(input('enter the value that you push in  stack'))
            self.top =self.top+1
            self.arr[self.top] = val  

    def pop(self):
        if(self.isEmpty()):
            print('stack is empty')
        else :
            self.arr[self.top] =0
            self.top= self.top -1

    def display(self):
        for i in range(0, self.arrLength):
            print(self.arr[i])

st = stack(5)
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
            st.push()
        case 4:
            st.pop()
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


        