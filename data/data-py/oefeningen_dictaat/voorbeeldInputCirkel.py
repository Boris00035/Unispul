import numpy as np
import matplotlib.pyplot as  plt

th = np.linspace(-0,2*np.pi,num=100)
r  = np.linspace(1E-5,1.0)

rv, thv = np.meshgrid(r,th)

fr = np.sin(rv)/rv**2 - np.cos(rv)/rv
fth = np.cos(4*thv)
img = fr*fth

plt.figure("Figuur 1")
ax = plt.axes()
plt.imshow(img,
           extent = [r.min(),r.max(),th.min(),th.max()])
ax.set_aspect(1/(2*np.pi))
plt.colorbar()
plt.xlabel(r"$r$")
plt.ylabel(r"$\theta$")
plt.show()

xv = rv * np.cos(thv)
yv = rv * np.sin(thv)

plt.figure("Figuur 2")
ax1 = plt.axes()
plt.pcolormesh(xv,yv,img)
plt.colorbar()
ax1.set_aspect('equal')
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.show()

