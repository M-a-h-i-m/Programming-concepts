class Solution(object):
    def findErrorNums(self, nums):
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
        print(nums)
        # Find missing number
        for i in range(n): 
            if i+1 != nums[i]:
              num.append(nums[i])  
              k = [i+1]
              l = num + k 
        return l
print(Solution().findErrorNums([1,1])) 