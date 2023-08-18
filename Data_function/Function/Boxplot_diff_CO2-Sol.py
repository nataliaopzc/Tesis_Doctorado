#import  tarfile
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.io import loadmat
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], linestyle='',label='REGION'),
Line2D([0], [0], color='yellow', lw=4, label='NA'),
Line2D([0], [0], color='pink', lw=3, label='NP'),
Line2D([0], [0], color='green', lw=3, label='CP'),
Line2D([0], [0], color='blue', lw=3, label='SP'),
Line2D([0], [0], color='red', lw=3, label='SA'),
Line2D([0], [0], linestyle='',label='DUST SOURCE'),
Line2D([0], [0],  marker='o',color='black', linestyle='',lw=3, label='Albani'),
Line2D([0], [0],  marker='p',color='black', linestyle='',lw=3, label='Lambert'),
Line2D([0], [0],  marker='v',color='black', linestyle='',lw=3, label='Takemura'),
Line2D([0], [0],  marker='s',color='black', linestyle='',lw=3, label='Ohgaito'),
Line2D([0], [0],  marker='X',color='black', linestyle='',lw=3, label='MIROC-ESM'),
Line2D([0], [0],  marker='D',color='black', linestyle='',lw=3, label='MRI-CGCM3')]

MODEL=['Albani','Lambert','Takemura','Ohgaito','MIROC-ESM','MRI-CGCM3']
AREA={'NA':2.2040e+13,'NP':4.0931e+13,'CP': 1.4168e+13,'SP':4.4080e+13,'SA':6.9268e+13}
TIME=['H','LGM']
REGION=['NA', 'NP','CP', 'SP', 'SA']
SOL=[0.3333, 0.6666,2,3]

colors = ['yellow', 'pink', 'green','blue','red']
Simbolos=['o','p','v','s','x','D']

index=[]
for z in range(5,30,6):
	for n in range(6,1,-1):
		index.append(z-n)
index2=np.array([-1, 5,11, 17, 0,6,12,18,1,7,13,19,2,8,14,20,3,9,15,21])
ii=0
for i in TIME:
	figure = plt.figure(i,figsize=(8, 5), dpi=100, facecolor='w', edgecolor='k')
	axes = figure.add_axes([0.1, 0.1, 0.8, 0.8])
# 	if i == 'LGM':
# 		axes2 = figure.add_axes([0.54, 0.39, 0.353, 0.35]) 
	Carga=loadmat('/home/natalia/Documentos/Tesis/Functions/Otros/DUST_AREA.mat')
	Carga=np.array([Carga['Albani'][:,:,ii],Carga['Lambert'][:,:,ii],Carga['Takemura'][:,:,ii],Carga['Ohgaito'][:,:,ii],Carga['MIROC_ESM'][:,:,ii],
	Carga['MRI_CGCM3'][:,:,ii]]) #0 es holoceno y 1 es LGM--> Ver: make_Dust_escalado_region.m
	ii+=1
	zz=-1
	ll=-1
	for j,d in zip(REGION,colors):
		zz+=1
		for k in SOL:
			CO2=[]
			CO22=[]
			Carga1=[]
			ll+=1
			vv=-1
			for h in MODEL:
				vv+=1
				CO2_or=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/worjh2.PO4Fe'+h+i+'_calculated_Dust/biogem/biogem_series_atm_pCO2.res',comments="%")
				CO2_file=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/worjh2.PO4Fe'+h+'_'+i+'_Sol_calculated_Dust_'+j+'_x'+str(k)+'/biogem/biogem_series_atm_pCO2.res',comments="%")
				Carga1.append(Carga[vv,zz])
				CO2.append((np.median(CO2_or[-10:,2]-np.median(CO2_file[-10:,2])))*1e+6/AREA[j])
			for l in range(0,6):
				CO22.append((CO2[l]/Carga1[l])[0])
			bplot=axes.boxplot(CO22,patch_artist=False,positions = [index2[ll]],widths = 0.8)
			for yp,m in zip(CO22,Simbolos):
				axes.grid(True)
				axes.scatter(index2[ll], yp, marker=m,c=d,edgecolors='k')
# 			if i == 'LGM':
# 				for yp,m in zip(CO22,Simbolos):
# 					axes2.scatter(index2[ll], yp, marker=m,c='k')
# 					bplot2=axes2.boxplot(CO22,patch_artist=True,positions = [index2[ll]],widths = 0.8)
				# for box2 in zip(bplot2['boxes']):
		 	# 		for patch, color in zip(bplot2['boxes'], colors):
		 	# 			patch.set_facecolor(d)
		 # 			plt.xlim(-2,23) #LGM
		 # 			plt.ylim(-1e-15,2e-15) #LGM
		 # 			axes2.set_xticks([1, 7, 13,19])
		 # 			axes2.set_xticklabels(['0.3', '0.6', '2', '3'])
			# # for box in zip(bplot['boxes']):
			# # 	for patch, color in zip(bplot['boxes'], colors):
		 # # 			patch.set_facecolor(d)
			axes.set_xticks([1, 7, 13,19])
			axes.set_xticklabels(['0.3', '0.6', '2', '3'],fontsize=14)
			axes.set_xlabel('Iron solubility Factor',fontsize=18)
			axes.set_ylabel('ΔCO2 [ppm m-2 kg-1]',fontsize=18)
			#axes.legend(handles=legend_elements, prop={'size': 12},loc='upper left')

plt.show()