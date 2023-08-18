#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 19:38:08 2022

@author: natalia
"""
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
Line2D([0], [0],  color='orange', lw=3,label='3'),
Line2D([0], [0],  color='green', lw=3,label='2'),
Line2D([0], [0],  color='white', lw=3,label='1'),
Line2D([0], [0],  color='blue', lw=3,label='0.6'),
Line2D([0], [0],  color='pink', lw=3,label='0.3'),
]

AREA={'NA':2.2040e+13,'NP':4.0931e+13,'CP': 1.4168e+13,'SP':4.4080e+13,'SA':6.9268e+13}
MODEL=['Albani','Lambert','Takemura','Ohgaito','MIROC-ESM','MRI-CGCM3']
REGION=['NA', 'NP','CP', 'SP', 'SA']
SOL=[0.3333, 0.6666,2,3]
TIME=['H', 'LGM']
Sim=['o','p','v','s','x','D']
colors = ['pink', 'lightblue', 'lightgreen','orange'];color=colors*5#;color.insert(0, "white")

figure=plt.figure(None,figsize=(8, 4.5), dpi=150, facecolor='w', edgecolor='k')
figure.add_axes([0.09, 0.1, 0.73, 0.8])

for r,n in zip(REGION,np.arange(1,20,4)):
    dCO2=np.zeros((6,4))
    CO2H=pd.read_excel('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Tabla/cgenie_output_Regional_H_'+r+'.xlsx')
    CO2LGM=pd.read_excel('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Tabla/cgenie_output_Regional_LGM_'+r+'.xlsx')
    for s,j in zip(SOL,range(4)):
        dCO2[:,j]=(CO2LGM[s]-CO2H[s])*AREA[r]
    df22 = pd.DataFrame(dCO2,columns=SOL,index=MODEL)
    bplot=plt.boxplot(df22,positions = np.arange(n,n+4),showfliers=False,patch_artist=True,vert=False)
    for b, c in zip(bplot['boxes'], color):
        b.set_alpha(0.6)
        b.set_edgecolor('k') # or try 'black'
        b.set_facecolor(c)
        b.set_linewidth(1)
    for m,l in zip(Sim,range(6)):
        plt.scatter(dCO2[l,:],np.arange(n,n+4),s=16,marker=m,c='black')

colors.insert(2, "white")
SOL=[0.3333, 0.6666,1,2,3]
dCO2c=np.zeros((6,5))
CO2Hc=pd.read_excel('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Tabla/cgenie_output_Global_H.xlsx')
CO2LGMc=pd.read_excel('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Tabla/cgenie_output_Global_LGM.xlsx') 
for s,j in zip(SOL,range(5)):        
    dCO2c[:,j]=(CO2LGMc[s]-CO2Hc[s])     
bplot=plt.boxplot(dCO2c,positions = np.arange(21,26),showfliers=False,patch_artist=True,vert=False)    
for b, c in zip(bplot['boxes'], colors):
    b.set_alpha(0.6)
    b.set_edgecolor('k') # or try 'black'
    b.set_facecolor(c)
    b.set_linewidth(1)
for m,l in zip(Sim,range(6)):
    plt.scatter(dCO2c[l,:],np.arange(21,26),s=16,marker=m,c='black')


for i,j in zip(np.arange(0.5,27,8), np.arange(4.5,27,8)):
 	plt.axhspan(i,j,facecolor='gray', alpha=0.3) 
plt.yticks(np.arange(2.5,25,4),['NA', 'NP', 'CEP','SP','SAI','Global'],fontsize=9,fontweight='bold')
plt.xlabel(r'$ \bf \Delta$' 'pCO' r'$\bf _{2}=(pCO_{2LGM}-pCO_{2H})/A$' ' [ppm/m' r'$^{2}$' ']',color='black',fontsize=9, fontweight='bold')
plt.grid(axis='x',linestyle = '--')
plt.legend(handles=legend_elements, loc='upper right',fontsize=9, bbox_to_anchor=(1.25, 1.03))
plt.tick_params(axis='y', left = False)
plt.savefig('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Prueba_Figure6_Boxplot_Tabla2_2.png')