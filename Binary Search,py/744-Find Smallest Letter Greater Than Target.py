class Solution(object):
    def nextGreatestLetter(self, letters, target):
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        k = left % len(letters)
        j = letters[k]
        return j

print(Solution().nextGreatestLetter(['c','c','c','c','c','c','c','c', 'f', 'f','f','f','f','f','f','f','f','f','f'], 'c'))
