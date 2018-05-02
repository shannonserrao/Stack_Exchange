%# load dataset of 150 instances and 3 dimensions
X = csvread('StackOverflowCluster3FeatureV2.csv',1,0);
%X = meas(:,1:3);
[numInst,numDims] = size(X);

%# K-means clustering
%# (K: number of clusters, G: assigned groups, C: cluster centers)
A = [0];
B = [0];
for K=1:20
[G,C, sumd, D] = kmeans(X, K, 'distance','sqEuclidean', 'start','sample','MaxIter',1000);

%s = silhouette(X,G);

for k=1:size(D)
    A(k) = D(k,G(k))^2;
end
B(K) = mean(A);
end
sB = [NaN,0.747848693,0.721383951,0.66416434,0.69599961,0.696839242,0.674902457,0.691417483,0.735571537,0.719502996,0.748227586,0.745141763,0.710759917,0.728897048,0.753678593,0.713818963,0.773691004,0.629963338,0.780620106,NaN];
yyaxis left
x = linspace(1,20,20);
plot(x,B)
 ylabel('Mean Squared Distance')
yyaxis right
plot(x,sB)
xlabel('Number of Clusters'), ylabel('Mean Silhouette')