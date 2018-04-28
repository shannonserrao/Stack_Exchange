%# load dataset of 150 instances and 3 dimensions
X = csvread('StackOverflowCluster9Feature.csv',1,0);
%X = meas(:,1:3);
[numInst,numDims] = size(X);

%# K-means clustering
%# (K: number of clusters, G: assigned groups, C: cluster centers)

K = 2;
[G,C] = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
tabulate(G)
C
cidx = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
s = silhouette(X,cidx);
mean(s)

K = 3;
[G,C] = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
tabulate(G)
C
cidx = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
s = silhouette(X,cidx);
mean(s)

K = 4;
[G,C] = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
tabulate(G)
C
cidx = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
s = silhouette(X,cidx);
mean(s)

K = 5;
[G,C] = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
tabulate(G)
C
cidx = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
s = silhouette(X,cidx);
mean(s)

K = 6;
[G,C] = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
tabulate(G)
C
cidx = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
s = silhouette(X,cidx);
mean(s)

K = 7;
[G,C] = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
tabulate(G)
C
cidx = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
s = silhouette(X,cidx);
mean(s)

K = 8;
[G,C] = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
tabulate(G)
C
cidx = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
s = silhouette(X,cidx);
mean(s)

K = 9;
[G,C] = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
tabulate(G)
C
cidx = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
s = silhouette(X,cidx);
mean(s)

K = 10;
[G,C] = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
tabulate(G)
C
cidx = kmeans(X, K, 'distance','sqEuclidean', 'start','sample');
s = silhouette(X,cidx);
mean(s)

