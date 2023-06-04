# '''import sys
# class Solution(object):
#     def threeSum(self, nums, target):
#         closestSum = sys.maxsize
#         for i in range(len(nums)):
#             for j in range (i+1, len(nums)):
#                 for k in range(j+1 , len(nums)):
#                      if(abs(target - closestSum) >
#                         abs(target - (nums[i] +
#                         nums[j] + nums[k]))):
#                             closestSum = (nums[i] +
#                                             nums[j] + nums[k])
#         return closestSum'''
# '''class Solution(object):
#  def threeSum(self, nums):
#         nums, result, i = sorted(nums), [], 0
#         while i < len(nums) - 2:
#             j, k = i + 1, len(nums) - 1
#             while j < k:
#                 if nums[i] + nums[j] + nums[k] < 0:
#                     j += 1
#                 elif nums[i] + nums[j] + nums[k] > 0:
#                     k -= 1
#                 else:
#                     result.append([nums[i], nums[j], nums[k]])
#                     j, k = j + 1, k - 1
#                     while j < k and nums[j] == nums[j - 1]:
#                         j += 1
#                     while j < k and nums[k] == nums[k + 1]:
#                         k -= 1
#             i += 1
#             while i < len(nums) - 2 and nums[i] == nums[i - 1]:
#                 i += 1
#         return result'''

# import string



# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummyHead = ListNode(0)
#         curr = dummyHead
#         carry = 0
#         while l1 != None or l2 != None or carry != 0:
#             l1Val = l1.val if l1 else 0
#             l2Val = l2.val if l2 else 0
#             columnSum = l1Val + l2Val + carry
#             carry = columnSum // 10
#             newNode = ListNode(columnSum % 10)
#             curr.next = newNode
#             curr = newNode
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         return dummyHead.next
        
# class Solution(object):
#     def addTwoNumbers(self,l1, l2):
#         sum  = []
#         for i in  reversed(range(len(l1))):
#             add = l1[i]+l2[i]
#             str = string(add)  
#             if str.isdigit() == True:  
#                 print(str)  
#             else:  
#                 print(str)  

# s1 = Solution()
# (s1.addTwoNumbers([5,4,3], [2,6,4]))

import math
class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums)
        mid = int(math.floor((start+end)/2))
        find = False
        if (mid == 0):
            print('de')
            if(nums[mid] == target):
                find = True
                return mid
        else:
            print(mid)
            if(nums[mid-1] <= nums[mid]):
                for i in range(0, mid):
                    if(nums[i] == target):
                        find = True
                        return i
            else:
                for j in range(mid, len(nums)):
                    
                    if(nums[j] == target):
                        find=True
                        return j
        if(find == False):
            return -1


s1 = Solution()
print(s1.search([2,5], 2))