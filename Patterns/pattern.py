#square
n = 5
print("Square: ")
print()
for i in range(n):
  print()
  for j in range(n):
    print("*",end=" ")


print()
print()
print()
print()
print()


###############################################################################################################################################################

#Triange

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
print()
print()
print()




###############################################################################################################################################################

#Ulta-Triange
print("Ulta-Triange: ")
print()

n = 5
for i in range(n):
  print(i * " ",end=" ")
  for j in range(5-i,0,-1):
    print("*",end=" ")
  print("")
  
  
 


print()
print()
print()
print()
print()



###############################################################################################################################################################

#Left-Triange

n = 5
print("Left-Triange: ")
print()


for i in range(n):
  print()
  for j in range(i+1):
    print("*",end=" ")


print()
print()
print()
print()
print()


###############################################################################################################################################################

#Ulta-Left-Triange
print("Ulta-Left-Triange: ")
print()

n = 5
for i in range(n):
  print()
  for j in range(n-i,0,-1):
    print("*",end=" ")


print()
print()
print()
print()
print()



###############################################################################################################################################################

#Right-Triange
print("Right-Triange: ")
print()

n = 5
for i in range(n):
  print(((n-1)*2 - (2*i)) * " ",end=" ")
  for j in range(i+1): 
    print("*",end=" ")
  print()
 


print()
print()
print()
print()
print()





###############################################################################################################################################################

#Ulta-Right-Triange
print("Ulta-Right-Triange: ")
print()

n = 5
for i in range(n):
  print(i * "  ",end="")
  for j in range(n-i,0,-1):
    print("*",end=" ")
  print("")
  
  
 


print()
print()
print()
print()
print()