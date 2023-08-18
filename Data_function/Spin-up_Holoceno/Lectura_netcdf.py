from netCDF4 import Dataset as nc #this line imports the package we just installed
import numpy as np

file=nc('/media/natalia/DATA/Documentos/TesisI/SPIN/cgenie_output/worjh2.PO4Fe_Mahowald2006.SPIN/biogem/fields_biogem_2d.nc') # this line defines the file path of the file we are trying to read
Sol_Iron=file.variables['misc_sur_fFe'][:] # ":" takes all the data dimension from the file
Sol_Iron_median=np.mean(Sol_Iron,axis=0) # Median in 3D dimention
np.savetxt('/media/natalia/DATA/Documentos/TesisI/SPIN/Spin-up_Holoceno/biogem_force_flux_ocn_Fe_SUR_2.dat',Sol_Iron_median, fmt='%1.6e')

exit()
file_sig=np.genfromtxt('/media/natalia/DATA/Documentos/TesisI/SPIN/Spin-up_Holoceno/biogem_force_flux_sed_det_SUR.dat') # this line defines the file path of the file we are trying to read
file_sig=np.flip(file_sig,axis=0)

List = [['-START-OF-DATA-'] , [0.0,1.0],[999999.0,1.0],['-END-OF-DATA-']] 
#print(List) 
#np.savetxt('biogem_force_flux_ocn_Fe_sig.dat',List)
my_data_file = open('biogem_force_flux_ocn_Fe_sig.dat', "w")

for item in List:
	print(item)
	for i in item:
		print(i)
		item2=str(i)
		my_data_file.write(item2 + ' ')
	my_data_file.write('\n')
	#print(item)
#my_data_file.close()

#my_data_file.write(str(List))
#my_data_file.close()
