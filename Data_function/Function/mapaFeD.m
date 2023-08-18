A=readtable('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/IDP2021_GEOTRACES_IDP2021_FeD.csv');
i=find((A.Var18<=10)==1); % Posiciones de valores de profundidad menores o igual a 10
A=A(i,:);
FeDp=find(~isnan(A.Var20)); % Encontrar las posiciones no Nan
A=A(FeDp,:);
FeDp=find(A.Var20~=0); %Encontrar las posiciones no cero. 
A=A(FeDp,:);
geoscatter(A.Var6,(A.Var5-360),log10(A.Var20),'*') % lat, lon, variable
colorbarforma
clear FeDp i 
%[X,Y,Z]=meshgrid((A.Var5-180),A.Var6,A.Var20); %long, lat, FeD
LFeD=str2double(readcell('/home/natalia/Documentos/DATA/TesisI/Data_function/Function/Lambert_H.dat'));
lon=ncread('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/worjh2.PO4FeLambertH_calculated_Dust/biogem/fields_biogem_2d.nc','lon');
lat=ncread('/home/natalia/Documentos/DATA/TesisI/cgenie/cgenie_output/worjh2.PO4FeLambertH_calculated_Dust/biogem/fields_biogem_2d.nc','lat');
[X,Y]=meshgrid(lon,lat);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


