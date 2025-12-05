array = [
  [1,2,3],
  [4,5,6,10,5,2],
  [7,8,9,4]
]
target = 10

def Search(array,target):
 for i in range(0,len(array)):
  for j in range(0,len(array[i])):
   if(array[i][j] == target):
    return f"The element found at index {i,j}"
 return [-1,-1]

print(Search(array,target))