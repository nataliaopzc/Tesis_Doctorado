# %%
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset as nc #this line imports the package we just installed
from mpl_toolkits.basemap import Basemap

MODEL=['Albani','Lambert','Takemura','Ohgaito','MIROC-ESM','MRI-CGCM3']
TIME=['H','LGM']
REGION=['NA', 'NP','CP', 'SP','SA']

dust_H=np.zeros((36,36,6))
dust_LGM=np.zeros((36,36,6))
SOl_LGM=np.zeros((36,36,6))
SOl_H=np.zeros((36,36,6))
for i, ii in zip(MODEL,range(7)):
        SOl_H[:,:,ii]=np.genfromtxt('../../../cgenie/Solubility/Global/'+i+'/worjh2.det_Fe_Sol_calculated.'+i+'_H_x1.dat',comments="%")
        SOl_LGM[:,:,ii]=np.genfromtxt('../../../cgenie/Solubility/Global/'+i+'/worjh2.det_Fe_Sol_calculated.'+i+'_LGM_x1.dat',comments="%")
        dust_H[:,:,ii]=np.genfromtxt('../../../../Tesis_Magister/Flujos_de_polvo/Globales_Kg/'+i+'/'+i+'.nc_annualflux_kgperm2pers.36x36_level1.dat',comments="%")
        dust_LGM[:,:,ii]=np.genfromtxt('../../../../Tesis_Magister/Flujos_de_polvo/Globales_Kg/'+i+'/'+i+'.nc_annualflux_kgperm2pers.36x36_level10.dat',comments="%")

SOL_H=np.median(SOl_H,axis=2)
SOL_LGM=np.median(SOl_LGM,axis=2)
Dust_H=np.log10(np.median(dust_H,axis=2))
Dust_LGM=np.log10(np.median(dust_LGM,axis=2))

#%% 
for j in REGION:
        if j=='NA':
                XNA_H=np.median(SOL_H[1:8,20:25])
                XNA_LGM=np.median(SOL_LGM[1:8,20:25])
        if j=='NP':
                XNP_H=np.median(SOL_H[1:8,3:15])
                XNP_LGM=np.median(SOL_LGM[1:8,3:15])
        if j=='CP':
                XCP_H=np.median(SOL_H[17:20,10:18])
                XCP_LGM=np.median(SOL_LGM[17:20,10:18])
        if j=='SP':
                XSP_H=np.median(SOL_H[29:36,6:19])
                XSP_LGM=np.median(SOL_LGM[29:36,6:19])
        if j=='SA':
                XSA1=np.median(SOL_H[29:36,20:36])
                XSA2=np.median(SOL_H[29:36,1:5]); XSA_H=np.mean([XSA1,XSA2])
                XSA1_LGM=np.median(SOL_LGM[29:36,20:36])
                XSA2_LGM=np.median(SOL_LGM[29:36,1:5]); XSA_LGM=np.mean([XSA1_LGM,XSA2_LGM])
# # %%
# SOL_H=np.zeros(6)
# SOL_LGM=np.zeros(6)
# XNA_H=np.zeros(6)
# XNA_LGM=np.zeros(6)
# XNP_H=np.zeros(6)
# XNP_LGM=np.zeros(6)
# XCP_H=np.zeros(6)
# XCP_LGM=np.zeros(6)
# XSP_H=np.zeros(6)
# XSP_LGM=np.zeros(6)
# XSA_H=np.zeros(6)
# XSA_LGM=np.zeros(6)
# for i in range(6):
#         SOL_H[i]=np.median(SOl_H[:,:,i])
#         SOL_LGM[i]=np.median(SOl_LGM[:,:,i])
#         for j in REGION:
#                 if j=='NA':
#                         XNA_H[i]=np.median(SOl_H[1:8,20:25,i])
#                         XNA_LGM[i]=np.median(SOl_LGM[1:8,20:25,i])
#                 if j=='NP':
#                         XNP_H[i]=np.median(SOl_H[1:8,3:15,i])
#                         XNP_LGM[i]=np.median(SOl_LGM[1:8,3:15,i])
#                 if j=='CP':
#                         XCP_H[i]=np.median(SOl_H[17:20,10:18,i])
#                         XCP_LGM[i]=np.median(SOl_LGM[17:20,10:18,i])
#                 if j=='SP':
#                         XSP_H[i]=np.median(SOl_H[29:36,6:19,i])
#                         XSP_LGM[i]=np.median(SOl_LGM[29:36,6:19,i])
#                 if j=='SA':
#                         XSA1=np.median(SOl_H[29:36,20:36,i])
#                         XSA2=np.median(SOl_H[29:36,1:5,i]); XSA_H[i]=np.mean([XSA1,XSA2])
#                         XSA1_LGM=np.median(SOl_LGM[29:36,20:36,i])
#                         XSA2_LGM=np.median(SOl_LGM[29:36,1:5,i]); XSA_LGM[i]=np.mean([XSA1_LGM,XSA2_LGM])
# %% Imagen 7
file1=nc('../../../cgenie/cgenie_output/Otros/Previews simulartions/worjh2.PO4FeH_Dust/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
lon=file1.variables['lon'][:]
lat=file1.variables['lat'][:]

m = Basemap(projection='mill',lon_0=-80,lat_0=0,resolution='l',
            llcrnrlat = min(lat),
            llcrnrlon = min(lon),
            urcrnrlat = max(lat),
            urcrnrlon = max(lon))

lons, lats = np.meshgrid(lon, lat) # get lat/lons of ny by nx evenly space grid.
x, y = m(lons, lats) # compute map proj coordinates.
cmap = plt.get_cmap('nipy_spectral')

fig = plt.figure(num=None, figsize=(10, 5.8), dpi=150, facecolor='w', edgecolor='k')

ax1=plt.subplot(2,2,1)
chartBox = ax1.get_position()
ax1.set_position([chartBox.x0-0.088, chartBox.y0+0.04,
                 chartBox.width,
                 chartBox.height])
m.drawcoastlines()
m.drawparallels([-60,-30,0,30,60],labels=[True,False],linewidth=0.01,fontsize=8) #fontweight='bold'
m.drawmeridians(np.arange(10.,351.,60.),labels=[True,True,False,True],linewidth=0.01,fontsize=8)
DustH=plt.contourf(x,y,np.flip(Dust_H,axis=0),700,vmax=np.max(Dust_LGM.flatten()),cmap=cmap)
plt.title('a)',x=-0.07, y=1.04) 

ax2 = fig.add_subplot(222)
chartBox = ax2.get_position()
ax2.set_position([chartBox.x0-0.01, chartBox.y0+0.04,
                 chartBox.width,
                 chartBox.height])
m.drawcoastlines()
m.drawparallels([-60,-30,0,30,60],labels=[True,False],linewidth=0.01,fontsize=8) #fontweight='bold'
m.drawmeridians(np.arange(10.,351.,60.),labels=[True,True,False,True],linewidth=0.01,fontsize=8)
SOLH=plt.contourf(x,y,np.flip(SOL_H,axis=0),700,cmap=cmap)
plt.title('b)',x=-0.06, y=1.04)

ax3 = fig.add_subplot(223)
chartBox = ax3.get_position()
ax3.set_position([chartBox.x0-0.088, chartBox.y0,
                 chartBox.width,
                 chartBox.height])
m.drawcoastlines()
m.drawparallels([-60,-30,0,30,60],labels=[True,False],linewidth=0.01,fontsize=8) #fontweight='bold'
m.drawmeridians(np.arange(10.,351.,60.),labels=[True,True,False,True],linewidth=0.01,fontsize=8)
DustLGM=plt.contourf(x,y,np.flip(Dust_LGM,axis=0),700,vmin=np.min(Dust_H.flatten()),cmap=cmap)
plt.title('c)',x=-0.07, y=1.05)
cbaxes = fig.add_axes([0.4, 0.13, 0.03, 0.78]) 
bar=plt.colorbar(DustLGM,cax = cbaxes,format='%.1f')
bar.set_label('Dust deposition [log10, kg m' r'$\bf ^{-2}$' 's' r'$\bf ^{-1}$' ']', rotation=90,fontsize=9,fontweight='bold')

ax4 = fig.add_subplot(224)
chartBox = ax4.get_position()
ax4.set_position([chartBox.x0-0.01, chartBox.y0,
                 chartBox.width,
                 chartBox.height])
m.drawcoastlines()
m.drawparallels([-60,-30,0,30,60],labels=[True,False],linewidth=0.01,fontsize=8) #fontweight='bold'
m.drawmeridians(np.arange(10.,351.,60.),labels=[True,True,False,True],linewidth=0.01,fontsize=8)
SOLLGM=plt.contourf(x,y,np.flip(SOL_LGM,axis=0),700,vmax=np.max(SOL_H.flatten()),cmap=cmap)
plt.title('d)',x=-0.06, y=1.05)
cbaxes = fig.add_axes([0.9, 0.13, 0.03, 0.78])  
bar=plt.colorbar(SOLH,cax = cbaxes,format='%.1f')
bar.set_label('Iron solubility [%]', rotation=90,fontsize=9,fontweight='bold')

plt.savefig('./Figure7.pdf')

# %%
