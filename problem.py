'''class Solution:
#     def convert(self, str: str, n: int) -> str:
       
#         if n == 1:
#             print(str)
#             return

#         l = len(str)

#         arr = ["" for x in range(l)]

#         row = 0

#         for i in range(l):

#             arr[row] += str[i]

#             if row == n - 1:
#                 down = False

#             elif row == 0:
#                 down = True

#             if down:
#                 row += 1
#             else:
#                 row -= 1

#         for i in range(n):
#             print(arr[i], end="")

# str = "PAYPALISHIRING"
# N = 3
# s1 = Solution()
# s1.convert(str, N)

# from cmath import log


# class Solution(object):
#     def longestPalindrome(self, s):
#         self.maxlen = 0
#         self.start = 0
            
#         for i in range(len(s)):
#             self.expandFromCenter(s,i,i)
#             self.expandFromCenter(s,i,i+1)
#         return s[self.start:self.start+self.maxlen]
            

#     def expandFromCenter(self,s,l,r):
#         while l > -1 and r < len(s) and s[l] ==s[r]:
#             l -= 1
#             r += 1
#         print(l ,r)
#         if self.maxlen < r-l-1:

#             self.maxlen = r-l-1
#             self.start = l + 1
class Solution(object):
#     def isPalindrome(self, x):
#         if(x < 0 or (x % 10 == 0 and x != 0)) :
#             return False

#         revertedNumber = 0
#         while(x > revertedNumber) :
#             revertedNumber = revertedNumber * 10 + x % 10
#             x /= 10
                   
#         return x == revertedNumber or x == revertedNumber/10;

# s1 = Solution()
# ans = s1.isPalindrome(121)
# print(ans)           
# # Program to implement a stack using
# # two queue
# from _collections import deque

# class MyStack:
	
# 	def __init__(self):
		
# 		# Two inbuilt queues
# 		self.q1 = deque()
# 		self.q2 = deque()

# 	def push(self, x):
		
# 		# Push x first in empty q2
# 		self.q2.append(x)

# 		# Push all the remaining
# 		# elements in q1 to q2.
# 		while (self.q1):
# 			self.q2.append(self.q1.popleft())


# 		# swap the names of two queues
# 		self.q1, self.q2 = self.q2, self.q1

# 	def pop(self):

# 		# if no elements are there in q1
# 		if self.q1:
# 			return self.q1.popleft()

# 	def top(self):
# 		if (self.q1):
# 			return self.q1[0]
# 		return None


# 	def empty(self):
# 		return len(self.q1)>1 if True else False 


# # Driver Code
# if __name__ == '__main__':
# 	s = MyStack()
# 	# print(s.push(1))
# 	# print(s.push(2))
# 	# print(s.top())
# 	# print(s.pop())
# 	print(s.empty())


# # This code is contributed by PranchalK
from asyncio.windows_events import NULL
from itertools import count
import math
from operator import le


class Solution:
    def rob(self, nums):
        count = len(nums)
        print(count)
        if(count == 0):
            return 0
        if(count >0 and count<3):
            return  max(nums[0], nums[count-1])
        memo = nums[:] 
        memo[1] = max(nums[0], nums[1])
        
        for i in range(2, count):
            memo[i] = max(memo[i-1], nums[i] + memo[i-2]) 
        
        return memo[count-1]
s1 = Solution()
print(s1.rob([1,2,3,1]))
print(s1.rob([2,7,9,3,1]))
print(s1.rob([3]))
print(s1.rob([0,4,3]))
print(s1.rob([2,1,1,2]
))'''

from errno import ERANGE
from platform import node


   
class Solution:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def rightSideView(self, root):
    
        tt  = TreeNode(1,2,3)
        print(tt.left)
        t1 = TreeNode('NULL', 5 , "NULL")
        print(t1.val)
ss = Solution()
ss.rightSideView([1,2,3,'NULL',5,'NULL',4])
ss.rightSideView([])
