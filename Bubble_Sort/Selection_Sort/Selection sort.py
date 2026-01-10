arr = [3, 1, 5, 4, 2]

for i in range(len(arr) - 1):
    min_index = i
     
    for j in range(i + 1, len(arr)): # Picked the smallest element index
        if arr[j] < arr[min_index]:
            min_index = j

    temp = arr[i]            # Swapped the picked index element with first index
    arr[i] = arr[min_index]
    arr[min_index] = temp

print(arr)
