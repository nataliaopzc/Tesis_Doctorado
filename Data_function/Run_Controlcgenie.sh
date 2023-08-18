#! /bin/bash


VAR=("Lambert" "Albani" "Ohgaito" "Takemura" "MIROC-ESM" "MRI-CGCM3")

#VAR2=("NP" "NA" "SP" "SA" "CP")

VAR3=("x0.3333" "x0.6666" "1" "x2" "x3")

VAR4=("LGM" "H")

backup_dir=$(date +'%H.%M.%S_%d_%m_%Y')

#RUN
RUN="/home/dropssweetie/cgenie.muffin/genie-main"

n=0; 
for i in {0..5} 
 do
  for k in {0..1}
  do
   for l in {0..4}
   do 
     n=`expr $n + 1`;
qsub -q dog.q -j y -o cgemie_log -V -S /bin/bash ./runmuffin.sh muffin.CB.worjh2.BASESFeTDTL /PRUEBA worjh2.PO4Fe${VAR[i]}_${VAR4[k]}_Sol_calculated_Dust_Control_${VAR3[l]} 10000 worjh2.PO4Fe${VAR[i]}H_calculated_Dust.SPIN
Time_sim=$(date +'%H.%M.%S_%d_%m_%Y')
echo "qsub -q dog.q -j y -o cgemie_log -V -S /bin/bash ./runmuffin.sh muffin.CB.worjh2.BASESFeTDTL /PRUEBA worjh2.PO4Fe${VAR[i]}_${VAR4[k]}_Sol_calculated_Dust_Control_${VAR3[l]} 10000 worjh2.PO4Fe${VAR[i]}H_calculated_Dust.SPIN    ${Time_sim}   $n" >> Run_historial_${backup_dir}.dat
sleep 60
     if (($n % 12 == 0 ))
then      
sleep 90000
     fi
   done
  done
done

