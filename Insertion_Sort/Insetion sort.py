arr = [2, 5, 3, 4, 1]

for i in range(len(arr)-1):
  for j in range(i+1,0,-1):
    if(arr[j]<arr[j-1]):
      copy = arr[j-1]
      arr[j-1] = arr[j]
      arr[j] = copy
    else:
      break
    
print(arr)