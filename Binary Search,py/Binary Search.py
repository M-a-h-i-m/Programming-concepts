array = [56, 60, 7, 24, 55, 5, 48, 51, 127, 21, 26, 19, 49, 50, 83, 33, 14, 45, 44, 2]
array.sort()  

target = 127
left = 0
right = len(array) - 1

while left <= right:
    mid = (left + right) // 2
    if array[mid] == target:
        print(f"The target {target} is at index {mid}")
        break
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Target not found")
