class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        i = 0

        # Cyclic sort
        while i < n:
            correct = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        # Find the missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

print(Solution().firstMissingPositive([3,4,-1,1]))   