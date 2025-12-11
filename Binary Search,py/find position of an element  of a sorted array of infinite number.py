array = [42,137,256,389,512,645,778,891,999,123,234,345,456,567,678,789,890,901,111,222,333,444,555,666,777,888,999,150,275,400,525]
array.sort()
#Imagine it's an infinite array.


target = 123
left = 0
right = 1

def binary(left,right,target):
  while left <= right:
      mid = (left + right) // 2
      if array[mid] == target:
          print(f"The target {target} is at index {mid}")
          break
      elif array[mid] < target:
          left = mid + 1
      elif array[mid] > target:
          right = mid - 1
  else:
      left = right + 1
      right = left + 1
      binary(left,right,target)
       