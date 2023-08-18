#import  tarfile
#%%
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.io import loadmat
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

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

figure = plt.figure(None,figsize=(10, 5.8), dpi=150, facecolor='w', edgecolor='k')
p=0
ii=0
for i, c in zip(TIME,range(1,4,2)):
	axes = figure.add_subplot(2,2,c)
	chartBox = axes.get_position()
	axes.set_position([chartBox.x0-0.055, chartBox.y0+0.04-p,
             	chartBox.width,
             	chartBox.height])
	Carga=loadmat('/home/natalia/Documentos/Tesis/Functions/Otros/DUST_AREA.mat')
	Carga=np.array([Carga['Albani'][:,:,ii],Carga['Lambert'][:,:,ii],Carga['Takemura'][:,:,ii],Carga['Ohgaito'][:,:,ii],Carga['MIROC_ESM'][:,:,ii],
	Carga['MRI_CGCM3'][:,:,ii]]) #0 es holoceno y 1 es LGM--> Ver: make_Dust_escalado_region.m
	ii+=1
	p+=0.04
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
				CO2_or=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/Global/'+h+'/worjh2.PO4Fe'+h+'_'+i+'_Sol_calculated_Dust_Control_x1/biogem/biogem_series_atm_pCO2.res',comments="%")
				CO2_file=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/Regional/'+h+'/worjh2.PO4Fe'+h+'_'+i+'_Sol_calculated_Dust_'+j+'_x'+str(k)+'/biogem/biogem_series_atm_pCO2.res',comments="%")
				Carga1.append(Carga[vv,zz])
				CO2.append((np.median(CO2_or[-10:,2])-np.median(CO2_file[-10:,2]))*1e+6/AREA[j])
			for l in range(0,6):
				CO22.append((CO2[l]/Carga1[l])[0])
			bplot=axes.boxplot(CO22,patch_artist=False,positions = [index2[ll]],widths = 0.8,showfliers=False) #showfliers=False-->quita los círculos de outliers
			for yp,m in zip(CO22,Simbolos):
				plt.grid(axis='y',linestyle = '--')
				axes.scatter(index2[ll], yp, s=16,marker=m,c=d,linewidths=0.5)
			axes.set_xlim(-2, 22)
			axes.set_ylim(-1.1e-15, 3e-15)
	axes.set_xticks([1, 7, 13,19])
	axes.set_yticks(np.arange(-1e-15,3e-15,0.5e-15))
	axes.set_xticklabels(['0.3', '0.6', '2', '3'],fontsize=8)
	axes.set_yticklabels(np.arange(-1,3,0.5),fontsize=8)
	plt.yticks(fontsize=8)
	axes.set_ylabel(r'$\bf \frac{\Delta pCO_{2}}{Axm}$' ' [ppm m' r'$\bf ^{-2}$' 'kg' r'$\bf ^{-1}$' r'$\bf x10^{-15}$' ']',fontsize=9,fontweight='bold')
	plt.axvspan(-2, 4, facecolor='gray', alpha=0.3) #	plt.axhline(y=0,linestyle = '-')
	plt.axvspan(10,16, facecolor='gray', alpha=0.3)
	plt.tick_params(axis='x', bottom = False)
	if i=='H':
		plt.title('a)',x=-0.16, y=1.05)
	else:
		plt.title('c)',x=-0.16, y=1.05)
		axes.set_xlabel('Multiplication factor of iron solubility',fontsize=9,fontweight='bold')
#plt.savefig('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Figure4_Subplot_CO2Diff_Normalize.png')
#plt.show()
# %%
