number = [56,60,7,24,55,5,48,51,127,21,26,19,49,50,83,33,14,45,44,2]
minimum = number[0]

def LinearSearch(number,min):

  for i in range(0,len(number)):
     if(number[i] < min):
        minimum = number[i]

  return minimum

print(LinearSearch(number,minimum))