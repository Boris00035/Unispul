# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:38:03 2021

@author: pjsva

Simulation of the collegedemonstraties double pendulum

Partially based on https://scipython.com/blog/the-double-pendulum/
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib import animation

""" 
Parameters
Values are measured by hand - see written notes 
Calculations can be entered in script at some point
"""
### Pendulum 1
m1 = 389.4e-3 # Mass [kg]
l1 = 11.5e-2 # Distance rotation axis - center of gravity of P1 [m]
L1 = 24.75e-2 # Distance between two rotation axes [m]
I1 = 3.72e-3 # Moment of intertia [kgm^2]
L1tot = 27.95e-2 # Total length of P1 - just for plotting purposes [m]

### Pendulum 2
m2 = 113.7e-3 # Mass [kg]
l2 = 10.3e-2 # Distance second rotation axis - center of gravity of P2 [m]
I2 = 5.34e-4 # Moment of intertia [kgm^2]
L2 = 22.4e-2 # Distance rotation axis - end of P2
L2tot = 23.5e-2 # Total length of P2 - just for plotting purposes [m]

### General
g = 9.81 # Gravitational acceleration [ms^-2]

### Collected
par = [m1, l1, L1, I1, m2, l2, I2, g]

### Initial state at t=0 (th1,dth1dt,th2,dth2dt)
y0 = (np.pi/2,0,np.pi/3,0)

"""
Function definitions
"""

### Derivatives 
# input: y = [th1,dth1dt,th2,dth2dt], t, m1, l1, L1, I1, m2, l2, I2, g 
def deriv(y, t, par):
    ### Parameter and variable definitions
    m1, l1, L1, I1, m2, l2, I2, g = par
    th1, dth1dt, th2, dth2dt = y
    ### Help functions
    a = m1*l1**2 + m2*L1**2 + I1
    b = m2*L1*l2*np.cos(th1 - th2)
    c = m2*L1*l2*np.sin(th1 - th2)*dth2dt**2 + (m1*g*l1 + m2*g*L1)*np.sin(th1)
    d = m2*l2**2 + I2
    f = -m2*L1*l2*np.sin(th1 - th2)*dth1dt**2 + m2*g*l2*np.sin(th2)
    ### Definition of second order derivatives
    d2th1dt2 = (b*f - c*d)/(a*d - b*b)
    d2th2dt2 = (c*b - a*f)/(a*d - b*b)
    return dth1dt, d2th1dt2, dth2dt, d2th2dt2

### Total energy (still to correct)
# def calc_E(y):
#     """Return the total energy of the system."""

#     th1, th1d, th2, th2d = y.T
#     V = -(m1+m2)*L1*g*np.cos(th1) - m2*L2*g*np.cos(th2)
#     T = 0.5*m1*(L1*th1d)**2 + 0.5*m2*((L1*th1d)**2 + (L2*th2d)**2 +
#             2*L1*L2*th1d*th2d*np.cos(th1-th2))
#     return T + V
#%%
"""
Simulation
"""

# Maximum time, time point spacings and the time grid (all in s).
tmax, dt = 30, 0.005
t = np.arange(0, tmax+dt, dt)
# Do the numerical integration of the equations of motion
y = odeint(deriv, y0, t, args=(par,))

# Angles and positions as a function of time
theta1, theta2 = y[:,0], y[:,2]
# Convert to Cartesian coordinates of the two bob positions.
x1 = L1*np.sin(theta1)
y1 = -L1*np.cos(theta1)
x2 = x1 + L2*np.sin(theta2)
y2 = y1 - L2*np.cos(theta2)


plt.figure()
plt.subplot(211)
plt.plot(t,theta1,'k-')
plt.ylabel('$\\theta_1$ (rad)')
plt.subplot(212)
plt.plot(t,theta2,'r-')
plt.ylabel('$\\theta_2$ (rad)')
plt.show()



#%%

"""
Animation (still working on this)
"""

n = 1000
# x12 = np.transpose([np.zeros(len(x1)),x1,x2])
# y12 = np.transpose([np.zeros(len(x1)),y1,y2])
x12 = np.transpose([np.zeros(n),x1[0:n],x2[0:n]])
y12 = np.transpose([np.zeros(n),y1[0:n],y2[0:n]])

plotrange = L1 + L2

#  Define plot environment
fig = plt.figure()
ax = plt.axes(xlim=(-plotrange, +plotrange), ylim=(-plotrange, +plotrange))
line, = ax.plot([], [], lw=2, c='k')
#line, = ax.plot([], [],'r.')

# Animated part of the plot. This part of the plot is updated 
def animate(i):
    line.set_data(x12[i],y12[i])
    return line,

# Call the animator. blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, frames=n, interval=int(dt*1000), blit=True)

# Save the animation to mp4, using the ffmpeg writer
Writer = animation.writers['ffmpeg']
# writer = Writer(fps=30, bitrate=1800)
# anim.save('C:/Temp/doublependulum.mp4',writer=writer)

plt.show()

# # Plotted bob circle radius
# r = 0.01

# def make_plot(i):
#     # Plot and save an image of the double pendulum configuration for time
#     # point i.
#     # The pendulum rods.
#     ax.plot([0, x1[i], x2[i]], [0, y1[i], y2[i]], lw=2, c='k')
#     # Circles representing the anchor point of rod 1, and bobs 1 and 2.
#     c0 = Circle((0, 0), r/2, fc='k', zorder=10)
#     c1 = Circle((x1[i], y1[i]), r, fc='b', ec='b', zorder=10)
#     c2 = Circle((x2[i], y2[i]), r, fc='r', ec='r', zorder=10)
#     ax.add_patch(c0)
#     ax.add_patch(c1)
#     ax.add_patch(c2)
    
# # Make an image every di time points, corresponding to a frame rate of fps
# # frames per second.
# # Frame rate, s-1
# fps = 10
# di = int(1/fps/dt)
# fig = plt.figure(figsize=(8.3333, 6.25), dpi=72)
# ax = fig.add_subplot(111)

# for i in range(0, t.size, di):
#     print(i // di, '/', t.size // di)
#     make_plot(i)