import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def p(y,t):
    a=1.0
    b=0.2
    prey=a*(y[0]-(y[0]*y[1]))
    predator=b*(-y[1]+(y[0]*y[1]))
    pp=[prey, predator]
    return pp

#Integrate from 0 to 5 for y0(0)=0.1 and y1(0)=1.0    
y=np.array([0.1,1.0])
t=np.linspace(0,5,1000)
ans=sp.integrate.odeint(p,y,t)

#Plot the graphs of y0 and y1 against t (1)
plt.plot(t,ans)
plt.plot(t,ans[:,0], label='Prey', color="blue")
plt.plot(t,ans[:,1], label='Predator', color="red")
plt.axis([0,5,0,1])
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('y0 and y1 against t (1)')
plt.grid(True)
plt.legend(loc='best')
plt.show()

#Plot the graph of y1 against y0 (1)
plt.plot(ans[:,0], ans[:,1])
plt.axis([0.1,0.5,0.4,1])
plt.xlabel('Prey')
plt.ylabel('Predator')
plt.title('Prey vs Predator (1)')
plt.grid(True)
plt.legend(loc='best')
plt.show()

#Integrate from 0 to 5 for y0(1)=0.11 and y1(1)=1.0
y=np.array([0.11,1.0])
t=np.linspace(0,5,1000)
ans=sp.integrate.odeint(p,y,t)

#Plot the graphs of y0 and y1 against t (2)
plt.plot(t,ans)
plt.plot(t,ans[:,0], label='Prey', color="blue")
plt.plot(t,ans[:,1], label='Predator', color="red")
plt.axis([0,5,0,1])
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('y0 and y1 against t (2)')
plt.grid(True)
plt.legend(loc='best')
plt.show()

#Plot the graph of y1 against y0 (2)
plt.plot(ans[:,0], ans[:,1])
plt.axis([0.1,0.5,0.4,1])
plt.xlabel('Prey')
plt.ylabel('Predator')
plt.title('Prey vs Predator (2)')
plt.grid(True)
plt.legend(loc='best')
plt.show()


