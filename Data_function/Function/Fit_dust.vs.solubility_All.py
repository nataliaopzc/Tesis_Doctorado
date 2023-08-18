import numpy as np
import matplotlib.pyplot as plt
import numpy.matlib as matlib
#from sklearn.linear_model import LinearRegression

print('name from forcing')
name = input()
print('OK ' + name + ' so :)' ) # También pudo ser print('OK %s so :)' % name)

#name='Albani'
DustH=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/genie-forcings/worjh2.Fe' + name + 'H_Dust_SPIN/biogem_force_flux_sed_det_SUR.dat') # this line defines the file path of the file we are trying to read
DustH=DustH.reshape((1296,))

Sol_feH=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/Solubility/worjh2.det_Fe_sol.' + name + '.dat') # this line defines the file path of the file we are trying to read
Sol_feH=Sol_feH.reshape((1296,))

result1=[float('nan') if  e==0 else 1 for e in Sol_feH ]
result2=[0 if  e==0 else 1 for e in Sol_feH ]

result1=np.array(result1)
DustH=result1*DustH

print(DustH.shape)

DustH=[ e for e in DustH if not  np.isnan(e) ]
Sol_feH=Sol_feH*result1
Sol_feH=[ e for e in Sol_feH if not  np.isnan(e) ]

log_DustH=np.matrix(np.log10(DustH)).T
log_Sol_feH=np.matrix(np.log10(Sol_feH)).T

reg = LinearRegression().fit(log_DustH,log_Sol_feH)
R2=reg.score(log_DustH,log_Sol_feH)
#print(reg.coef_)
#print(reg.intercept_)
print(R2)
coef=reg.coef_[0][0]
intercept=reg.intercept_[0]
coef_a=10**intercept

print(coef,intercept)
#print(DustH.shape,Sol_feH.shape)
x=np.linspace(np.min(DustH),1.5*10**12,num=500)

plt.figure(num=1, figsize=(7, 4.5), dpi=100, facecolor='w', edgecolor='k')

plt.plot(log_DustH,log_Sol_feH,'*')
plt.xlabel('log10(Dust)')
plt.ylabel('Log10(Solubility)')
plt.title('Dust vs Solubility')
ax=plt.gca()
textstr = '\n'.join((
    #r'S=10$^a$xDust$^b$',
    r'R$^2$=0.9999',
    r'a =%.2f' %(coef_a, ),
    r'b =%.2f' %(coef, ),
    r'S=%.2f*F_{dust}'
        # r'$\mu=%.2f$' % (mu, ),
    ))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
plt.text(0.7, 0.93, textstr,transform=ax.transAxes,fontsize=14, horizontalalignment='left',
        verticalalignment='top',bbox=props)

plt.figure(num=2, figsize=(7, 4.5), dpi=100, facecolor='w', edgecolor='k')
plt.plot(DustH,Sol_feH,'*')

#plt.savefig('/home/natalia/Documentos//Documentos/TesisI/Data_function/Regresion_DustvsSol_' + name + '.png')

plt.plot(x,coef_a*(x**coef))
print ('a:',coef_a)
print ('b:',coef)

plt.legend(['Data','Fit'],prop={'size': 14},facecolor='wheat',edgecolor='k',framealpha=0.5)
plt.xlabel('Dust')
plt.ylabel('Solubility')
plt.title('Dust vs Solubility')

#plt.savefig('/home/natalia/Documentos//Documentos/TesisI/Data_function/Regresion_Fit_DustvsSoL_' + name + '.png')


#plt.figure(num=3, figsize=(7, 4.5), dpi=100, facecolor='w', edgecolor='k')
#lt.plot(log_DustH,(log_Sol_feH-((10**intercept)*(log_DustH**coef))),'*')
#plt.xlabel('Dust')
#plt.ylabel('Residual')
#lt.title('')


plt.show()

##############################################
DustLGM=np.genfromtxt('/home/natalia/Documentos/Tesis/Flujos_de_polvo/Globales_Moles/' + name+ '/' + name +'.nc_annualflux_molperyr.36x36_level10.dat')
Sol_feLGM=np.power(DustLGM,coef)*(10**intercept)
Sol_feLGM=Sol_feLGM.reshape((1296,))
Sol_feLGM=result2*Sol_feLGM
Sol_feLGM=Sol_feLGM.reshape((36,36))
print(Sol_feLGM)
np.savetxt('/home/natalia/Documentos/DATA/TesisI/cgenie/worjh2.det_Fe_sol.' + name + '_LGM.dat',Sol_feLGM, fmt='%1.8e')


