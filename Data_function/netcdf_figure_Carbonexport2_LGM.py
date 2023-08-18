from netCDF4 import Dataset as nc #this line imports the package we just installed
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

file1=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006LGM_DUST/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
lon=file1.variables['lon'][:]
lat=file1.variables['lat'][:]

file1_ALT=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006LGM_DUST_ALT/biogem/fields_biogem_2d.nc')
file1_OLD=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006LGM_DUST_OLD/biogem/fields_biogem_2d.nc')

file2=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006LGM_ALT/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
file3=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006LGM_OLD/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
file4=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006LGM_FeFe2LFeL/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read

Exp1=file1.variables['bio_export_POC'][:] # ":" takes all the data dimension from the file
Exp1_ALT=file1_ALT.variables['bio_export_POC'][:] # ":" takes all the data dimension from the file
Exp1_OLD=file1_OLD.variables['bio_export_POC'][:] # ":" takes all the data dimension from the file
Exp2=file2.variables['bio_export_POC'][:] # ":" takes all the data dimension from the file
Exp3=file3.variables['bio_export_POC'][:] # ":" takes all the data dimension from the file
Exp4=file4.variables['bio_export_POC'][:] # ":" takes all the data dimension from the file

Exp1_median=np.median(Exp1,axis=0) # Median in 3D dimention
Exp1_median_ALT=np.median(Exp1_ALT,axis=0) # Median in 3D dimention
Exp1_median_OLD=np.median(Exp1_OLD,axis=0) # Median in 3D dimention
Exp2_median=np.median(Exp2,axis=0) # Median in 3D dimention
Exp3_median=np.median(Exp3,axis=0) # Median in 3D dimention
Exp4_median=np.median(Exp4,axis=0) # Median in 3D dimention


## DIFERENCIAS

Exp_ALT=(Exp1_median-Exp2_median)
Exp_OLD=(Exp1_median-Exp3_median)
Exp_ALT2=(Exp1_median_ALT-Exp2_median)
Exp_OLD2=(Exp1_median_OLD-Exp3_median)

Exp_perc_ALT=(100*Exp_ALT)/Exp1_median
Exp_perc_OLD=(100*Exp_OLD)/Exp1_median
Exp_perc_ALT2=(100*Exp_ALT2)/Exp1_median_ALT
Exp_perc_OLD2=(100*Exp_OLD2)/Exp1_median_OLD
Exp_perc_ALT2_2=(100*Exp_ALT2)/Exp1_median_ALT
Exp_perc_OLD2_2=(100*Exp_OLD2)/Exp1_median_OLD

print(np.mean(Exp1_median_ALT),np.median(Exp1_median_ALT),'max(Exp1_median_ALT)=',np.max(Exp1_median_ALT),'min(Exp1_median_ALT)=',np.min(Exp1_median_ALT))
print(np.mean(Exp1_median_OLD),np.median(Exp1_median_OLD),'max(Exp1_median_OLD)=',np.max(Exp1_median_OLD),'min(Exp1_median_OLD)=',np.min(Exp1_median_OLD))
print(np.mean(Exp2_median),np.median(Exp2_median),'max(Exp2_median)=',np.max(Exp2_median),'min(Exp2_median)=',np.min(Exp2_median))
print(np.mean(Exp3_median),np.median(Exp3_median),'max(Exp3_median)=',np.max(Exp3_median),'min(Exp3_median)=',np.min(Exp3_median))
print(np.mean(Exp_ALT2),np.median(Exp_ALT2),'max(Exp_ALT2)=',np.max(Exp_ALT2),'min(Exp_ALT2)=',np.min(Exp_ALT2))
print(np.mean(Exp_OLD2),np.median(Exp_OLD2),'max(Exp_OLD2)=',np.max(Exp_OLD2),'min(Exp_OLD2)=',np.min(Exp_OLD2))
print(np.mean(Exp_perc_ALT),np.median(Exp_perc_ALT),'max(Exp_perc_ALT)=',np.max(Exp_perc_ALT),'min(Exp_perc_ALT)=',np.min(Exp_perc_ALT))
print(np.mean(Exp_perc_OLD),np.median(Exp_perc_OLD),'max(Exp_perc_OLD)=',np.max(Exp_perc_OLD),'min(Exp_perc_OLD)=',np.min(Exp_perc_OLD))
print(np.mean(Exp_perc_ALT2),np.median(Exp_perc_ALT2),'max(Exp_perc_ALT2)=',np.max(Exp_perc_ALT2),'min(Exp_perc_ALT2)=',np.min(Exp_perc_ALT2))
print(np.mean(Exp_perc_OLD2),np.median(Exp_perc_OLD2),'max(Exp_perc_OLD2)=',np.max(Exp_perc_OLD2),'min(Exp_perc_OLD2)=',np.min(Exp_perc_OLD2))
print('min',np.min(100*(Exp2_median-Exp1_median_OLD)/Exp2_median),'máx',np.max(100*(Exp2_median-Exp1_median_OLD)/Exp2_median))
print('min',np.min(100*(Exp3_median-Exp1_median_OLD)/Exp3_median),'máx',np.max(100*(Exp3_median-Exp1_median_OLD)/Exp3_median))
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

plt.figure(num=None, figsize=(10, 9.5), dpi=100, facecolor='w', edgecolor='k')
cmap = plt.get_cmap('nipy_spectral')

plt.subplot(421)
m.drawcoastlines()
Exp_H1 = m.contourf(x,y,Exp1_median_ALT,500,vmin=0.01, vmax=5.12,cmap=cmap) #vmin=0.04, vmax=4.5
Exp_H1=plt.colorbar(Exp_H1,orientation="vertical")
Exp_H1.set_label('mol m-2 yr-1', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Appyng Dust with "ALT" iron cycle')

plt.subplot(423)
m.drawcoastlines()
ExpLGM_H1 = m.contourf(x,y,Exp2_median,500,vmin=0.01, vmax=5.12,cmap=cmap) #vmin=0.04, vmax=4.5
ExpLGM_H1=plt.colorbar(ExpLGM_H1,orientation="vertical")
ExpLGM_H1.set_label('mol m-2 yr-1', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Appying dissolved Fe with "ALT" iron cycle')


plt.subplot(425)
m.drawcoastlines()
ExpLGM_H1 = m.contourf(x,y,Exp_ALT2,500,vmin=-1.634, vmax=1.232,cmap=cmap) #vmin=-0.69, vmax=0.35, 
ExpLGM_H1=plt.colorbar(ExpLGM_H1,orientation="vertical")
ExpLGM_H1.set_label('mol m-2 yr-1', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Dissolved iron/DUST difference')


plt.subplot(427)
m.drawcoastlines()
ExpLGM_H1 = m.contourf(x,y,Exp_perc_ALT2,500,vmin=-35.3, vmax=91.65,cmap=cmap) 
ExpLGM_H1=plt.colorbar(ExpLGM_H1,orientation="vertical")
ExpLGM_H1.set_label('%', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Percentage dissolved iron/DUST difference')

#plt.subplot(529)
#m.drawcoastlines()
#ExpLGM_H1 = m.contourf(x,y,100*(Exp2_median-Exp1_median_OLD)/Exp2_median,500,vmin=-35.3, vmax=91.65,cmap=cmap) 
#xpLGM_H1=plt.colorbar(ExpLGM_H1,orientation="vertical")
#ExpLGM_H1.set_label('%', rotation=90)
#plt.xlabel('Longitude',color='gray')
#plt.ylabel('Latitude',color='gray')
#plt.title('Dissolved iron/DUST difference percentage')

#plt.subplot(323)
#m.drawcoastlines()
#ExpLGM_H1 = m.contourf(x,y,(100*Exp3_median)/Exp2_median,500,cmap=cmap) 
#ExpLGM_H1=plt.colorbar(ExpLGM_H1,orientation="vertical")
#ExpLGM_H1.set_label('mol m-2 yr-1', rotation=90)
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')
#plt.title('Fe cycle "ALT"/"OLD" difference')

#a=plt.subplot(333)
#a.boxplot(np.reshape(Exp_ALT,(1296,1)))print(Exp_perc_ALT.shape,len(Exp_perc_ALT))

plt.subplot(422)
m.drawcoastlines()
ExpLGM_H1 = m.contourf(x,y,Exp1_median_OLD,500,vmin=0.01, vmax=5.12,cmap=cmap) #vmin=0.04, vmax=4.5
ExpLGM_H1=plt.colorbar(ExpLGM_H1,orientation="vertical")
ExpLGM_H1.set_label('mol m-2 yr-1', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Appyng Dust with "OLD" iron cycle')



plt.subplot(424)
m.drawcoastlines()
Exp_H2 = m.contourf(x,y,Exp3_median,500,vmin=0.01, vmax=5.12,cmap=cmap) #vmin=0.04, vmax=4.5, 
Exp_H2=plt.colorbar(Exp_H2,orientation="vertical")
Exp_H2.set_label('mol m-2 yr-1', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Appying dissolved Fe with "ALT" iron cycle')

plt.subplot(426)
m.drawcoastlines()
ExpLGM_H1 = m.contourf(x,y,Exp_OLD2,500,vmin=-1.634, vmax=1.232,cmap=cmap) #vmin=-0.69, vmax=0.35, 
ExpLGM_H1=plt.colorbar(ExpLGM_H1,orientation="vertical")
ExpLGM_H1.set_label('mol m-2 yr-1', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Dissolved iron/DUST difference')

plt.subplot(428)
m.drawcoastlines()
ExpLGM_H1 = m.contourf(x,y,Exp_perc_OLD2,500,vmin=-35.3, vmax=91.65,cmap=cmap) 
ExpLGM_H1=plt.colorbar(ExpLGM_H1,orientation="vertical")
ExpLGM_H1.set_label('%', rotation=90)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Percentage dissolved iron/DUST difference')

#plt.subplot(4,2,10)
#m.drawcoastlines()
#ExpLGM_H1 = m.contourf(x,y,100*(Exp3_median-Exp1_median_OLD)/Exp3_median,500,vmin=-35.3, vmax=91.65,cmap=cmap) 
#ExpLGM_H1=plt.colorbar(ExpLGM_H1,orientation="vertical")
#ExpLGM_H1.set_label('%', rotation=90)
#plt.xlabel('Longitude',color='gray')
#plt.ylabel('Latitude',color='gray')
#plt.title('Dissolved iron/DUST difference percentage')

plt.suptitle("Holocene: Biological export POC",fontsize=14,weight='bold')
plt.subplots_adjust(hspace=0.4)
plt.savefig('/media/natalia/DATA/Documentos/TesisI/Presentación12-08/figuras/figure_CarbonexportLGM2.pdf')

plt.figure(num=None, figsize=(12, 6), dpi=100, facecolor='w', edgecolor='k')
#from matplotlib.colors import Normalize
#class MidpointNormalize(Normalize):
#    def __init__(self, vmin=None, vmax=None, vcenter=None, clip=False):
#        self.vcenter = vcenter
#        Normalize.__init__(self, vmin, vmax, clip)
#
#    def __call__(self, value, clip=None):
#        # I'm ignoring masked values and all kinds of edge cases to make a
#        # simple example...
#        x, y = [self.vmin, self.vcenter, self.vmax], [0, 0.5, 1]
#        return np.ma.masked_array(np.interp(value, x, y))

print('min=(Exp1_median_ALT-Exp1_median_OLD)',np.min(Exp1_median_ALT-Exp1_median_OLD),np.max(Exp1_median_ALT-Exp1_median_OLD))
print('min=(Exp2_median-Exp3_median)',np.min(Exp2_median-Exp3_median),np.max(Exp2_median-Exp3_median))
print('Percentage1',np.min(100*(Exp1_median_ALT-Exp1_median_OLD)/Exp1_median_ALT),np.max(100*(Exp1_median_ALT-Exp1_median_OLD)/Exp1_median_ALT))
print('Percentage2',np.min(100*(Exp2_median-Exp3_median)/Exp2_median),np.max(100*(Exp2_median-Exp3_median)/Exp2_median))

plt.subplot(231)
m.drawcoastlines()
#midnorm = MidpointNormalize(vmin=-0.1, vcenter=0, vmax=0.04)
Exp_R1 = m.pcolor(x,y,(Exp1_median_ALT-Exp1_median_OLD),cmap=cmap) #vmin=-0.69, vmax=0.35, ,norm=midnorm 
Exp_R1=plt.colorbar(Exp_R1,orientation="horizontal")
Exp_R1.set_label('mol m-2 yr-1', rotation=0)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Difference using Dust with \n "ALT"/"OLD" iron cycle')

plt.subplot(232)
m.drawcoastlines()
Exp_R2 = m.pcolor(x,y,(Exp2_median-Exp3_median),vmin=-0.02, vmax=0.1,cmap=cmap) 
Exp_R2=plt.colorbar(Exp_R2,orientation="horizontal")
Exp_R2.set_label('mol m-2 yr-1', rotation=0)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Difference using Dissolved Fe with \n "ALT"/"OLD" iron cycle')


plt.subplot(233)
m.drawcoastlines()
Exp_R2 = m.pcolor(x,y,(Exp2_median-Exp3_median),cmap=cmap)
Exp_R2=plt.colorbar(Exp_R2,orientation="horizontal")
Exp_R2.set_label('mol m-2 yr-1', rotation=0)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Difference using Dissolved Fe with \n "ALT"/"OLD" iron cycle')

plt.subplot(234)
m.drawcoastlines()
Exp_R11 = m.pcolor(x,y,100*(Exp1_median_ALT-Exp1_median_OLD)/Exp1_median_ALT,vmin=-2.6136, vmax=4.7,cmap=cmap) #vmin=-0.69, vmax=0.35, ,norm=midnorm 
Exp_R11=plt.colorbar(Exp_R11,orientation="horizontal")
Exp_R11.set_label('%', rotation=0)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Percentage difference using Dust \n with "ALT"/"OLD" iron cycle')

plt.subplot(235)
m.drawcoastlines()
Exp_R22 = m.pcolor(x,y,100*(Exp2_median-Exp3_median)/Exp2_median,vmin=-2.6136, vmax=4.7,cmap=cmap) 
Exp_R22=plt.colorbar(Exp_R22,orientation="horizontal")
Exp_R22.set_label('%', rotation=0)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Percentage difference using \n Dissolved Fe with "ALT"/"OLD" cycle')

plt.subplot(236)
m.drawcoastlines()
Exp_R22 = m.pcolor(x,y,100*(Exp2_median-Exp3_median)/Exp2_median,cmap=cmap) 
Exp_R22=plt.colorbar(Exp_R22,orientation="horizontal")
Exp_R22.set_label('%', rotation=0)
plt.xlabel('Longitude',color='gray')
plt.ylabel('Latitude',color='gray')
plt.title('Percentage difference using \n Dissolved Fe with "ALT"/"OLD" cycle')

plt.subplots_adjust(hspace=0.4)
plt.savefig('/media/natalia/DATA/Documentos/TesisI/Presentación12-08/figuras/figure_CarbonexportLGM2_differences.pdf')
plt.show()

#plt.subplot(224)
#m.drawcoastlines()
#ExpLGM_H2 = m.contourf(x,y,np.log(Exp4_median),500,map=cmap) 
#ExpLGM_H2=plt.colorbar(ExpLGM_H2,orientation="vertical")
#ExpLGM_H2.set_label('mol m-2 yr-1', rotation=90)
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')
#plt.title('LGM')
#plt.suptitle("Difference Biological export POC",fontsize=14)
#plt.show()


