#Right-Triange

print()
print("Right-Triange: ")
print()

n = 5
for i in range(n):
  print(((n-1)*2 - (2*i)) * " ",end="")
  for j in range(i+1): 
    print("*",end=" ")
  print()
 


print()
print()

for i in range(n):
  print((i) * "  ",end="")
  for j in range(n-i,0,-1):
    print("*",end=" ")
  print("")
  
  
 


print()
print()
