%# load dataset of 150 instances and 3 dimensions
dataTable = readtable('SOCluster17FeatureSmallAlter.csv');
label = dataTable(:,1);

dataTable.Properties.VariableNames = {'Var3' 'Var4' 'Var5' 'Var6' 'Var7' 'Var8' 'Var9' 'Var10' 'Var11' 'Var12' 'Var13' 'Var14' 'Var15' 'Var16' 'Var17' 'Var18' 'Var19'};
X = dataTable(:,2:end);
%X = meas(:,1:3);
[numInst,numDims] = size(X);

corrplot(dataTable)

