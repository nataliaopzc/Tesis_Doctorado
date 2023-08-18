import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy.matlib as matlib
import scipy.io as sio

mat = sio.loadmat('lon_lat.mat')
lonlat_edges=mat['lonlat_edges'];
lonlat=mat['lonlat'];
lon=lonlat_edges[:,0]-180;
#print(len(lon))
m = Basemap(projection='mill')

#lons, lats = np.meshgrid(lon, lat) # get lat/lons of ny by nx evenly space grid.
#x, y = m(lons, lats) # compute map proj coordinates.
#print(Sol_Iron_median.shape[0])

for i in range(37):
	#m.drawcoastlines()
	plt.plot(lon,matlib.repmat(lonlat_edges[i,1],37,1),'-k')
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')


#############################################
# SP
for i in range(7):
    for j in range(5,18):
        plt.text(lonlat[j,0],lonlat[i,1],'x')
# SA
for i in range(7):
    for j in range(19,35):
        plt.text(lonlat[j,0],lonlat[i,1],'x')

for i in range(0,7):
    for j in range(0,4):
        plt.text(lonlat[j,0],lonlat[i,1],'x')
# NP
for i in range(28,35):
    for j in range(2,14):
        plt.text(lonlat[j,0],lonlat[i,1],'x')
# NA
for i in range(28,35):
    for j in range(19,24):
        plt.text(lonlat[j,0],lonlat[i,1],'x')
#CP
for i in range(16,19):
    for j in range(9,17):
        plt.text(lonlat[j,0],lonlat[i,1],'x')

plt.show()
# Regiones

# SA
#for i in range(0,8): #del 29 al 36
#    plt.plot(lon[11:33],matlib.repmat(lonlat_edges[i,1],23, 1),'-r')
A=matlib.repmat(lonlat_edges[i,1],23, 1)
print(A)