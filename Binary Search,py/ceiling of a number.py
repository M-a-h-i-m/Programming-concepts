array = [56, 60, 7, 24, 55, 5, 48, 51, 127, 21, 26, 19, 49, 50, 83, 33, 14, 45, 44, 2]
array.sort()
print(array)

target = 12
left = 0
right = len(array) - 1
ceil_index = -1  

while left <= right:
    mid = (left + right) // 2
    if array[mid] == target:
        print(f"The target {target} is at index {mid}")
        break
    elif array[mid] < target:
        left = mid + 1
    else:
        ceil_index = mid   
        right = mid - 1
else:
    if ceil_index != -1:
        print(f"Target not found. The ceil of {target} is {array[ceil_index]} at index {ceil_index}")
    else:
        print(f"Target not found. No ceil exists (target > all elements).")


# The ceiling of a number is the smallest integer that is greater than or equal to that number