#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 14:20:57 2022

@author: natalia
"""

from netCDF4 import Dataset as nc #this line imports the package we just installed
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

file=nc('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/worjh2.PO4FeLambertH_calculated_Dust/biogem/fields_biogem_2d.nc')
TDFe=file.variables['ocn_sur_TDFe'][0,:,:] # Eliminé la primera dimensión
lat=file.variables['lat'][:]
lon=file.variables['lon'][:]

import csv
import pandas as pd

FeD=pd.read_csv('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/IDP2021_GEOTRACES_IDP2021_FeD.csv', delimiter=",")
FeD=FeD.iloc[33:,:] # Para cortar dataframe
FeD=FeD.reset_index(); del FeD['index']# Reseteando el indice (posición)
#print(FeD.iloc[0,:]) # Para conocer nombres de las columnas en el dataframe
#FeD['Unnamed: 19'] # Para ver datos 
A=np.array(FeD['Unnamed: 17'], dtype=np.float) #Convierte el objeto en una matriz de números
A=(A<=10); A=np.where(A==True); A=A[0]; A=np.array(A,dtype=np.float)
#D=FeD['Unnamed: 17'][A] #Para ver todos los datos de la "columna 2"
FeD=FeD.iloc[A,:]; FeD=FeD.reset_index(); del FeD['index']
# De aquí en adelante encontrar las posiciones no Nan
B=np.array(FeD['Unnamed: 19'],dtype=np.float);B=(np.isnan(B)); B=np.where(B==False);B=B[0]; B=np.array(B,dtype=np.float)
FeD=FeD.iloc[B,:]; FeD=FeD.reset_index(); del FeD['index']
# De aquí en adelante encontrar las posiciones no Ceros
C=np.array(FeD['Unnamed: 19'],dtype=np.float);C=(C!=0);C=np.where(C==True);C=C[0]; C=np.array(C,dtype=np.float)
FeD=FeD.iloc[C,:]; FeD=FeD.reset_index(); del FeD['index']

df = FeD.astype({'Unnamed: 4': float, 'Unnamed: 5': float,'Unnamed: 19':float})
 

########################################################

#m = Basemap(projection='mill',lon_0=-80,lat_0=0,resolution='l')
m = Basemap(projection='mill',lon_0=0,lat_0=0,resolution='l',
            llcrnrlat = min(lat),
            llcrnrlon = min(lon),
            urcrnrlat = max(lat),
            urcrnrlon = max(lon))


#m.drawcoastlines()
lons, lats = np.meshgrid(lon, lat) # get lat/lons of ny by nx evenly space grid.
x, y = m(lons, lats) # compute map proj coordinates.
#print(Sol_Iron_median.shape[0])
plt.figure(num=None, figsize=(8, 4.5), dpi=150, facecolor='w', edgecolor='k')
cmap = plt.get_cmap('jet')

m.drawcoastlines()
#from matplotlib import ticker
cs2 = plt.contourf(x,y,np.log10(TDFe),cmap=cmap) 
#cbar2=plt.colorbar(cs2,orientation="vertical")
#cbar2.set_label('ln(%)', rotation=90)
plt.xlabel('Longitude',color='black',fontsize=8, fontweight='bold' )
plt.ylabel('Latitude',color='black',fontsize=8, fontweight='bold' )
#plt.title('Aeolian iron solubility')

lon= np.array(df['Unnamed: 4'][:]-360)
lat= np.array(df['Unnamed: 5'][:])
data=np.array(df['Unnamed: 19'][:]);data=np.log10(data*10**-9)
x2,y2=m(lon,lat)

#x2, y2 = m((df['Unnamed: 4'][:]-360),df['Unnamed: 5'][:])
#plt.plot(x2,y2,marker='*',markerfacecolor='pink',markersize=5,markeredgecolor='None',linestyle = 'None')

plt.scatter(x2, y2,10, data,cmap=cmap,marker ="^",linewidths = 0.3,edgecolor ="black")
bar=plt.colorbar(fraction=0.026)
bar.set_label('Surface Fe D [log10(mol/kg)]', rotation=90,fontsize=8)

#############################################################################
import scipy.io
import numpy.matlib
mat = scipy.io.loadmat('/home/natalia/Documentos/Tesis/Functions/Otros/lon_lat.mat')
lon3=(mat['lonlat_edges'][:,0]-265)
lat3=mat['lonlat_edges'][:,1]

lon3,lat3=m(lon3,lat3)
for i in range(37):
    plt.plot(lon3,numpy.matlib.repmat(lat3[i],37,1),'-k',linewidth=0.4)

for j in range(37):
    plt.plot(numpy.matlib.repmat(lon3[j],37,1),lat3,'-k',linewidth=0.4)


#####SA

# for i in range(0,9): #del 29 al 36
#     plt.plot(lon3[14:37],numpy.matlib.repmat(lat3[i],23,1),'-r',linewidth=0.4)
    
for i in range(0,9): #del 29 al 36
    plt.plot(lon3[19:37],numpy.matlib.repmat(lat3[i],18,1),'-r',linewidth=0.8)
    
for i in range(0,9): #del 29 al 36
    plt.plot(lon3[0:6],numpy.matlib.repmat(lat3[i],6,1),'-r',linewidth=0.8)    

for j in range(19,37):
    plt.plot(numpy.matlib.repmat(lon3[j],9,1),lat3[0:9],'-r',linewidth=0.8)
    
for j in range(0,6):
    plt.plot(numpy.matlib.repmat(lon3[j],9,1),lat3[0:9],'-r',linewidth=0.8)    
    
######SP
for i in range(0,9):
     plt.plot(lon3[5:20],numpy.matlib.repmat(lat3[i],15,1),'-b',linewidth=0.8)

for j in range(5,20):
     plt.plot(numpy.matlib.repmat(lon3[j],9,1),lat3[0:9],'-b',linewidth=0.8)

######NP

for i in range(28,37):
    plt.plot(lon3[3:16],numpy.matlib.repmat(lat3[i],13,1),color=(1,0,1),linewidth=0.6)

for j in range(3,16):
   plt.plot(numpy.matlib.repmat(lon3[j],9,1),lat3[28:37],color=(1,0,1),linewidth=0.6)

#######NA

for i in range(28,37):
    plt.plot(lon3[18:26],numpy.matlib.repmat(lat3[i],8,1),color=(1,1,0),linewidth=0.6)

for j in range(18,26):
   plt.plot(numpy.matlib.repmat(lon3[j],9,1),lat3[28:37],color=(1,1,0),linewidth=0.6)

########CEP

for i in range(16,21):
    plt.plot(lon3[9:19],numpy.matlib.repmat(lat3[i],10,1),color=(1/255,1,0),linewidth=0.6)

for j in range(9,19):
    plt.plot(numpy.matlib.repmat(lon3[j],5,1),lat3[16:21],color=(1/255,1,0),linewidth=0.6)


##############################################################################
######SAI
plt.text(lon3[30], lat3[3], 'SAI', style='italic',
        bbox={'facecolor': 'red', 'alpha': 1, 'pad': 2, 'edgecolor':'none'},fontsize=7)
######SP
plt.text(lon3[12], lat3[3], 'SP', style='italic',
        bbox={'facecolor': 'blue', 'alpha': 1, 'pad':2 ,'edgecolor':'none'},fontsize=7)
######NP
plt.text(lon3[9], lat3[33], 'NP', style='italic',
        bbox={'facecolor': 'm', 'alpha': 1, 'pad': 2,'edgecolor':'none'},fontsize=7)
######NA
plt.text(lon3[22], lat3[33], 'NA', style='italic',
        bbox={'facecolor': (1,1,0), 'alpha': 1, 'pad': 2,'edgecolor':'none'},fontsize=7)
######CP
plt.text(lon3[13], lat3[18], 'CEP', style='italic',
        bbox={'facecolor': (1/255,1,0), 'alpha': 1, 'pad': 2,'edgecolor':'none'},fontsize=7)

plt.savefig('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Figure1.png')