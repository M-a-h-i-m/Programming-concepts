class Solution(object):
    def searchRange(self, nums, target):
        if not nums:  # handle empty list
            return [-1, -1]

        k = []
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # safety check to prevent index errors when list shrinks
            if mid >= len(nums):
                break

            if nums[mid] == target:
                k.append(mid)
                nums.pop(mid)
                # don’t continue blindly — reset pointers after removal
                left = 0
                right = len(nums) - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if not k:
            return [-1, -1]

        k.sort()
        return k


print(Solution().searchRange([1], 1))
