#import  tarfile
import numpy as np
import matplotlib.pyplot as plt

#f = open('prueba.tar', 'rb')
#print (f)
#tar = tarfile.open(fileobj=f, mode='r:') # Unpack tar
#for item in tar:
#    print(item)

AREA={'NA':2.2040e+13,'NP':4.0931e+13,'CP': 1.4168e+13,'SP':4.4080e+13,'SA':6.9268e+13}

MODEL=['Ohgaito']
TIME=['H', 'LGM']
REGION=['NA', 'NP', 'CP', 'SP', 'SA']
SOL=[0.3333, 0.6666,2,3]

fig, axs = plt.subplots(2, 3)
ii=0;
for i in TIME: # es lo mismo que for i in range(len(list)): print(list[i])
	#plt.figure(i+'1')
	for j in REGION:
		CO2=[]
		for k in SOL:
			for l in MODEL:
				CO2_file=np.genfromtxt('/media/natalia/DATA/Documentos/TesisI/cgenie/cgenie_output/worjh2.PO4Fe'+l+'_'+i+'_Sol_calculated_Dust_'+j+'_x'+str(k)+'/biogem/biogem_series_atm_pCO2.res',comments="%")
				CO2.append(np.median(CO2_file[-100:,2]*1e+6))
		axs[ii,0].plot(SOL,CO2,'-*')
		axs[ii,0].set_title(i+' pCO2 v/s Iron solubility scale')
		axs[ii,0].set_xlabel('Iron solubility scale')
		axs[ii,0].set_ylabel('Atmospheric CO2 [ppm]')
	axs[ii,0].legend(REGION)
	ii+=1

ii=0;
for i in TIME: # es lo mismo que for i in range(len(list)): print(list[i])
	#plt.figure(i+'2')
	for j in REGION:
		CO2=[]
		for k in SOL:
			for l in MODEL:
				CO2_or=np.genfromtxt('/media/natalia/DATA/Tesis/Cgenie_output/Globales/'+l+'/worjh2.PO4Fe.All.'+l+'.level1/biogem/biogem_series_atm_pCO2.res',comments="%")
				CO2_file=np.genfromtxt('/media/natalia/DATA/Documentos/TesisI/cgenie/cgenie_output/worjh2.PO4Fe'+l+'_'+i+'_Sol_calculated_Dust_'+j+'_x'+str(k)+'/biogem/biogem_series_atm_pCO2.res',comments="%")
				CO2.append((np.median(CO2_or[-100:,2]-np.median(CO2_file[-100:,2])))*1e+6)
		axs[ii,1].plot(SOL,CO2,'-*')
		axs[ii,1].set_title(i+' pCO2 difference v/s Iron solubility scale')
		axs[ii,1].set_xlabel('Iron solubility scale')
		axs[ii,1].set_ylabel('Atmospheric CO2 [ppm]')
	axs[ii,1].legend(REGION)
	ii+=1

ii=0;
for i in TIME: # es lo mismo que for i in range(len(list)): print(list[i])
	#plt.figure(i+'3')
	for j in REGION:
		CO2=[]
		for k in SOL:
			for l in MODEL:
			    CO2_or=np.genfromtxt('/media/natalia/DATA/Tesis/Cgenie_output/Globales/'+l+'/worjh2.PO4Fe.All.'+l+'.level1/biogem/biogem_series_atm_pCO2.res',comments="%")
			    CO2_file=np.genfromtxt('/media/natalia/DATA/Documentos/TesisI/cgenie/cgenie_output/worjh2.PO4Fe'+l+'_'+i+'_Sol_calculated_Dust_'+j+'_x'+str(k)+'/biogem/biogem_series_atm_pCO2.res',comments="%")
			    CO2.append((np.median(CO2_or[-100:,2]-np.median(CO2_file[-100:,2])))*1e+6/AREA[j])
		axs[ii,2].plot(SOL,CO2,'-*')
		axs[ii,2].set_title(i+' pCO2 difference per m2 v/s Iron solubility scale')
		axs[ii,2].set_xlabel('Iron solubility scale')
		axs[ii,2].set_ylabel('Atmospheric CO2 [ppm/m2]')
	axs[ii,2].legend(REGION)
	ii+=1

plt.show()
