#import  tarfile
import numpy as np
import matplotlib.pyplot as plt

#f = open('prueba.tar', 'rb')
#print (f)
#tar = tarfile.open(fileobj=f, mode='r:') # Unpack tar
#for item in tar:
#    print(item)

AREA={'NA':2.2040e+13,'NP':   4.0931e+13,'CP': 1.4168e+13,'SP':4.4080e+13,'SA':6.9268e+13}

TIME=['H', 'LGM']
REGION=['NA', 'NP', 'CP', 'SP', 'SA']
SOL=[0.3333, 0.6666,2,3]


for i in TIME: # es lo mismo que for i in range(len(list)): print(list[i])
	plt.figure(i+'1')
	for j in REGION:
		CO2=[]
		for k in SOL:
			CO2_file=np.genfromtxt('/media/natalia/DATA/Documentos/TesisI/cgenie/cgenie_output/worjh2.PO4FeLambert_'+i+'_Sol_calculated_Dust_'+j+'_x'+str(k)+'/biogem/biogem_series_atm_pCO2.res',comments="%")
			CO2.append(np.median(CO2_file[-100:,2]*1e+6))
		plt.plot(SOL,CO2,'-*')
		plt.title(i+' pCO2 v/s Iron solubility scale')
		plt.xlabel('Iron solubility scale')
		plt.ylabel('Atmospheric CO2 [ppm]')
	plt.legend(REGION)

for i in TIME: # es lo mismo que for i in range(len(list)): print(list[i])
	plt.figure(i+'2')
	for j in REGION:
		CO2=[]
		for k in SOL:
			CO2_or=np.genfromtxt('/media/natalia/DATA/Documentos/TesisI/cgenie/cgenie_output/worjh2.PO4FeLambertH_calculated_Dust/biogem/biogem_series_atm_pCO2.res',comments="%")
			CO2_file=np.genfromtxt('/media/natalia/DATA/Documentos/TesisI/cgenie/cgenie_output/worjh2.PO4FeLambert_'+i+'_Sol_calculated_Dust_'+j+'_x'+str(k)+'/biogem/biogem_series_atm_pCO2.res',comments="%")
			CO2.append((np.median(CO2_or[-100:,2]-np.median(CO2_file[-100:,2])))*1e+6)
		plt.plot(SOL,CO2,'-*')
		plt.title(i+' pCO2 difference v/s Iron solubility scale')
		plt.xlabel('Iron solubility scale')
		plt.ylabel('Atmospheric CO2 [ppm]')
	plt.legend(REGION)

for i in TIME: # es lo mismo que for i in range(len(list)): print(list[i])
	plt.figure(i+'3')
	for j in REGION:
		CO2=[]
		for k in SOL:
		    CO2_or=np.genfromtxt('/media/natalia/DATA/Documentos/TesisI/cgenie/cgenie_output/worjh2.PO4FeLambertH_calculated_Dust/biogem/biogem_series_atm_pCO2.res',comments="%")
		    CO2_file=np.genfromtxt('/media/natalia/DATA/Documentos/TesisI/cgenie/cgenie_output/worjh2.PO4FeLambert_'+i+'_Sol_calculated_Dust_'+j+'_x'+str(k)+'/biogem/biogem_series_atm_pCO2.res',comments="%")
		    CO2.append((np.median(CO2_or[-100:,2]-np.median(CO2_file[-100:,2])))*1e+6/AREA[j])
		plt.plot(SOL,CO2,'-*')
		plt.title(i+' pCO2 difference per m2 v/s Iron solubility scale')
		plt.xlabel('Iron solubility scale')
		plt.ylabel('Atmospheric CO2 [ppm/m2]')
	plt.legend(REGION)

plt.show()


