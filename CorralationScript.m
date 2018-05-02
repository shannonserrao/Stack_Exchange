%# load dataset of 150 instances and 3 dimensions
dataTable = readtable('SOCluster17FeatureSmallAlter.csv');
label = dataTable(:,1);
X = dataTable(:,2:end);
%X = meas(:,1:3);
[numInst,numDims] = size(X);
X.Properties.VariableNames = {'var 3', 'var 4', 'var 5', 'var 6','var 7','var 8','var 9','var 10','var 11','var 12','var 13','var 14','var 15','var 16','var 17','var 18','var 19'};
corrplot(X)

