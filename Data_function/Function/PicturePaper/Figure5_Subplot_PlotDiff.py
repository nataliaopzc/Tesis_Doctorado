# %%
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.io import loadmat
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from matplotlib.font_manager import FontProperties
import itertools
import matplotlib.ticker as mtick

MODEL=['Albani','Lambert','Takemura','Ohgaito','MIROC-ESM','MRI-CGCM3']
AREA={'NA':2.2040e+13,'NP':4.0931e+13,'CP': 1.4168e+13,'SP':4.4080e+13,'SA':6.9268e+13}
TIME=['H','LGM']
REGION=['NA', 'NP','CP', 'SP','SA']
SOL=[0.3333, 0.6666,2,3]

colors = ['yellow', 'pink', 'green','blue','red']
Simbolos=['o','*','v','s','x','D']

figure = plt.figure(None,figsize=(10, 5.8), dpi=150, facecolor='w', edgecolor='k')
pp=2
ii=0
p=0
for i, c in zip(TIME,range(1,4,2)):
	pp-=1
	axes = figure.add_subplot(2,2,c)
	chartBox = axes.get_position()
	axes.set_position([chartBox.x0-0.055, chartBox.y0+0.04-p,
             	chartBox.width,
             	chartBox.height])
	Solubility=loadmat('/home/natalia/Documentos/Tesis/Functions/Otros/Solubility.mat')
	Solubility=np.array([Solubility['OUT'][:,:,pp]]) # Aquí es al revés, 0 es LGM y 1 Holoceno-->Ver: make_Solubility_escalado_region.m
	Solubility=Solubility[0,:,:]
	ii+=1
	zz=-1
	p+=0.04
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
				CO2_or=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/Global/'+h+'/worjh2.PO4Fe'+h+'_'+i+'_Sol_calculated_Dust_Control_x1/biogem/biogem_series_atm_pCO2.res',comments="%")
				CO2_file=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/Regional/'+h+'/worjh2.PO4Fe'+h+'_'+i+'_Sol_calculated_Dust_'+j+'_x'+str(k)+'/biogem/biogem_series_atm_pCO2.res',comments="%")
				CO2.append((np.median(CO2_or[-10:,2])-np.median(CO2_file[-10:,2]))*1e+6)
			for xp,yp,m in zip(Sol,CO2,Simbolos):
				axes.grid(True)
				axes.scatter(xp, yp, marker=m,c=d,s=16,linewidths=0.5)
			#plt.xlim(-0.1,8) #LGM
			plt.ylim(-8,14)
			#axes.set_yticks(np.arange(-0.75e-5,1.5e-5,0.25e-5))
			#axes.set_yticklabels(np.arange(-0.75,1.5,0.25),fontsize=8)
			plt.xticks(fontsize=8);plt.yticks(fontsize=8)
			axes.set_ylabel(r'$\bf \Delta pCO_{2}$' ' [ppm]',fontsize=10,fontweight='bold')
	if i=='LGM':
		plt.title('c)',x=-0.16, y=1.05)
		axes.set_xlabel('Median iron solubility [%]',fontsize=9,fontweight='bold')
	else:
		plt.title('a)',x=-0.16, y=1.05)
	#plt.savefig('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Figure5_CO2Diff_'+i+'.png')

# %%
