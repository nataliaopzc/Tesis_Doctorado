import numpy as np
import matplotlib.pyplot as plt
import numpy.matlib as matlib
from sklearn.linear_model import LinearRegression

DustH=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/worjh2.FeMahowald2006H_SPIN/biogem_force_flux_ocn_Fe_SUR.dat') # this line defines the file path of the file we are trying to read
#DustH=DustH(result)

DustH=DustH.reshape((1296,))

Sol_feH=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/worjh2.det_Fe_sol.Mahowald.dat') # this line defines the file path of the file we are trying to read
Sol_feH=Sol_feH.reshape((1296,))

result1=[float('nan') if  e==0 else 1 for e in Sol_feH ]
result2=[0 if  e==0 else 1 for e in Sol_feH ]
#result = np.where(Sol_feH == 0)
result1=np.array(result1)
DustH=result1*DustH

print(DustH.shape)

#DustH=[float('nan') if  e==float(0) else e[0] for e in DustH ]
DustH=[ e for e in DustH if not  np.isnan(e) ]
Sol_feH=Sol_feH*result1
Sol_feH=[ e for e in Sol_feH if not  np.isnan(e) ]

log_DustH=np.matrix(np.log10(DustH)).T
log_Sol_feH=np.matrix(np.log10(Sol_feH)).T

reg = LinearRegression().fit(log_DustH,log_Sol_feH)


# ##############################################
# DustLGM=np.genfromtxt('/media/natalia/DATA/Documentos/TesisI/cgenie/biogem_force_flux_sed_det_SUR_LGM.dat')
# Sol_feLGM=np.power(DustLGM,coef)*(10**intercept)
# Sol_feLGM=Sol_feLGM.reshape((1296,))
# Sol_feLGM=result2*Sol_feLGM
# Sol_feLGM=Sol_feLGM.reshape((36,36))
# print(Sol_feLGM)
# #np.savetxt('/media/natalia/DATA/Documentos/TesisI/cgenie/worjh2.det_Fe_sol.Mahowald_LGM.dat',Sol_feLGM, fmt='%1.8e')


