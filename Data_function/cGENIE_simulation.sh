#! /bin/bash

VAR=("Lambert" "Albani" "Ohgaito" "Takemura" "MIROC-ESM" "MRI-CGCM3")

VAR2=("NP" "NA" "SP" "SA" "CP")

VAR3=("x0.3333" "x0.6666" "x2" "x3")

VAR4=("LGM" "H")

FORCINGC="/home/ffwng/cgenie.muffin/genie-forcings"
FORCING="/media/natalia/DATA/Documentos/TesisI/cgenie/genie-forcings"
USERCONFIGC="/home/ffwng/cgenie.muffin/genie-userconfigs/PRUEBA"
USERCONFIG="/media/natalia/DATA/Documentos/TesisI/cgenie/genie-userconfigs"
SOLUBILITYC="/home/ffwng/cgenie.muffin/genie-biogem/data/input"
DUST="/media/natalia/DATA/Tesis/Flujos_de_polvo/Globales_Moles"
SOLUBILITY="/media/natalia/DATA/Documentos/TesisI/cgenie/Solubility/Region"
RUN="/home/ffwng/cgenie.muffin/genie-main"

for i in {0..5..1} 
do
 for j in {0..4..1}
 do
  for k in {0..1..1}
  do
   for l in {0..3..1}
   do 
#mkdir -p $FORCING/"worjh2.Fe${VAR[i]}_${VAR4[k]}_Sol_calculated_Dust_${VAR2[j]}_${VAR3[l]}"
#scp -r ffwng@domino.ucr.edu:$FORCINGC/worjh2.FeMRI-CGCM3H_Dust/* $FORCING/"worjh2.Fe${VAR[i]}_${VAR4[k]}_Sol_calculated_Dust_${VAR2[j]}_${VAR3[l]}"
#rm $FORCING/"worjh2.Fe${VAR[i]}_${VAR4[k]}_Sol_calculated_Dust_${VAR2[j]}_${VAR3[l]}"/biogem_force_flux_sed_det_SUR.dat
    if [$k = 0]
     then 
cp $DUST/${VAR[i]}/"${VAR[i]}.nc_annualflux_molperyr.36x36_level10.dat" $FORCING/"worjh2.Fe${VAR[i]}_${VAR4[k]}_Sol_calculated_Dust_${VAR2[j]}_${VAR3[l]}"/biogem_force_flux_sed_det_SUR.dat
#cp $DUST/${VAR[i]}/"${VAR[i]}_${VAR2[j]}_${VAR4[k]}.dat" $FORCING/"worjh2.Fe${VAR[i]}_${VAR4[k]}_Sol_calculated_Dust_${VAR2[j]}_${VAR3[l]}"/biogem_force_flux_sed_det_SUR.dat
     else 
cp $DUST/${VAR[i]}/"${VAR[i]}.nc_annualflux_molperyr.36x36_level1.dat" $FORCING/"worjh2.Fe${VAR[i]}_${VAR4[k]}_Sol_calculated_Dust_${VAR2[j]}_${VAR3[l]}"/biogem_force_flux_sed_det_SUR.dat
    fi 
scp -r $FORCING/"worjh2.Fe${VAR[i]}_${VAR4[k]}_Sol_calculated_Dust_${VAR2[j]}_${VAR3[l]}" ffwng@domino.ucr.edu:$FORCINGC

#scp $SOLUBILITY/"worjh2.det_Fe_Sol_calculated.${VAR[i]}_${VAR4[k]}_${VAR2[j]}_${VAR3[l]}.dat" ffwng@domino.ucr.edu:$SOLUBILITYC

#cp $USERCONFIG/worjh2.PO4FeAlbaniLGM_calculated_Dust $USERCONFIG/"worjh2.PO4Fe${VAR[i]}_${VAR4[k]}_Sol_calculated_Dust_${VAR2[j]}_${VAR3[l]}"
#sed -i "s/worjh2.det_Fe_sol.Albani_LGM.dat/"worjh2.det_Fe_Sol_calculated.${VAR[i]}_${VAR4[k]}_${VAR2[j]}_${VAR3[l]}.dat"/g;s/worjh2.FeAlbaniLGM_Dust/"worjh2.Fe${VAR[i]}_${VAR4[k]}_Sol_calculated_Dust_${VAR2[j]}_${VAR3[l]}"/g" "$USERCONFIG/"worjh2.PO4Fe${VAR[i]}_${VAR4[k]}_Sol_calculated_Dust_${VAR2[j]}_${VAR3[l]}""
#scp $USERCONFIG/"worjh2.PO4Fe${VAR[i]}_${VAR4[k]}_Sol_calculated_Dust_${VAR2[j]}_${VAR3[l]}" ffwng@domino.ucr.edu:$USERCONFIGC
   done
  done
 done
done 






