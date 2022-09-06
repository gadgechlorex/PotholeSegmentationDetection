% Performance Analysis
% Segmentation Accuracy
% imgt -- Ground Truth -Gray Scale Image
% immask -- segmeted mask - Gray Scale Image

clc;
clear all;
close all;
warning off;

% dr1=dir('*.jpg');
% dr=dir('*.bmp');
fprintf('SEGMENTATION ACCURACY\n\n\n\n\n');
imgt='watershed278.jpg';
immask='278Mask.jpg';
f1=im2bw(imread(imgt),0.5);
[ro co ]=size(f1);
f2=im2bw(imread(immask),0.5);
[ro1 co1 ]=size(f2);

if (ro==ro1) && (co==co1)
TP=0;
TN=0;
FN=0;
FP=0;
for i=1:ro
    for j=1:co
        if f1(i,j)==1 && f2(i,j)==1 
            TP=TP+1;
        elseif f1(i,j)==0 && f2(i,j)==0 
            TN=TN+1;
        elseif f1(i,j)==1 && f2(i,j)==0 
            FP=FP+1;
        elseif f1(i,j)==0 && f2(i,j)==1
            FN=FN+1;
        end
    end
end



Accuracy =(TN+TP)/(TN+TP+FN+FP);
Specificity =(TN)/(TN+FP);
Sensitivity =(TP)/(TP+FN);
Precision = (TP)/(TP+FP);
fprintf('Accuracy ----> %f%%\n',Accuracy*100);
fprintf('Sensitivity ----> %f%%\n',Sensitivity*100);
fprintf('Specificity ----> %f%%\n',Specificity*100);
fprintf('Precision ----> %f%%\n',Precision*100);
else 
    disp('Dimension Error\n')
end
