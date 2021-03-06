import numpy as np
import matplotlib as mpl  
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt
import math

x=[]
y=[]
z=[]
t=[]
m=[]
n=[]
w=[]
p=[]
v=[]
s=[]
vin=float(raw_input('please input the firing speed(unit:m/s): '))
ang=float(raw_input('please input the firing angle(unit:degree): '))
lat=float(raw_input('please input the latitude(unit:degree): '))
B=4e-5
dt=0.1
g=9.8
DA=6.371e6
DB=7.29e-5
a=math.radians(ang)
b=math.radians(lat)
#vinn=v-DA*DB*math.cos(b)
#fco=2*DB*vinn
x.append(0.0)
y.append(0.0)
z.append(0.0)
t.append(0.0)
m.append(vin*math.cos(a))
n.append(vin*math.sin(a))
w.append(0.0)

for i in range(0,100000):
    sv=(m[i]**2+n[i]**2+w[i]**2)**0.5
    sp=math.exp(-z[i]/10000)
    sx=x[i]+m[i]*dt
    sm=m[i]-B*sp*sv*m[i]*dt
    sz=z[i]+n[i]*dt
    sn=n[i]-g*dt-B*sp*sv*n[i]*dt-2*DB*(sv-DA*DB*math.cos(b))*math.cos(b)*dt
    sy=y[i]+w[i]*dt
    sw=w[i]+2*DB*(sv-DA*DB*math.cos(b))*math.sin(b)*dt
    x.append(sx)
    m.append(sm)
    y.append(sy)
    n.append(sn)
    z.append(sz)
    w.append(sw)
    v.append(sv)
    p.append(sp)
    t.append(dt*(i+1))
    #print x[i],m[i],z[i],n[i],t[i],y[i]
    if z[i+1]<0:
        break

print x[-2],y[-2],v[-1],math.degrees(math.atan(abs(n[-1])/abs((m[-1]**2+w[-1]**2))**0.5))
if __name__ == "__main__":  
    #mpl.rcParams["legend.fontsize"] = 10  
    fig = plt.figure()  
    ax = Axes3D(fig)  
   
    ax.set_title('picture 6')
    ax.set_xlabel('x/m')
    ax.set_ylabel('y/m')
    ax.set_zlabel('z/m')
    ax.plot(x, y, z, label ='added Coriolis force')  
    ax.legend()  

    plt.show()  
  

