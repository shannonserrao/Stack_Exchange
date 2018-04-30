%# load dataset of 150 instances and 3 dimensions
dataTable = readtable('StackOverflowCluster17Feature.csv');
label = dataTable(:,1);
X = dataTable(:,2:end);
%X = meas(:,1:3);
[numInst,numDims] = size(X);

corrplot(X)

