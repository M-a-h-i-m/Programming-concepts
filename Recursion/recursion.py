#factorial number printing
#fact(5) = 5*4*3*2*1
def factorial(n):
  if(n <= 1):
    return 1
  else:
   fact = n * factorial(n-1)
   return fact
  

print(factorial(5))
  

