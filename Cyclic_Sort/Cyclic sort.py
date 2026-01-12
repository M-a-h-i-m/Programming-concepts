arr = [3, 5, 2, 1, 4]
i = 0
while i < len(arr):
  
  if(arr[i] != i+1):
     j = arr[i]-1  
     copy = arr[j]
     arr[j] = arr[i] 
     arr[i] = copy
  else:
     i+=1
    

print(arr)