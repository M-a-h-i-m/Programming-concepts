class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        nums.reverse()
        return nums[k-1]


print(Solution().findKthLargest([3,2,1,5,6,4],2)) 