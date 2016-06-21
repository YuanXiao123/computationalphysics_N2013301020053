import numpy as np
import matplotlib.pyplot as plt
import math

x=[]
y=[]
t=[]
m=[]
n=[]
v=[]
p=[]
ang=float(raw_input('please input the firing angle(unit:degree): '))
B=4e-5
dt=0.1
g=9.8
a=math.radians(ang)
x.append(0.0)
y.append(0.0)
t.append(0.0)
m.append(700*math.cos(a))
n.append(700*math.sin(a))

for i in range(0,100000):
    sv=(m[i]**2+n[i]**2)**0.5
    sp=math.exp(-y[i]/10000)
    sx=x[i]+m[i]*dt
    sm=m[i]-B*sp*sv*m[i]*dt
    sy=y[i]+n[i]*dt
    sn=n[i]-g*dt-B*sp*sv*n[i]*dt
    x.append(sx)
    m.append(sm)
    y.append(sy)
    n.append(sn)
    v.append(sv)
    p.append(sp)
    t.append(dt*(i+1))
    print x[i],m[i],y[i],n[i],t[i],v[i]
    if y[i+1]<0:
        break

print v[-1],math.degrees(math.atan(abs(n[-1])/abs(m[-1])))
plt.title('Problem 2.9')
plt.xlabel('x/m')
plt.ylabel('y/m')
plt.plot(x,y,marker='o',linewidth=1)
plt.show()



    
    
