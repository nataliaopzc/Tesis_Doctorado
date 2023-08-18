from netCDF4 import Dataset as nc #this line imports the package we just installed
import numpy as np
import matplotlib.pyplot as plt
import numpy.matlib as matlib
from mpl_toolkits.basemap import Basemap

file1=nc('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/Previews simulartions/worjh2.PO4FeH_Dust/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
lon=file1.variables['lon'][:]
lat=file1.variables['lat'][:]
Sol_feH=np.flip(np.genfromtxt('/home/natalia/cgenie.muffin/genie-biogem/data/input/worjh2.det_Fe_sol.Mahowald.dat'),axis=0)
Sol_feLGM=np.flip(np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/worjh2.det_Fe_sol.Mahowald_LGM.dat'),axis=0)

print(np.min(Sol_feH),np.max(Sol_feH))
print(np.min(Sol_feLGM),np.max(Sol_feLGM))

m = Basemap(projection='mill',lon_0=-80,lat_0=0,resolution='l',
            llcrnrlat = min(lat),
            llcrnrlon = min(lon),
            urcrnrlat = max(lat),
            urcrnrlon = max(lon))

#m.drawcoastlines()
lons, lats = np.meshgrid(lon, lat) # get lat/lons of ny by nx evenly space grid.
x, y = m(lons, lats) # compute map proj coordinates.
#print(Sol_Iron_median.shape[0])

plt.figure(num=None, figsize=(4,4.5), dpi=100, facecolor='w', edgecolor='k')
cmap = plt.get_cmap('nipy_spectral')

plt.subplot(211)
m.drawcoastlines()
Exp_H1 = m.contourf(x,y,Sol_feH,500,cmap=cmap) #vmin=0.04, vmax=4.5
Exp_H1=plt.colorbar(Exp_H1,orientation="vertical")
Exp_H1.set_label('%', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Holocene')


plt.subplot(212)
m.drawcoastlines()
Exp_H1 = m.contourf(x,y,Sol_feLGM,500,vmax=2.94,cmap=cmap) #vmin=0.04, vmax=4.5
Exp_H1=plt.colorbar(Exp_H1,orientation="vertical")
Exp_H1.set_label('%', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('LGM')

plt.savefig('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/MahowaldSolubility_Mahowald.pdf')

plt.show()