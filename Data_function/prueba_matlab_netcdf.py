from netCDF4 import Dataset as nc #this line imports the package we just installed
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

file1=nc('/media/natalia/DATA/Documentos/TesisI/cgenie/cgenie_output/worjh2.PO4FeLambert_LGM_Sol_calculated_Dust_CP_x0.6666/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
lon=file1.variables['lon'][:]
print(lon)
lat=file1.variables['lat'][:]

Exp1=file1.variables['bio_export_POC'][:] # ":" takes all the data dimension from the file
# #Exp1_median=np.median(Exp1,axis=0) # Median in 3D dimention

m = Basemap(projection='mill',lon_0=-80,lat_0=0,resolution='l',
            llcrnrlat = min(lat),
             llcrnrlon = min(lon),
             urcrnrlat = max(lat),
             urcrnrlon = max(lon))
m.drawcoastlines()
lons, lats = np.meshgrid(lon, lat) # get lat/lons of ny by nx evenly space grid.
x, y = m(lons, lats) # compute map proj coordinates.
# #print(Sol_Iron_median.shape[0])

# plt.figure()
# cmap = plt.get_cmap('nipy_spectral')

# plt.subplot(221)
# m.drawcoastlines()
# Exp_H1 = m.contourf(x,y,Exp1,500,vmin=-0.9, vmax=1.2,cmap=cmap) 
Exp_H1=m.contourf(x,y,Exp1,500) 
# #Exp_H1=plt.colorbar(Exp1,orientation="vertical")
# Exp_H1.set_label('mol m-2 yr-1', rotation=90)
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.title('Holocene'),
plt.show()