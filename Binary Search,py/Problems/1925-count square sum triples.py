import math
class Solution(object):
    def countTriples(self, n):
      count = 0
      for i in range(2,n+1):
         for j in range(i+1,n+1):
           k =  math.sqrt(i*i+j*j)
           if(k<=n and k.is_integer()):  
            count = count + 2 
      return count         
         

print(Solution().countTriples(10))

