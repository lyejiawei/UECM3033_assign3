UECM3033 Assignment #3 Report
========================================================

- Prepared by: Lye Jia Wei
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  Gauss-Legendre formula

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/lyejiawei/UECM3033_assign3](https://github.com/lyejiawei/UECM3033_assign3)
 

By using the Legendre function, the nodes and weights with any n from 1 to 100 is obtained. Nodes is represented by ‘x’ while weights is represented by ‘w’. Then, the x value is transformed into the integral from the interval [-1, 1] to [a, b]. The answer is calculated out by using the Gauss-Legendre Quadrature formula with np.polynomial.legendre.leggauss. The Jacobian of the transformation is calculated by using formula (b-a)/2.

My result of findings:
I = -139/6 + 34*log(2), 
I = 0.400338097411

---------------------------------------------------------

## Task 2 -- Predator-prey model

Numpy, scipy, and matpltlib.pyplot are imported from library. Then, a function called p(y,t) is defined. Array of prey and predator is created as pp. Prey and predator is calculated and pp is returned to p(y,t). Next, an array of y0 and y1 is created by using numpy and initial condition of y0=0.1 and y1=1.0 is initialized. Time from t=0 to t=5 is created by using linspace to return evenly spaced t over 0<t<5. Now, a system of ordinary differential equations can be solved using lsoda from the Fortran library odtepack with sp.integrate.odeint. The integrated answer is stored in array form. Then, graph of y0 and y1 against t and graph of y1 against y0 are plotted. Next, graph of y0 and y1 against t and graph of y1 against y0 are plotted again with different initial condition of y0=0.11 and y1=1.0. This is to test the sensitivity on initial conditions.

The following graphs are the result of my findings.
Figure 1: Graph of y0 and y1 against t with initial condition of y0=0.1, y1=1.0
Figure 2: Graph of y1 against y0 with initial condition of y0=0.1, y1=1.0
Figure 3: Graph of y0 and y1 against t with initial condition of y0=0.11, y1=1.0
Figure 4: Graph of y1 against y0 with initial condition of y0=0.11, y1=1.0


Figure 1: 
![y0 and y1 against t (1).png]


Figure 2:
![Prey vs Predator (1).png]


Figure 3:
![y0 and y1 against t (2).png]

Figure 4:
![Prey vs Predator (2).png]


As a conclusion, there is inverse relationship between prey and predator by the observation from the graphs. When the number of predators increases, the number of prey decreases, while other factors held constant. On the other hand, the changes in result of using different initial condition is insignificant.

The system of ODE is not sensitive to initial condition. This is because if the system of ODE is sensitive to initial condition, a small changes in initial condition will cause a large significant changes in system of ODE. 

-----------------------------------

<sup>last modified: 16/4/2016</sup>
