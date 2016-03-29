import numpy as np
import matplotlib.pyplot as plt

a=float(raw_input('please input a: '))
b=float(raw_input('please input b: '))
sta=float(raw_input('please input the initial N: '))
dt=float(raw_input('please input dt: '))
end_t=float(raw_input('please input the end time: '))
N=[]
t=[]
N.append(sta)
t.append(0.0)

for i in range(int(end_t/dt+1)):
    sN=N[i]+(a*N[i]-b*N[i]**2)*dt
    t.append(dt*(i+1))
    N.append(sN)
    print t[i],N[i]

plt.title('Problem 1.6')
plt.xlabel('Time/unit')
plt.ylabel('Population/unit')
plt.plot(t,N,marker='o')
plt.show()

