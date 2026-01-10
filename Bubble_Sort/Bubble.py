arr = [3,1,5,4,2]

for i in range(len(arr)-1):
  for j in range(len(arr)-1):
    if(arr[j] > arr[j+1]):
      copy = arr[j]
      arr[j] = arr[j+1]
      arr[j+1] = copy

print(arr)
