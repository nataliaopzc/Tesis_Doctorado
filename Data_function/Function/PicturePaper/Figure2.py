# %%
from netCDF4 import Dataset as nc #this line imports the package we just installed
import numpy as np
import matplotlib.pyplot as plt
import numpy.matlib as matlib
from mpl_toolkits.basemap import Basemap
from scipy.io import loadmat

Area=loadmat('/home/natalia/Documentos/Tesis/Functions/Otros/areat_as_grid.mat')
Area=Area['area']

file1=nc('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/Otros/Previews simulartions/worjh2.PO4FeH_Dust/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
lon=file1.variables['lon'][:]
lat=file1.variables['lat'][:]
Sol_feH=np.flip(np.genfromtxt('/home/natalia/cgenie.muffin/genie-biogem/data/input/worjh2.det_Fe_sol.Mahowald.dat'),axis=0)
Sol_feLGM=np.flip(np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/worjh2.det_Fe_sol.Mahowald_LGM.dat'),axis=0)
###############################################################################
m = Basemap(projection='mill',lon_0=-80,lat_0=0,resolution='l',
            llcrnrlat = min(lat),
            llcrnrlon = min(lon),
            urcrnrlat = max(lat),
            urcrnrlon = max(lon))

lons, lats = np.meshgrid(lon, lat) # get lat/lons of ny by nx evenly space grid.
x, y = m(lons, lats) # compute map proj coordinates.

fig = plt.figure(num=None, figsize=(10, 5.8), dpi=150, facecolor='w', edgecolor='k')


ax3 = fig.add_subplot(222)
chartBox = ax3.get_position()
ax3.set_position([chartBox.x0-0.01, chartBox.y0+0.04,
                 chartBox.width,
                 chartBox.height])
#figure=plt.figure(num=None, figsize=(8, 4.5), dpi=150, facecolor='w', edgecolor='k')
#figure.add_axes([0.07, 0.1, 0.83, 0.8])
cmap = plt.get_cmap('nipy_spectral')
m.drawcoastlines()
m.drawparallels([-60,-30,0,30,60],labels=[True,False],linewidth=0,fontsize=8) #fontweight='bold'
m.drawmeridians(np.arange(10.,351.,60.),labels=[True,True,False,True],linewidth=0,fontsize=8)
Exp_H1 = ax3.contourf(x,y,Sol_feH,700,cmap=cmap) #vmin=0.04, vmax=4.5
cbaxes = fig.add_axes([0.9, 0.13, 0.03, 0.78]) 
cb = plt.colorbar(Exp_H1, cax = cbaxes, extend='both',format='%.1f')
plt.title('b)',x=-12.8, y=1.02)
cb.set_label('Iron solubility [%]', rotation=90,fontsize=9,fontweight='bold')
# ax3.set_xlabel('Longitude',color='black',fontsize=8, fontweight='bold' )
# ax3.set_ylabel('Latitude',color='black',fontsize=8, fontweight='bold' )
#plt.savefig('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Figure2_Solubility_H.png')

ax4 = fig.add_subplot(224)
chartBox = ax4.get_position()
ax4.set_position([chartBox.x0-0.01, chartBox.y0,
                 chartBox.width,
                 chartBox.height])
#figure=plt.figure(num=None, figsize=(8, 4.5), dpi=150, facecolor='w', edgecolor='k')
#figure.add_axes([0.07, 0.1, 0.83, 0.8])
m.drawcoastlines()
m.drawparallels([-60,-30,0,30,60],labels=[True,False],linewidth=0,fontsize=8) #fontweight='bold'
m.drawmeridians(np.arange(10.,351.,60.),labels=[True,True,False,True],linewidth=0,fontsize=8)
Exp_H1 = ax4.contourf(x,y,Sol_feLGM,700,vmax=np.max(Sol_feH.flatten()),cmap=cmap) #vmin=0.04, vmax=4.5
plt.title('d)',x=-0.06, y=1.05)
#cb = plt.colorbar(Exp_H1, cax = cbaxes)
#Exp_H1.set_label('%', rotation=90,fontsize=8)
# ax4.set_xlabel('Longitude',color='black',fontsize=8, fontweight='bold' )
# ax4.set_ylabel('Latitude',color='black',fontsize=8, fontweight='bold' )

#plt.savefig('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Figure2_Solubility_LGM.png')

from matplotlib import ticker, cm
from mpl_toolkits.axes_grid1 import make_axes_locatable

DustH=np.loadtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/Otros/Previews_simulations/worjh2.FeMahowald2006H_Dust_SPIN/biogem_force_flux_sed_det_SUR.dat',dtype=str) # this line defines the file path of the file we are trying to read
DustLGM=np.loadtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/Otros/Previews_simulations/worjh2.FeMahowald2006_LGM_SPIN/biogem_force_flux_sed_det_SUR.dat',dtype=str) # this line defines the file path of the file we are trying to read

# for i in range(36):
#     for j in range(36):
#         DustH[i,j]=float(DustH[i,j].replace(',','.'))
#         DustLGM[i,j]=float(DustH[i,j].replace(',','.'))

  # Si fuera en moles:      
# DustH=np.log10(np.array(DustH, dtype=np.float))  
# DustLGM=np.log10(np.array(DustLGM, dtype=np.float))  
DustH1=np.array(DustH, dtype=np.float)*(56/1000)
DustH=np.log10(np.array(DustH, dtype=np.float)*(56/(1000*60*60*24*365))/Area)  # 1 mol Fe ->56 gr (/1000 -> kg)
DustLGM=np.log10(np.array(DustLGM, dtype=np.float)*(56/(1000*60*60*24*365))/Area)  

ax1 = fig.add_subplot(223)
chartBox = ax1.get_position()
ax1.set_position([chartBox.x0-0.088, chartBox.y0,
                 chartBox.width,
                 chartBox.height])

cmap = plt.get_cmap('jet')
m.drawcoastlines()
m.drawparallels([-60,-30,0,30,60],labels=[True,False],linewidth=0,fontsize=8) #fontweight='bold'
m.drawmeridians(np.arange(10.,351.,60.),labels=[True,True,False,True],linewidth=0,fontsize=8)
cs = ax1.contourf(x,y,np.flip(DustLGM,axis=0),500,vmin=np.min(DustH.flatten()),cmap=cmap)
plt.title('c)',x=-0.07, y=1.05) 
# Adding the colorbar
cbaxes = fig.add_axes([0.4, 0.13, 0.03, 0.78]) 
 
# position for the colorbar
cb = plt.colorbar(cs, cax = cbaxes,format='%.1f')
cb.set_label('Dust deposition [log10, kg m' r'$\bf ^{-2}$' 's' r'$\bf ^{-1}$' ']', rotation=90,fontsize=9,fontweight='bold')
# ax1.set_xlabel('Longitude',color='black',fontsize=8, fontweight='bold')
# ax1.set_ylabel('Latitude',color='black',fontsize=8, fontweight='bold')

#plt.savefig('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Figure2_Dust_LGM.png')

ax2 = fig.add_subplot(221)
chartBox = ax2.get_position()
ax2.set_position([chartBox.x0-0.088, chartBox.y0+0.04,
                 chartBox.width,
                 chartBox.height])

m.drawcoastlines()
m.drawparallels([-60,-30,0,30,60],labels=[True,False],linewidth=0,fontsize=8) #fontweight='bold'
m.drawmeridians(np.arange(10.,351.,60.),labels=[True,True,False,True],linewidth=0,fontsize=8)
cs= ax2.contourf(x,y,np.flip(DustH,axis=0),500,vmax=np.max(DustLGM.flatten()),cmap=cmap)
plt.title('a)',x=-0.07, y=1.04) 
#cbar2=plt.colorbar(cs,orientation="vertical",fraction=0.026)
# ax2.set_xlabel('Longitude',color='black',fontsize=8, fontweight='bold' )
# ax2.set_ylabel('Latitude',color='black',fontsize=8, fontweight='bold')

#plt.savefig('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Figure2_Dust_H.png')

plt.savefig('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Figure2_Subplot.png')
# %%
