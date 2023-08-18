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
	figure = plt.figure(i,figsize=(8, 4.5), dpi=150, facecolor='w', edgecolor='k')
	axes = figure.add_axes([0.13, 0.15, 0.83, 0.8])
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
				CO2.append((np.median(CO2_or[-10:,2])-np.median(CO2_file[-10:,2]))*1e+6/AREA[j])
			for l in range(0,6):
				CO22.append((CO2[l]/Carga1[l])[0])
			bplot=axes.boxplot(CO22,patch_artist=False,positions = [index2[ll]],widths = 0.8)
			for yp,m in zip(CO22,Simbolos):
				plt.grid(axis='y',linestyle = '--')
				axes.scatter(index2[ll], yp, marker=m,c=d,edgecolors='k')
			axes.set_xlim(-2, 22)
	axes.set_xticks([1, 7, 13,19])
	axes.set_xticklabels(['0.3', '0.6', '2', '3'],fontsize=14)
	plt.yticks(fontsize=14)
	axes.set_xlabel('Factor [%]',fontsize=15,fontweight='bold')
	axes.set_ylabel(r'$\bf \Delta$' 'CO' r'$\bf _2$' '[ppm m' r'$\bf ^{-2}$' 'kg' r'$\bf ^{-1}$' ']',fontsize=15,fontweight='bold')
	plt.axvspan(-2, 4, facecolor='gray', alpha=0.3) #	plt.axhline(y=0,linestyle = '-')
	plt.axvspan(10,16, facecolor='gray', alpha=0.3)
	plt.savefig('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Figure4_CO2Diff_'+i+'_Normalize.png')
plt.show()