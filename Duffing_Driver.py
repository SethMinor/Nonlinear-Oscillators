# Duffing Osc Integrator
# Cubic-order approx to nonlinear pendulum
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from duffing import duffing

# Parameters
# x'' + dx' + kx + bx^3 = gamma*fcn
k = -1 # Hooke stiffness
d = 0.1 # Damping
b = 1.3 # Nonlinear stifness
gamma = 1 # Forcing
params = [k,d,b,gamma]

# ICs
t0,tf = 0,60
Y0 = [1.6,-0.3,k,d,b,gamma]

# Integrate ODE
solution = integrate.RK45(duffing,t0,Y0,tf,\
    0.05, 0.0000001, 2.7**-9)

# Grab solution data
# (StackOverflow beta)
t_values = []
x_values = []
y_values = []

while True:
    solution.step()
    t_values.append(solution.t)
    x_values.append(solution.y[0])
    y_values.append(solution.y[1])
    # break loop after modeling is finished
    if solution.status == 'finished':
        break

# Plot solutions
fig, axs = plt.subplots(2)
fig.suptitle('Duffing Oscillator')
axs[0].plot(t_values, x_values)
axs[0].plot(t_values, y_values)
axs[1].plot(x_values, y_values)
