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
MODELO=['Albani','Lambert','Takemura','Ohgaito','MRI-CGCM3']

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
index2=[-1, 5,11, 17, 0,6,12,18,1,7,13,19,2,8,14,20,3,9,15,21]
index2_cont=3

for i in TIME:
	figure = plt.figure(i,figsize=(9, 6), dpi=100, facecolor='w', edgecolor='k')
	axes = figure.add_axes([0.1, 0.1, 0.8, 0.8])
# 	if i == 'LGM':
# 		axes2 = figure.add_axes([0.53, 0.645, 0.27, 0.25]) #(iniciox,inicioy,ancho,alto)
	ii=-1
	ll=-1
	for j,d in zip(REGION,colors):
		for k in SOL:
			CO2=[]
			CO2_c=[]
			ll+=1
			ii+=1
			for h in MODEL:
				CO2_file=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/worjh2.PO4Fe'+h+'_'+i+'_Sol_calculated_Dust_'+j+'_x'+str(k)+'/biogem/biogem_series_atm_pCO2.res',comments="%")
				CO2_cont=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/worjh2.PO4Fe'+h+i+'_calculated_Dust/biogem/biogem_series_atm_pCO2.res',comments="%")
				CO2.append(np.median(CO2_file[-10:,2]*1e+6))
				CO2_c.append(np.median(CO2_cont[-10:,2]*1e+6))
				#axes.legend(handles=legend_elements, prop={'size': 12},loc='upper right')
			bplot=axes.boxplot(CO2,patch_artist=False,positions = [index2[ii]],widths = 0.8)
			for yp,m in zip(CO2,Simbolos):
				axes.grid(True)
				axes.scatter(index2[ll], yp, marker=m,c=d)
# 			if i == 'LGM':
# 				CO2_2=[]
# 				CO2_c2=[]
# 				for hh in MODEL:
# 					CO2_file2=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/worjh2.PO4Fe'+hh+'_'+i+'_Sol_calculated_Dust_'+j+'_x'+str(k)+'/biogem/biogem_series_atm_pCO2.res',comments="%")
# 					CO2_cont2=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/worjh2.PO4Fe'+hh+i+'_calculated_Dust/biogem/biogem_series_atm_pCO2.res',comments="%")
# 					CO2_2.append(np.median(CO2_file2[-10:,2]*1e+6))
# 					CO2_c2.append(np.median(CO2_cont2[-10:,2]*1e+6))
# # 				bplot2=axes2.boxplot(CO2_2,patch_artist=False,positions = [index2[ii]],widths = 0.8)
# # 				bplotc=axes2.boxplot(CO2_c2,patch_artist=False,positions = [10],widths = 0.8)
# 				#axes2.set_xticks([1, 7, 13,19])
# 		 		#axes2.set_xticklabels(['0.3', '0.6', '2', '3'])
			axes.set_xlim(-2, 23)
	bplot=axes.boxplot(CO2_c,patch_artist=False,positions = [10],widths = 0.8)
	for yp,m in zip(CO2_c,Simbolos):
		axes.grid(True)
		axes.scatter(10, yp, marker=m,c=d)
	#plt.xticks([1, 7,10, 13,19], ['0.3', '0.6','1', '2', '3'],fontsize=14)
	axes.set_xticks([1, 7, 13,19])
	axes.set_xticklabels(['0.3', '0.6', '2', '3'],fontsize=14)
	axes.set_xlabel('Iron solubility factor [%]',fontsize=24)
	axes.set_ylabel('Atmospheric CO2 [ppm]',fontsize=24)
	axes.text(10, max(CO2_c) + 0.5, u'Control', fontsize = 11, horizontalalignment='center', verticalalignment='center',weight='bold')  # Colocamos texto cerca del valor donde se encuentra el máximo
plt.show()