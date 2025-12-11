class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        start, end = 0, mountainArr.length() - 1

        while start < end:
            mid = (start + end) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                start = mid + 1
            else:
                end = mid
        peak = start

        start, end = 0, peak
        while start <= end:
            mid = (start + end) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                start = mid + 1
            else:
                end = mid - 1
        start, end = peak + 1, mountainArr.length() - 1
        while start <= end:
            mid = (start + end) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:  
                end = mid - 1
            else:
                start = mid + 1

        return -1

