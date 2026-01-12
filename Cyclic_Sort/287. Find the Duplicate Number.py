class Solution(object):
    def findDuplicate(self, nums):
        i = 0
        n = len(nums)

        # Cyclic sort
        while i < n:
            correct = nums[i]
            if correct < n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        
        # Find missing number
        for i in range(n): 
            if i+1 != nums[i]:
                return nums[i]
        return n
       
print(Solution().findDuplicate([1,3,4,2,2]))       