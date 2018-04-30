%# load dataset of 150 instances and 3 dimensions
X = csvread('StackOverflowCluster3Feature.csv',1,0);
%X = meas(:,1:3);
[numInst,numDims] = size(X);

%# K-means clustering
%# (K: number of clusters, G: assigned groups, C: cluster centers)
A = [0];
B = [0];
for K=1:100
[G,C, sumd, D] = kmeans(X, K, 'distance','sqEuclidean', 'start','sample','MaxIter',1000);

%s = silhouette(X,G);
%mean(s)
for k=1:size(D)
    A(k) = D(k,G(k))^2;
end
B(K) = mean(A);
end
B
plot(B)
xlabel('Number of Clusters'), ylabel('Mean Squared Distance from Centroid')