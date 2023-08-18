# %%

#import  tarfile
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches
from matplotlib.lines import Line2D


legend_elements = [Line2D([0], [0], linestyle='',label='PERIOD'),
Line2D([0], [0], color='red', linestyle='-',lw=2, label='Holocene'),
Line2D([0], [0], color='blue', linestyle='-',lw=2, label='LGM'),
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
SOL=[0.3333, 0.6666,1,2,3]

colors = ['yellow', 'pink', 'green','blue','red']
Simbolos=['o','p','v','s','x','D']

index=[]
for z in range(5,30,6):
	for n in range(6,1,-1):
		index.append(z-n)
index2=[-0, 3,6, 9, 12]
index2_cont=3

###############################################################################
# %%
figure=plt.figure(None,figsize=(8, 4.5), dpi=150, facecolor='w', edgecolor='k')
p=0
for i, c in zip(TIME,range(1,3)):
	axes = figure.add_axes([0.1,0.1,0.85,0.85])
	p+=0.04
	ii=-1
	ll=-1
	for k in SOL:
		CO2=[]
		ll+=1
		ii+=1
		for h in MODEL:
			CO2_file=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/Global/'+h+'/worjh2.PO4Fe'+h+'_'+i+'_Sol_calculated_Dust_Control_x'+str(k)+'/biogem/biogem_series_atm_pCO2.res',comments="%")
			CO2_1=CO2_file[-10:,2]*1e+6
			CO2.append(np.median(CO2_1,axis=0))
		bplot=axes.boxplot(CO2,patch_artist=False,positions = [index2[ii]],widths = 0.8,showfliers=False)
		for yp,m in zip(CO2,Simbolos):
			plt.grid(axis='y',linestyle = '--')
			if i=='H':
				axes.scatter(index2[ll], yp,s=16, marker=m,c="r")
			else:
				axes.scatter(index2[ll], yp,s=16, marker=m,c="b")
		axes.set_xlim(-1.5, 13.5)
		axes.set_ylim(210, 340)
		axes.set_xticks([0,3, 6,9,12])
		axes.set_xticklabels(['0.3', '0.6', '1','2', '3'],fontsize=10)
		plt.yticks(fontsize=10) 
		axes.set_ylabel(r'$ \bf $' 'pCO' r'$\bf _2$' ' [ppm]',fontsize=10,fontweight='bold')
		plt.axvspan(-1.5, 1.5, facecolor='gray', alpha=0.03)
		plt.axvspan(4.5,7.5, facecolor='gray', alpha=0.03)
		plt.axvspan(10.5,13.5, facecolor='gray', alpha=0.03)
		plt.tick_params(axis='x', bottom = False)
		axes.legend(handles=legend_elements, loc='upper right',fontsize=8)
		axes.set_xlabel('Multiplication factor of iron solubility',fontsize=9,fontweight='bold')
		# Add rectangle
axes.add_patch(
patches.Rectangle(
(5.5, 240), # (x,y)
4, # width
15, # height
# You can add rotation as well with 'angle'
alpha=0.25, facecolor="purple", edgecolor="purple", linewidth=2, linestyle='solid')
)
plt.savefig('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Figurex1_Subplot_CO2.png')
plt.show()

# %%
