
H=xlsread('cgenie_output_Global_H.xlsx','B2:F7'); %H=reshape(H,[30 1]);
LGM=xlsread('cgenie_output_Global_LGM.xlsx','B2:F7');
x=[0.333 0.6666 1 2 3];%x=repmat(x,[6,1]);x=reshape(x,[30 1]);
Hm=median(H);
LGMm=median(LGM);

myfittype = fittype('(a/(x-c)) +b',...
    'dependent',{'y'},'independent',{'x'},...
    'coefficients',{'a','b','c'})

[fitobject,gof,output] = fit(x',Hm',myfittype); 
[fitobject2,gof2,output2] = fit(x',LGMm',myfittype,'StartPoint',[1 210 0]);
coef=coeffvalues(fitobject);
coef2=coeffvalues(fitobject2);
xx=linspace(0,9);
yy=(coef(1)./(xx-coef(3)))+coef(2);
yy2=(coef2(1)./(xx-coef2(3)))+coef2(2);
plot(xx,yy)
hold on 
plot(x,Hm,'*')
plot(xx,yy2)
plot(x,LGMm,'*')



