#PRUEBA
import numpy as np
#from mpl_toolkits.basemap import Basemap
#import matplotlib.pyplot as plt


file_sig=np.genfromtxt('/natalia/Documentos/DATA/TesisI/cgenie/SPIN/Spin-up_Holoceno/biogem_force_flux_sed_det_SUR.dat') # this line defines the file path of the file we are trying to read
file_sig=np.flip(file_sig,axis=0)
file_sig=0.035*file_sig
area=np.genfromtxt('/natalia/Documentos/DATA/TesisI/cgenie/SPIN/area_t.dat')
area=np.flip(np.reshape(area, (36, 36)),axis=0) #Ejemplo -->A=np.flip([[2,3],[4,5]],axis=0) -> A=[[4 5][2 3]]
file_sig=(file_sig*area*365*24*60*60)/0.055845
np.savetxt('/natalia/Documentos/DATA/TesisI/cgenie/SPIN/Spin-up_Holoceno/biogem_force_flux_ocn_Fe_SUR.dat',file_sig, fmt='%1.6e')

file_sig2=np.genfromtxt('/media/natalia/DATA/Documentos/TesisI/cgenie/SPIN/Spin-up_LGM/biogem_force_flux_sed_det_SUR.dat') # this line defines the file path of the file we are trying to read
file_sig2=np.flip(file_sig2,axis=0)
file_sig2=(3.5/100)*file_sig2
file_sig2=(file_sig*area*365*24*60*60)/0.055845

np.savetxt('/natalia/Documentos/DATA/TesisI/cgenie/SPIN/Spin-up_LGM/biogem_force_flux_ocn_Fe_SUR.dat',file_sig2, fmt='%1.6e')

##################
######################
cmap = plt.get_cmap('nipy_spectral')
x=np.linspace(1,36,num=36,dtype=int)
y=np.linspace(1,36,num=36,dtype=int)
X, Y=np.meshgrid(x,y)

plt.subplot(1,2,1)
H1 = plt.contourf(X,Y,np.log(file_sig),500,cmap=cmap) 
H1=plt.colorbar(H1,orientation="horizontal")
H1.set_label('%', rotation=0)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Dust flux')


file_sig_1=np.genfromtxt('/natalia/Documentos/DATA/TesisI/cgenie/SPIN/Spin-up_Holoceno/biogem_force_flux_ocn_Fe_SUR_1.dat') # this line defines the file path of the file we are trying to read

plt.subplot(1,2,2)
H1 = plt.contourf(X,Y,np.log(file_sig_1),500,cmap=cmap) 
H1=plt.colorbar(H1,orientation="horizontal")
H1.set_label('%', rotation=0)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Dust flux')

plt.show()

exit()
#plt.subplot(1,2,2)
#H = plt.pcolor(np.log(file_sig),cmap=cmap) 
#H=plt.colorbar(H,orientation="horizontal")
#H.set_label('%', rotation=0)
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')
#plt.title('Dust flux')

#plt.figure()

#H1 = plt.contourf(X,Y,np.log(file_sig_1),500,cmap=cmap) 
#H1=plt.colorbar(H1,orientation="horizontal")
#H1.set_label('%', rotation=0)
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')
#plt.title('Dust flux')

plt.show()
