'''class Solution():
    def febnocci(self, n):
        if(n == 0):
            return 0
        if(n== 1):
            return 1
        return self.febnocci(n-1) + self.febnocci(n-2)

s1 = Solution()
print(s1.febnocci(3))

class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        
        size = len(candyType)
        return int(size/2)


candyType = [1,1,2,2,3,3]
s1 = Solution()
print(s1.distributeCandies(candyType))

import numpy as np

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        arr = nums1 +nums2
        
s1 =  Solution()
s1.findMedianSortedArrays([2,3,4],[6,8,9])'''

class Solution(object):
    def reverse(self,x):
        rev = 0
        x = str(x)
        if x[0] == '-':
            a = int('-' + x[-1:0:-1])
            if a >= -2147483648 and a<= 2147483647:
                return a
            else:
                return 0
        else:
            a = int(x[::-1])
            if a >= -2147483648 and a<= 2147483647:
                return a
            else:
                return 0
s1 = Solution()
result = s1.reverse(123)
print(result)