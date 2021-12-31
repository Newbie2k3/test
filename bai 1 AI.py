import math
x = 0
y = 0
while (True):
    a,b =  input().split()
    b = int(b)
    if (a == "END") : break;    
    if (a == "DOWN") :
        b = -b
        x += b        
    elif(a == "UP"):    
        x += b          
    elif (a == "LEFT"):
        b = -b
        y += b        
    else : y += b    
    
s = math.sqrt(x*x + y*y)
print("OUTPUt ",round(s))