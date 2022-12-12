import numpy as np
import matplotlib.pyplot as plt

tweeD_nullen  = np.zeros((6,6))
tweeD_enen    = np.ones((6,6))
tweeD_random  = np.random.rand(6,6)

eenD_array  = np.arange(36)
tweeD_array = eenD_array.reshape(6,6)

x = np.arange(6)
y = np.arange(6)
xv, yv = np.meshgrid(x, y, indexing='xy')

x = np.linspace(-1.0,1.0, 1000)
y = np.linspace(-1.0,1.0, 1000)
xv, yv = np.meshgrid(x,y)
hyperbool = (np.sin(4*np.pi * xv)**2 * yv**2)
xavgHyperbool = (np.sin(4*np.pi * xv)**2 * yv**2).mean(axis=0)
yavgHyperbool = (np.sin(4*np.pi * xv)**2 * yv**2).mean(axis=1)

plt.imshow(hyperbool,
           interpolation='none',
           cmap = 'seismic',
           extent = [x.min(),x.max(),y.min(),y.max()])

plt.plot(x,xavgHyperbool)
plt.plot(y,yavgHyperbool)
# plt.axes().set_aspect('equal')
plt.colorbar()
plt.clim(-1,1)
plt.show()