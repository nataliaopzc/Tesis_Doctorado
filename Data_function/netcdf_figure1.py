from netCDF4 import Dataset as nc #this line imports the package we just installed
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

file=nc('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/Previews simulartions/worjh2.PO4Fe_Mahowald2006.SPIN/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
file_sig=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/Data_function/Spin-up_Holoceno/biogem_force_flux_sed_det_SUR.dat') # this line defines the file path of the file we are trying to read

file_sig=np.flip(np.log(file_sig),axis=0)

Sol_Iron=file.variables['misc_sur_fFe'][:] # ":" takes all the data dimension from the file
#Sol_Iron=np.log(Sol_Iron)

Sol_Iron_median=np.median(Sol_Iron,axis=0) # Median in 3D dimention
Sol_Iron_median=np.log(Sol_Iron_median)
#print( Sol_Iron_median[0,:])

Sol_Iron_perc=file.variables['misc_sur_Fe_sol'][:]
Sol_Iron_perc_median=np.mean(Sol_Iron_perc,axis=0)
Sol_Iron_perc_median=np.log(Sol_Iron_perc_median)

lon=file.variables['lon'][:]
lat=file.variables['lat'][:]
print(lon)
###########################################################
file2=nc('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/Previews simulartions/worjh2.PO4Fe_Mahowald2006LGM.SPIN/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
file_sig2=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/Data_function/Spin-up_LGM/biogem_force_flux_sed_det_SUR.dat') # this line defines the file path of the file we are trying to read
file_sig2=np.flip(np.log(file_sig2),axis=0)

Sol_IronLGM=file2.variables['misc_sur_fFe'][:] # ":" takes all the data dimension from the file

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

#plt.figure()
plt.figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
cmap = plt.get_cmap('nipy_spectral')
plt.subplot(321)

m.drawcoastlines()
cs5 = m.contourf(x,y,file_sig,500,vmin=15, vmax=32,cmap=cmap) 
cbar5=plt.colorbar(cs5,orientation="vertical")
cbar5.set_label('ln(kg m-2 s-1)', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
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
cbar5=plt.colorbar(cs5,orientation="vertical")
cbar5.set_label('ln(kg m-2 s-1)', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
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
m.drawcoastlines()
cs2 = m.contourf(x,y,Sol_Iron_perc_median,500,vmin=-3.1, vmax=1.54,cmap=cmap) 
cbar2=plt.colorbar(cs2,orientation="vertical")
cbar2.set_label('ln(%)', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
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
m.drawcoastlines()
csLGM2 = m.contourf(x,y,Sol_IronLGM_perc_median,500,vmin=-3.1, vmax=1.54,cmap=cmap) 
cbarLGM2=plt.colorbar(csLGM2,orientation="vertical")
cbarLGM2.set_label('ln(%)', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Aeolian iron solubility')

#csLGM3=plt.pcolor(x,y,Sol_IronLGM_perc_median,cmap=cmap) 
#cbarLGM2=plt.colorbar(csLGM3,orientation="horizontal")
#cbarLGM2.set_label('%', rotation=0)
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')
#plt.title('Aeolian iron solubility')

########################################################
plt.subplot(325)
m.drawcoastlines()
cs = m.contourf(x,y,Sol_Iron_median,500,vmin=12.04, vmax=18,cmap=cmap) 
cbar=plt.colorbar(cs,orientation="vertical")
cbar.set_label('Ln(mol Fe yr-1)', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Solulablized aeolian iron flux\n to surface grid points')

#plt.subplot(212)
#cs4=plt.pcolor(x,y,Sol_Iron_median,cmap=cmap) 
#cbar=plt.colorbar(cs4,orientation="horizontal")
#cbar.set_label('mol Fe yr-1', rotation=0)
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')

plt.subplot(326)
m.drawcoastlines()
csLGM = m.contourf(x,y,Sol_IronLGM_median,500,vmin=12.04, vmax=18,cmap=cmap) 
cbarLGM=plt.colorbar(csLGM,orientation="vertical")
cbarLGM.set_label('Ln(mol Fe yr-1)', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Solulablized aeolian iron flux\n to surface grid points')

#csLGM4=plt.pcolor(x,y,Sol_IronLGM_median,cmap=cmap) 
#cbarLGM=plt.colorbar(csLGM4,orientation="horizontal")
#cbarLGM.set_label('mol Fe yr-1', rotation=0)
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')
plt.subplots_adjust(hspace=0.3)
plt.suptitle("Holocene/LGM",fontsize=14,weight='bold')

plt.savefig('/media/natalia/DATA/Documentos/TesisI/Presentación12-08/figuras/figure1.pdf')
plt.show()