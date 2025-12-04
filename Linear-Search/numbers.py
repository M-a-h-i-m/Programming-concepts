number = [2,56,60,7,24,55,5,48,51,127,21,26,19,49,50,83,33,14,45,44]
target = 12

def LinearSearch(number,target):
  if(len(number) == 0):
      return "Add numbers to your array and then return home"
  for i in range(0,len(number)-1):
     if(number[i] == target):
        return f"Found the element at index {i}"
  return "The target is missing in the list"

print(LinearSearch(number,target))