class Solution(object):
    def findDuplicates(self, nums):
        i = 0
        n = len(nums)
        num = []
        # Cyclic sort
        while i < n:
            correct = nums[i] - 1
            if correct < n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        
        # Find missing number
        for i in range(n): 
            if i+1 != nums[i]:
              num.append(nums[i])  
        return num
       
       
print(Solution().findDuplicates([1])) 