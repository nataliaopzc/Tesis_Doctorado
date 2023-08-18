from netCDF4 import Dataset as nc #this line imports the package we just installed
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

file=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006.SPIN/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
file_sig=np.genfromtxt('/media/natalia/DATA/Documentos/TesisI/SPIN/Spin-up_Holoceno/biogem_force_flux_sed_det_SUR.dat') # this line defines the file path of the file we are trying to read
file_sig=np.flip(np.log(file_sig),axis=0)

lon=file.variables['lon'][:];lon=np.array(lon)
lat=file.variables['lat'][:];lat=np.array(lat)
#lon_lat=np.transpose(np.array([lon, lat]))
#np.savetxt('/media/natalia/DATA/Documentos/TesisI/SPIN/lon_lat.dat',lon_lat)

Sol_Iron=file.variables['misc_sur_fFe'][:] # ":" takes all the data dimension from the file
Sol_Iron=np.log(Sol_Iron)

Sol_Iron_median=np.mean(Sol_Iron,axis=0) # Median in 3D dimention
Sol_Iron_median=np.log(Sol_Iron_median)
#print( Sol_Iron_median[0,:])

Sol_Iron_perc=file.variables['misc_sur_Fe_sol'][:]
Sol_Iron_perc_median=np.mean(Sol_Iron_perc,axis=0)
Sol_Iron_perc_median=np.log(Sol_Iron_perc_median)

###########################################################
file2=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006LGM.SPIN/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
file_sig2=np.genfromtxt('/media/natalia/DATA/Documentos/TesisI/SPIN/Spin-up_LGM/biogem_force_flux_sed_det_SUR.dat') # this line defines the file path of the file we are trying to read
file_sig2=np.flip(np.log(file_sig2),axis=0)

Sol_IronLGM=file2.variables['misc_sur_fFe'][:] # ":" takes all the data dimension from the file
Sol_IronLGM=np.log(Sol_IronLGM)

Sol_IronLGM_median=np.mean(Sol_IronLGM,axis=0) # Median in 3D dimention
Sol_IronLGM_median=np.log(Sol_IronLGM_median)

Sol_IronLGM_perc=file2.variables['misc_sur_Fe_sol'][:]
Sol_IronLGM_perc_median=np.mean(Sol_IronLGM_perc,axis=0)
Sol_IronLGM_perc_median=np.log(Sol_IronLGM_perc_median)

########################################################

#m = Basemap(projection='mill',lon_0=-80,lat_0=0,resolution='l')
m = Basemap(projection='mill',lon_0=-80,lat_0=0,resolution='l',
            llcrnrlat = min(lat),
            llcrnrlon = min(lon),
            urcrnrlat = max(lat),
            urcrnrlon = max(lon))

#m.drawcoastlines()
lons, lats = np.meshgrid(lon, lat) # get lat/lons of ny by nx evenly space grid.
x, y = m(lons, lats) # compute map proj coordinates.
#print(Sol_Iron_median.shape[0])

plt.figure()
cmap = plt.get_cmap('nipy_spectral')
plt.subplot(321)

m.drawcoastlines()
cs5 = m.contourf(x,y,file_sig,500,vmin=15, vmax=32,cmap=cmap) 
cbar5=plt.colorbar(cs5,orientation="horizontal")
cbar5.set_label('%', rotation=0)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Dust flux')

#plt.subplot(212)
#cs6=plt.pcolor(x,y,file_sig,cmap=cmap,vmin=15, vmax=32) 
#cbar6=plt.colorbar(cs6,orientation="horizontal")
#cbar6.set_label('%', rotation=0)
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')
#plt.title('Aeolian iron solubility')

plt.subplot(322)
m.drawcoastlines()
cs5 = m.contourf(x,y,file_sig2,500,vmin=15, vmax=32,cmap=cmap) 
cbar5=plt.colorbar(cs5,orientation="horizontal")
cbar5.set_label('%', rotation=0)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Dust flux')

#plt.subplot(212)
#cs6=plt.pcolor(x,y,file_sig2,cmap=cmap,vmin=15.78, vmax=32) 
#cbar6=plt.colorbar(cs6,orientation="horizontal")
#cbar6.set_label('%', rotation=0)
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')
#plt.title('Aeolian iron solubility')


##################################################

plt.subplot(323)
cs2 = m.contourf(x,y,Sol_Iron_perc_median,500,cmap=cmap) 
cbar2=plt.colorbar(cs2,orientation="horizontal")
cbar2.set_label('%', rotation=0)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Aeolian iron solubility')

#plt.figure()
#plt.subplot(211)
#cs3=plt.pcolor(x,y,Sol_Iron_perc_median,cmap=cmap) 
#cbar2=plt.colorbar(cs3,orientation="horizontal")
#cbar2.set_label('%', rotation=0)
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')
#plt.title('Aeolian iron solubility')

plt.subplot(324)
csLGM2 = m.contourf(x,y,Sol_IronLGM_perc_median,500,cmap=cmap) 
cbarLGM2=plt.colorbar(csLGM2,orientation="horizontal")
cbarLGM2.set_label('%', rotation=0)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Aeolian iron solubility')

#csLGM3=plt.pcolor(x,y,Sol_IronLGM_perc_median,cmap=cmap) 
#cbarLGM2=plt.colorbar(csLGM3,orientation="horizontal")
#cbarLGM2.set_label('%', rotation=0)
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')
#plt.title('Aeolian iron solubility')

########################################################
plt.subplot(325)
cs = m.contourf(x,y,Sol_Iron_median,500,cmap=cmap) 
cbar=plt.colorbar(cs,orientation="horizontal")
cbar.set_label('mol Fe yr-1', rotation=0)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Solulablized aeolian iron flux\n to surface grid points')

#plt.subplot(212)
#cs4=plt.pcolor(x,y,Sol_Iron_median,cmap=cmap) 
#cbar=plt.colorbar(cs4,orientation="horizontal")
#cbar.set_label('mol Fe yr-1', rotation=0)
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')

plt.subplot(326)
csLGM = m.contourf(x,y,Sol_IronLGM_median,500,cmap=cmap) 
cbarLGM=plt.colorbar(csLGM,orientation="horizontal")
cbarLGM.set_label('mol Fe yr-1', rotation=0)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Solulablized aeolian iron flux\n to surface grid points')

#csLGM4=plt.pcolor(x,y,Sol_IronLGM_median,cmap=cmap) 
#cbarLGM=plt.colorbar(csLGM4,orientation="horizontal")
#cbarLGM.set_label('mol Fe yr-1', rotation=0)
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')

plt.show()