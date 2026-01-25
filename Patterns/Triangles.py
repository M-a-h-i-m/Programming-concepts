#Triange
print()
print()
n = 5

print("Triange: ")
print()


for i in range(n):
  print((n-i)*" ",end=" ")
  for j in range(i+1): 
    print("*",end=" ")
  print()


print()
print()


for i in range(n):
  print((i+1) * " ",end=" ")
  for j in range(n-i,0,-1):
    print("*",end=" ")
  print("")
  
  
 