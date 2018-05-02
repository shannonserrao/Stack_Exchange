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
sB = [NaN,0.747848692886006,0.721383951147475,0.664164340424336,0.695999610420893,0.696839241535856,0.674902457415862,0.691417482915390,0.735571536501700,0.719502996267280,0.748227586006462,0.745141763088071,0.710759917190287,0.728897047657760,0.753678593479020,0.713818963138387,0.773691003645735,0.629963338411259,0.780620105523224,NaN];
yyaxis left
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
x
B
plot(x,B)
 ylabel('Mean Squared Distance')
yyaxis right
plot(x,sB)
xlabel('Number of Clusters'), ylabel('Mean Silhouette')