array = [2, 6, 10, 16, 19, 21, 28]

target = 11
left = 0
right = len(array) - 1
floor_index = -1  

while left <= right:
    mid = (left + right) // 2
    if array[mid] == target:
        print(f"The target {target} is at index {mid}")
        break
    elif array[mid] < target:
        floor_index = mid 
        left = mid + 1
    else:
       floor_index = right 
       right = mid - 1 
        
else:
    if floor_index != -1:
        print(f"Target not found. The floor of the number is at index {floor_index}")
    else:
        print(f"Target not found. No floor exists (target > all elements).")


