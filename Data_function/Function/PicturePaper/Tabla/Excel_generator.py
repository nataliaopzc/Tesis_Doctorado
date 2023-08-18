import csv
import pandas as pd
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

MODEL=['Albani','Lambert','Takemura','Ohgaito','MIROC-ESM','MRI-CGCM3']
TIME=['H','LGM']
SOL=[0.3333, 0.6666,1,2,3]

for t in TIME:
    CO2=np.zeros((6,5))
    for h, i in zip(MODEL,range(6)):
        for j, k in zip(SOL,range(5)):
            CO2_file=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/Global/'+h+'/worjh2.PO4Fe'+h+'_'+t+'_Sol_calculated_Dust_Control_x'+str(j)+'/biogem/biogem_series_atm_pCO2.res',comments="%")
            CO2_1=CO2_file[-10:,2]*1e+6
            CO2[i,k]=np.median(CO2_1,axis=0)
            print(i,k,CO2)
    df22 = pd.DataFrame(CO2,columns=SOL,index=MODEL)
    df22.to_excel('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Tabla/cgenie_output_Global_'+t+'.xlsx')
    
REGION=['NA', 'NP','CP', 'SP', 'SA']
SOL=[0.3333, 0.6666,2,3]    
for t in TIME:
    CO2=np.zeros((6,4))
    for r in REGION:
        for h, i in zip(MODEL,range(6)):
            for j, k in zip(SOL,range(4)):
                CO2_file=np.genfromtxt('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/Regional/'+h+'/worjh2.PO4Fe'+h+'_'+t+'_Sol_calculated_Dust_'+r+'_x'+str(j)+'/biogem/biogem_series_atm_pCO2.res',comments="%")
                CO2_1=CO2_file[-10:,2]*1e+6
                CO2[i,k]=np.median(CO2_1,axis=0)
                print(i,k,CO2)
        df22 = pd.DataFrame(CO2,columns=SOL,index=MODEL)
        df22.to_excel('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/PicturePaper/Tabla/cgenie_output_Regional_'+t+'_'+r+'.xlsx')    
            