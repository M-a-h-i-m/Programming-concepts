arr = [3, 1, 5, 4, 2]

for i in range(len(arr)-1):
  max_idx = i

  for j in range(i+1,len(arr)):
    if(arr[max_idx] < arr[j] ):
      max_idx = j

  copy = arr[i]
  arr[i] = arr[max_idx]
  arr[max_idx] = copy

print(arr)
