from netCDF4 import Dataset as nc #this line imports the package we just installed
import numpy as np

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

file2=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006LGM.SPIN/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
Sol_IronLGM=file2.variables['misc_sur_fFe'][:] # ":" takes all the data dimension from the file
Sol_IronLGM_median=np.mean(Sol_IronLGM,axis=0) # Median in 3D dimention

np.savetxt('/media/natalia/DATA/Documentos/TesisI/SPIN/Spin-up_LGM/biogem_force_flux_ocn_Fe_SUR_4.dat',Sol_IronLGM_median, fmt='%1.6e')
#exit()
lon=file2.variables['lon'][:]
lat=file2.variables['lat'][:]
print(lon,lat)
exit()

Sol_IronLGM_perc=file2.variables['misc_sur_Fe_sol'][:]
Sol_IronLGM_perc_median=np.mean(Sol_IronLGM_perc,axis=0)

file_sig2=np.genfromtxt('/media/natalia/DATA/Documentos/TesisI/SPIN/Spin-up_LGM/biogem_force_flux_sed_det_SUR.dat') # this line defines the file path of the file we are trying to read
file_sig2=np.flip(np.log(file_sig2),axis=0)

########################################################
########################################################

#m.drawcoastlines()
m = Basemap(projection='mill',lon_0=-80,lat_0=0,resolution='l',
            llcrnrlat = min(lat),
            llcrnrlon = min(lon),
            urcrnrlat = max(lat),
            urcrnrlon = max(lon))


lons, lats = np.meshgrid(lon, lat) # get lat/lons of ny by nx evenly space grid.
x, y = m(lons, lats) 

cmap = plt.get_cmap('nipy_spectral')
plt.figure()
plt.subplot(212)
csLGM = m.contourf(x,y,np.log(Sol_IronLGM_median),500,cmap=cmap) 
cbarLGM=plt.colorbar(csLGM,orientation="horizontal")
cbarLGM.set_label('mol Fe yr-1', rotation=0)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Solulablized aeolian iron flux\n to surface grid points')

plt.subplot(211)
csLGM2 = m.contourf(x,y,Sol_IronLGM_perc_median,500,cmap=cmap) 
cbarLGM2=plt.colorbar(csLGM2,orientation="horizontal")
cbarLGM2.set_label('%', rotation=0)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Aeolian iron solubility')

plt.figure()
plt.subplot(211)
csLGM3=plt.pcolor(x,y,Sol_IronLGM_perc_median,cmap=cmap) 
cbarLGM2=plt.colorbar(csLGM3,orientation="horizontal")
cbarLGM2.set_label('%', rotation=0)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Aeolian iron solubility')

plt.subplot(212)
csLGM4=plt.pcolor(x,y,Sol_IronLGM_median,cmap=cmap) 
cbarLGM=plt.colorbar(csLGM4,orientation="horizontal")
cbarLGM.set_label('mol Fe yr-1', rotation=0)
plt.xlabel('Longitude')
plt.ylabel('Latitude')

#############################################
plt.figure()

plt.subplot(211)
m.drawcoastlines()
cs5 = m.contourf(x,y,file_sig2,500,vmin=15, vmax=32,cmap=cmap) 
cbar5=plt.colorbar(cs5,orientation="horizontal")
cbar5.set_label('%', rotation=0)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Aeolian iron solubility')

plt.subplot(212)
cs6=plt.pcolor(x,y,file_sig2,cmap=cmap,vmin=15.78, vmax=32) 
cbar6=plt.colorbar(cs6,orientation="horizontal")
cbar6.set_label('%', rotation=0)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Aeolian iron solubility')

plt.show()