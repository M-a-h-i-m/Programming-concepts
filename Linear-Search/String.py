String = "Linear"
target = 'i'

def LinearSearch(String,target):
  if(len(String) == 0):
      return "Add characters to your String and then return home"
  for i in range(0,len(String)-1):
     if(String[i] == target):
        return f"Found the element at index {i}"
  return "The target is missing in the list"

print(LinearSearch(String,target))