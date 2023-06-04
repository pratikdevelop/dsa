'''import math

class Solution(object):
    def searchInsert(self, nums, target):

        start = 0
        end = len(nums)
        mid = int(math.floor((start+end)/2))
        find = False
        if (mid == 0):
            if(nums[mid] == target):
                find = True
                return mid
        else:
            if(nums[mid] > target):
                for i in range(0, mid):
                    if(nums[i] == target):
                        find = True
                        return i
                    elif (nums[i] < target and nums[i+1] > target):
                        return (i+1)

            else:
                for j in range(0, len(nums)-1):
                    print('demo',nums[j])
                    print('demo',nums[j+1])
                    if(nums[j] == target):
                        return j

                    elif (nums[j] < target and nums[j+1]>target):
                        return (j)
        if(find == False):
            return len(nums)
           
s1 = Solution()
dd=s1.searchInsert([1,3,5,6],2)
print(dd)


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range (0, len(nums)):
            nums[i] *= nums[i]
            
        for j in range(0,len(nums)-1):
            for  k in range(j, len(nums)):
                
                if(nums[j] >nums[k]):
                    swap =nums[k]
                    nums[k]  =nums[j]
                    nums[j] = swap
            
        return nums




# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         for i in range(0,k):
#             ele= nums.pop()
#             nums.insert(0,ele)
#         return nums


class Solution(object):
     def rotate(self,nums,K):
        n = len(nums)
        p1 = nums[0:K+1]

        # Reverse the elements from K
        # till the end of the array
        p2 = nums[K+1:]
        arr =  p2+p1

        return arr;'''

'''class Solution(object):
     def rotate(self,nums):
        n = len(nums)
        count=0
        for i in range(n):
            if nums[i] != 0:
                print(count)
                print(i)               # here count is incremented
                nums[count] = nums[i]
                count+=1
        
        # Now all non-zero elements have been
        # shifted to front and 'count' is set
        # as index of first 0. Make all
        # elements 0 from count to end.
        while count < n:
            nums[count] = 0
            count += 1

        return nums
'''

class Solution(object):
    def twoSum(self, numbers, target):
        head = 0
        tail = len(numbers) - 1
        while numbers[head] + numbers[tail] != target:
            if numbers[head] + numbers[tail] > target:
                tail -= 1
            else:
                head += 1
        return [head + 1, tail + 1]
s1 = Solution()
print(s1.twoSum([1,0,3,4,4,6,7], 14))


# class Solution(object):
#     def diagonalSum(self, mat):
#         """
#         :type mat: List[List[int]]
#         :rtype: int
#         """
#         sum = 0
#         for i in range(0, len(mat)):
#             for j in range(0, len(mat)):
#                 if  i == j:
#                     sum  +=  mat[i][j] 
#                 if ((i == len(mat)-1  and j == 0) or (j == len(mat)-1 and i==0)):
#                     sum  +=  mat[i][j] 
#         return sum