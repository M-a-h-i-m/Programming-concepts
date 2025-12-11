class Solution(object):
    def peakIndexInMountainArray(self, arr):
          start = 0
          end = len(arr) - 1

          while start < end:              #My own Algorithm 
              mid = (start + end) // 2
              if arr[mid] < arr[mid + 1]:
                  start = mid + 1
              else:
                  end = mid
          return start 
  

  
    
print(Solution().peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))