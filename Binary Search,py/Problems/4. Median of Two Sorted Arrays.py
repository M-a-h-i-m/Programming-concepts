class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        if(len(nums) % 2 != 0):
            med = nums[(len(nums) // 2 )]
        else:
            idx1 = (len(nums) // 2) - 1
            idx2 =  len(nums) // 2 
            med = (nums[idx1] + nums[idx2]) / 2 
        return med
    
print(Solution().findMedianSortedArrays([1,2],[3,4]))