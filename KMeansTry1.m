%# load dataset of 150 instances and 3 dimensions
X = csvread('StackOverflowCluster3Feature.csv',1,0);
%X = meas(:,1:3);
[numInst,numDims] = size(X);

%# K-means clustering
%# (K: number of clusters, G: assigned groups, C: cluster centers)
K = 4;
[G,C] = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
%# show points and clusters (color-coded)
clr = lines(K);
figure, hold on
scatter3(X(:,1), X(:,2), X(:,3), 36, clr(G,:), 'Marker','.')
scatter3(C(:,1), C(:,2), C(:,3), 100, clr, 'Marker','o', 'LineWidth',3)
hold off
view(3), axis vis3d, box on, rotate3d on
xlabel('StackOverflowSatisfaction'), ylabel('StackOverflowFoundAnswer'), zlabel('StackOverflowCopiedCode')