
from ctypes import sizeof
from itertools import count
import math
from sre_constants import JUMP
from tokenize import Number

'''
arr = [-2,-4, 5 ,-6 ,5 ,-3,6 ,-4]
arr1 = [1,2,6,10,34,56,67]
def maxSubArray(num , arr):
    max_count = 0
    temp_count =0
    for i in range(0, num-1):
        temp_count += arr[i]
        if(max_count < temp_count):
            max_count = temp_count

        if(temp_count< 0):
            temp_count = 0

        print(max_count)
def searchWithArray(length, arr, start, searchValue):

    midPoint =  math.floor((start+length)/2)
    if(arr[midPoint] <  arr[midPoint -1]):
        for i in range(start, midPoint):
            if(arr[i] ==searchValue):
                return i
    else:
        for j in range(midPoint, length-1):
            if(arr[j] ==searchValue):
                return j

# (maxSubArray(len(arr), arr))
# a =int(input('enter the no that you will search in array'))
# pos = searchWithArray(len(arr1), arr1, 0, a)
'''



arr1 = [1,2,6,10,34,56,67]
arr2 = [1,3,5,8,9,2,6,7,6,8,9]
# def compareArrays(arr1, arr2, arraySize):

#     # arr1.sort(), arr2.sort()
#     arr1 = sorted(arr1)
#     arr2 = sorted(arr2)
#     count =0
#     for  i in range(arraySize):
#         if arr1[i] == arr2[i]:
#             count  +=1

#     if(count == arraySize):
#         return True
#     return False
# pos = compareArrays(arr1, arr2,  6)
# print(pos)


def fibnociseries(arrLength):
    
    if(arrLength == 0):
        return 0
    if arrLength == 1:
        return 1
    else:
        return (fibnociseries(arrLength-1)+ int(fibnociseries(arrLength-2)))


def countArrayJumps(arr, sizeOfAray, start):
    jumps=[0 for i in range(sizeOfAray)]
    if(arr[start] == 0):
        return 0
    if(start == sizeOfAray):
        return 0
    else :
        jumps[0]= 0
        for i in range(1,sizeOfAray):
            jumps[i] = float('inf')
            for j in range(i):
                print(jumps)
                print( jumps[j+1])
                if((i <= j+arr[j]) and jumps[i] != 'inf'):
                    jumps[i] =  min(jumps[i], jumps[j]+1)
                    break
        print(jumps)
        print(sizeOfAray)
        return jumps[sizeOfAray-1]
arr1 =[0]
a = countArrayJumps(arr1, len(arr1), 0)
print(a)

def in_range(n): #check if every split is in range 0-255
	if n >= 0 and n<=255:
		return True
	return False
	
def has_leading_zero(n): # check if eery split has leading zero or not.
	if len(n)>1:
		if n[0] == "0":
			return True
	return False
def isValid(s):
	
	s = s.split(".")
	if len(s) != 4: #if number of splitting element is not 4 it is not a valid ip address
		return 0
	for n in s:
		
		if has_leading_zero(n):
			return 0
		if len(n) == 0:
			return 0
		try: #if int(n) is not an integer it raises an error
			n = int(n)

			if not in_range(n):
				return 0
		except:
			return 0
	return 1
		

if __name__=="__main__":
	
	
	ip1 = "222.111.111.111"
	ip2 = "5555..555"
	ip3 = "0000.0000.0000.0000"
	ip4 = "1.1.1.1"
	print(isValid(ip1))
	print(isValid(ip2))
	print(isValid(ip3))
	print(isValid(ip4))

	
# this code is contributed by Vivek Maddeshiya.


'''arr = [1,0,2]

def jumpArray(arr, size):
    jumps=[0 for i in range(size)]
    if(arr[0] == 0):
        return 0
    else :
        jumps[0]= 0
    for i in range(1, size):
        jumps[i] = float('inf')
        for j in range(i):
            print(jumps[i])
            if((i <= j+arr[j]) and jumps[i] != 'inf'):

                jumps[i] =  min(jumps[i], jumps[j]+1)
                break
    return jumps[size-1]

print(jumpArray(arr , len(arr)))
'''