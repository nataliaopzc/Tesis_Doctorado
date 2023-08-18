import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.io import loadmat
from matplotlib.patches import Patch
from matplotlib.lines import Line2D


MODEL=['Albani','Lambert','Takemura','Ohgaito','MIROC-ESM','MRI-CGCM3']
AREA={'NA':2.2040e+13,'NP':4.0931e+13,'CP': 1.4168e+13,'SP':4.4080e+13,'SA':6.9268e+13}

TIME=['LGM']#,'H']
REGION=['NA', 'NP','CP', 'SP', 'SA']
SOL=[0.3333, 0.6666,2,3]

colors = ['yellow', 'pink', 'green','blue','red']
Simbolos=['o','p','v','s','x','D']

Solubilityp=loadmat('/media/natalia/DATA/Tesis/Functions/Otros/Solubilityp.mat')
Solubilityp=np.array([Solubilityp['OUTp'][:,:,0]]) # DATOS LGM
Solubilityp=Solubilityp[0,0,:]
#print(Solubilityp.shape)


print(len(CO22))
plt.plot(Solubilityp,CO22,'*')
plt.show()