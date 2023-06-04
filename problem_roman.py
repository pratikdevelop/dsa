
# class Solution(object):
#     def romanToInt(self, s):
#         roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
#         i = 0
#         num = 0
#         while i < len(s):
#             if i+1<len(s) and s[i:i+2] in roman:
#                 num+=roman[s[i:i+2]]
#                 i+=2
#             else:
#                 #print(i)
#                 num+=roman[s[i]]
#                 i+=1
#         return num    

# s =Solution()
# print(s.romanToInt('III'))

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1 = ListNode()
        l1 = l1
        print(l1.next)


s1 = Solution()
s1.addTwoNumbers([2,4,3], [5,6,4])
        