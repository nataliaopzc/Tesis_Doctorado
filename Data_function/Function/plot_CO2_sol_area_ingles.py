#import  tarfile
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.io import loadmat
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from matplotlib.font_manager import FontProperties
import itertools

legend_elements = [Line2D([0], [0], linestyle='',label='REGION'),
Line2D([0], [0], marker='o', color='yellow', linestyle='',lw=4, label='NA'),
Line2D([0], [0],  marker='o',color='pink', linestyle='',lw=3, label='NP'),
Line2D([0], [0], marker='o', color='green', linestyle='',lw=3, label='CP'),
Line2D([0], [0],  marker='o',color='blue', linestyle='',lw=3, label='SP'),
Line2D([0], [0],  marker='o',color='red', linestyle='',lw=3, label='SA'),
Line2D([0], [0], linestyle='',label='DUST SOURCE'),
Line2D([0], [0],  marker='o',color='black', linestyle='',lw=3, label='Albani'),
Line2D([0], [0],  marker='p',color='black', linestyle='',lw=3, label='Lambert'),
Line2D([0], [0],  marker='v',color='black', linestyle='',lw=3, label='Takemura'),
Line2D([0], [0],  marker='s',color='black', linestyle='',lw=3, label='Ohgaito'),
Line2D([0], [0],  marker='X',color='black', linestyle='',lw=3, label='MIROC-ESM'),
Line2D([0], [0],  marker='D',color='black', linestyle='',lw=3, label='MRI-CGCM3'),
Line2D([0], [0], linestyle='',label='FACTOR'),
Line2D([0], [0],  marker='o',color='black', linestyle='',markersize=2, label='0.3'),
Line2D([0], [0],  marker='o',color='black', linestyle='',markersize=5, label='0.6'),
Line2D([0], [0],  marker='o',color='black', linestyle='',markersize=12, label='2'),
Line2D([0], [0],  marker='o',color='black', linestyle='',markersize=18, label='3'),
]

MODEL=['Albani','Lambert','Takemura','Ohgaito','MIROC-ESM','MRI-CGCM3']
AREA={'NA':2.2040e+13,'NP':4.0931e+13,'CP': 1.4168e+13,'SP':4.4080e+13,'SA':6.9268e+13}
TIME=['H','LGM']
REGION=['NA', 'NP','CP', 'SP','SA']
SOL=[0.3333, 0.6666,2,3]

colors = ['yellow', 'pink', 'green','blue','red']
Simbolos=['o','p','v','s','x','D']

pp=2
ii=0
for i in TIME:
	pp-=1
	figure=plt.figure(i,figsize=(10, 6), dpi=100, facecolor='w', edgecolor='k')
	axes = figure.add_axes([0.1, 0.1, 0.8, 0.8])
 	# axes2 = figure.add_axes([0.54, 0.15, 0.35, 0.29]) # LGM
	Carga=loadmat('/home/natalia/Documentos/Tesis/Functions/Otros/DUST_AREA.mat')
	Carga=np.array([Carga['Albani'][:,:,ii],Carga['Lambert'][:,:,ii],Carga['Takemura'][:,:,ii],Carga['Ohgaito'][:,:,ii],Carga['MIROC_ESM'][:,:,ii],
	Carga['MRI_CGCM3'][:,:,ii]]) #0 es holoceno y 1 es LGM--> Ver: make_Dust_escalado_region.m
	Solubility=loadmat('/home/natalia/Documentos/Tesis/Functions/Otros/Solubility.mat')
	Solubility=np.array([Solubility['OUT'][:,:,pp]]) # Aquí es al revés, 0 es LGM y 1 Holoceno-->Ver: make_Solubility_escalado_region.m
	print(np.shape(Solubility));Solubility=Solubility[0,:,:];print(np.shape(Solubility))
	ii+=1
	zz=-1
	for j,d in zip(REGION,colors):
		zz+=1
		ll=-1
		Sol2=[]
		CO222=[]
		for k in SOL:
			CO2=[]
			CO22=[]
			Carga1=[]
			Sol=[]
			vv=-1
			ll+=1
			for h in MODEL:
				vv+=1
				Sol.append(Solubility[zz,4*vv+ll])
				Sol2.append(Solubility[zz,4*vv+ll])
				############################## CO2 ########################
				CO2_or=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/worjh2.PO4Fe'+h+i+'_calculated_Dust/biogem/biogem_series_atm_pCO2.res',comments="%")
				CO2_file=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/worjh2.PO4Fe'+h+'_'+i+'_Sol_calculated_Dust_'+j+'_x'+str(k)+'/biogem/biogem_series_atm_pCO2.res',comments="%")
				Carga1.append(Carga[vv,zz])
				#print((np.median(CO2_or[-100:,2])-np.median(CO2_file[-100:,2])))
				CO2.append((np.median(CO2_or[-10:,2])-np.median(CO2_file[-10:,2]))*1e+6/AREA[j])
# 			for l in range(0,6):
# 				CO22.append((CO2[l]/Carga1[l])[0])
# 				CO222.append((CO2[l]/Carga1[l])[0])
			for xp,yp,m in zip(Sol,CO2,Simbolos):
				axes.grid(True)
				axes.scatter(xp, yp,s=4**(ll+1.2), marker=m,c=d)
# 				axes2.scatter(xp, yp,s=4**(ll+1.2), marker=m,c=d)
# 				if i == 'H':
# 					plt.xlim(0,1.5) # 1.2 #H
# 					plt.ylim(-0.35e-15,0.5e-15) #H
# 				else:
# 					plt.xlim(0,1.2) #LGM
# 					plt.ylim(-2e-16,4e-16) #LGM
			axes.set_xlabel('Iron solubility [%]',fontsize=24)
			axes.set_ylabel('ΔCO2 [ppm m-2]',fontsize=24)
			#axes.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(0.993, 0.94))
			#plt.title('Dust vs Solubility')
plt.show()
