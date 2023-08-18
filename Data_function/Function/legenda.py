#import  tarfile
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], linestyle='',label='REGION'),
Line2D([0], [0], marker='o', color='yellow', linestyle='',lw=4, label='NA'),
Line2D([0], [0],  marker='o',color='pink', linestyle='',lw=3, label='NP'),
Line2D([0], [0], marker='o', color='green', linestyle='',lw=3, label='CEP'),
Line2D([0], [0],  marker='o',color='blue', linestyle='',lw=3, label='SP'),
Line2D([0], [0],  marker='o',color='red', linestyle='',lw=3, label='SAI'),
Line2D([0], [0], linestyle='',label='DUST SOURCE'),
Line2D([0], [0],  marker='o',color='black', linestyle='',lw=3, label='Albani'),
Line2D([0], [0],  marker='p',color='black', linestyle='',lw=3, label='Lambert'),
Line2D([0], [0],  marker='v',color='black', linestyle='',lw=3, label='Takemura'),
Line2D([0], [0],  marker='s',color='black', linestyle='',lw=3, label='Ohgaito'),
Line2D([0], [0],  marker='X',color='black', linestyle='',lw=3, label='MIROC-ESM'),
Line2D([0], [0],  marker='D',color='black', linestyle='',lw=3, label='MRI-CGCM3'),
Line2D([0], [0], linestyle='',label='FACTOR'),
Line2D([0], [0],  marker='o',color='black', linestyle='',markersize=2, label='0.3'),
Line2D([0], [0],  marker='o',color='black', linestyle='',markersize=5, label='0.6'),
Line2D([0], [0],  marker='o',color='black', linestyle='',markersize=12, label='2'),
Line2D([0], [0],  marker='o',color='black', linestyle='',markersize=18, label='3'),
]

plt.legend(handles=legend_elements)
plt.show()