#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##  Vector Forces
import math
x=input("Force in x coordinate: ")
x=float(x)
y=input("Force in y coordinate: ")
y=float(y)

def resultant(x,y):
    r=((x**2)+y**2)**0.5
    return(r)
result=resultant(x,y)


print('The resultant force is ',resultant(x,y) )


      
def angle(x,y):
    theta=math.degrees(math.atan(y/x))
    return(theta)
result2=angle(x,y)
print('The angle is ', angle(x,y), 'degrees')

