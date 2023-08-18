from netCDF4 import Dataset as nc #this line imports the package we just installed
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

file1=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006_DUST/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
lon=file1.variables['lon'][:]
lat=file1.variables['lat'][:]

file2=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
file3=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006TDFe/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read

Exp1=file1.variables['bio_export_POC'][:] # ":" takes all the data dimension from the file
Exp2=file2.variables['bio_export_POC'][:] # ":" takes all the data dimension from the file
Exp3=file3.variables['bio_export_POC'][:] # ":" takes all the data dimension from the file

Exp1_median=np.median(Exp1,axis=0) # Median in 3D dimention
Exp2_median=np.median(Exp2,axis=0) # Median in 3D dimention
Exp3_median=np.median(Exp3,axis=0) # Median in 3D dimention

Exp_SFe=(Exp2_median-Exp1_median)
Exp_STDFe=(Exp3_median-Exp1_median)
###########################################################
file4=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006LGM_DUST/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
file5=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006LGM/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
file6=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006TDFe_LGM/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to rea

ExpLGM4=file4.variables['bio_export_POC'][:] # ":" takes all the data dimension from the file
ExpLGM5=file5.variables['bio_export_POC'][:]
ExpLGM6=file6.variables['bio_export_POC'][:]

ExpLGM4_median=np.median(ExpLGM4,axis=0) # Median in 3D dimention
ExpLGM5_median=np.median(ExpLGM5,axis=0) # Median in 3D dimention
ExpLGM6_median=np.median(ExpLGM6,axis=0) # Median in 3D dimention


ExpLGM_SFe=(ExpLGM5_median-ExpLGM4_median)
ExpLGM_STDFe=(ExpLGM6_median-ExpLGM4_median)

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

plt.subplot(221)
m.drawcoastlines()
Exp_H1 = m.contourf(x,y,Exp_SFe,500,vmin=-0.9, vmax=1.2,cmap=cmap) 
Exp_H1=plt.colorbar(Exp_H1,orientation="vertical")
Exp_H1.set_label('mol m-2 yr-1', rotation=90)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Holocene')

plt.subplot(222)
m.drawcoastlines()
ExpLGM_H1 = m.contourf(x,y,ExpLGM_SFe,500,vmin=-0.9, vmax=1.2,cmap=cmap) 
ExpLGM_H1=plt.colorbar(ExpLGM_H1,orientation="vertical")
ExpLGM_H1.set_label('mol m-2 yr-1', rotation=90)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('LGM')

plt.subplot(223)
m.drawcoastlines()
Exp_H2 = m.contourf(x,y,Exp_STDFe,500,vmin=-2.6, vmax=0,cmap=cmap) 
Exp_H2=plt.colorbar(Exp_H2,orientation="vertical")
Exp_H2.set_label('mol m-2 yr-1', rotation=90)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Holocene')

plt.subplot(224)
m.drawcoastlines()
ExpLGM_H2 = m.contourf(x,y,ExpLGM_STDFe,500,vmin=-2.6, vmax=0,map=cmap) 
ExpLGM_H2=plt.colorbar(ExpLGM_H2,orientation="vertical")
ExpLGM_H2.set_label('mol m-2 yr-1', rotation=90)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('LGM')

plt.suptitle("Difference Biological export POC",fontsize=14)
plt.show()
