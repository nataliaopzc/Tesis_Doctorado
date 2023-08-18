# %%
import csv
import pandas as pd
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt


legend_elements = [Line2D([0], [0], linestyle='',label='DUST SOURCE'),
Line2D([0], [0],  marker='o',color='black', linestyle='',lw=3, label='Albani'),
Line2D([0], [0],  marker='p',color='black', linestyle='',lw=3, label='Lambert'),
Line2D([0], [0],  marker='v',color='black', linestyle='',lw=3, label='Takemura'),
Line2D([0], [0],  marker='s',color='black', linestyle='',lw=3, label='Ohgaito'),
Line2D([0], [0],  marker='X',color='black', linestyle='',lw=3, label='MIROC-ESM'),
Line2D([0], [0],  marker='D',color='black', linestyle='',lw=3, label='MRI-CGCM3'),
Line2D([0], [0], linestyle='',label='FACTOR'),
Line2D([0], [0],  color='pink', lw=3,label='0.3'),
Line2D([0], [0],  color='blue', lw=3,label='0.6'),
Line2D([0], [0],  color='white', lw=3,label='1'),
Line2D([0], [0],  color='green', lw=3,label='2'),
Line2D([0], [0],  color='orange', lw=3,label='3')]


MODEL=['Albani','Lambert','Takemura','Ohgaito','MIROC-ESM','MRI-CGCM3']
REGION=['NA', 'NP','CP', 'SP', 'SA']
SOL=[0.3333, 0.6666,2,3]
Sim=['o','p','v','s','x','D']
colors = ['pink', 'lightblue', 'lightgreen','orange'];color=colors*5;color.insert(0, "white")

dCO2=pd.read_excel('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Tabla/Tabla.xlsx')
dCO2=(np.array(dCO2)).T;dCO2=dCO2[1:7];

figure=plt.figure(None,figsize=(8, 4.5), dpi=150, facecolor='w', edgecolor='k')
figure.add_axes([0.09, 0.1, 0.73, 0.8])

bplot=plt.boxplot(dCO2,showfliers=False,patch_artist=True)

for b, c in zip(bplot['boxes'], color):
    b.set_alpha(0.6)
    b.set_edgecolor('k') # or try 'black'
    b.set_facecolor(c)
    b.set_linewidth(1)

for h in range(1,22):
    for m,l in zip(Sim,range(7)):
        plt.scatter(h,dCO2[l,h-1],s=16,marker=m,c='black')

for i,j in zip(np.arange(1.5,21,8), np.arange(5.5,22,8)):
	plt.axvspan(i,j,facecolor='gray', alpha=0.3) 
plt.xticks([1, 3.5, 7.5,11.5,15.5,19.5],['Global', 'NA', 'NP', 'CEP','SP','SAI'],fontsize=9,fontweight='bold')
plt.ylabel(r'$ \bf \Delta$' 'pCO' r'$\bf _2$' ' [ppm]',color='black',fontsize=9, fontweight='bold')
plt.xlim(0, 22)
plt.ylim(0, 50)
plt.grid(axis='y',linestyle = '--')
plt.legend(handles=legend_elements, loc='upper right',fontsize=9, bbox_to_anchor=(1.25, 1.03))
plt.tick_params(axis='x', bottom = False)
#plt.savefig('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Figure6_Boxplot_Tabla.png')
# %%
