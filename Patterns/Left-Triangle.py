#Left-Triange
print()
n = 5
print("Left-Triange: ")



for i in range(n):
  print()
  for j in range(i+1):
    print("*",end=" ")


print()
print()


for i in range(n):
  print()
  for j in range(n-i,0,-1):
    print("*",end=" ")


print()
print()


