%# load dataset of 150 instances and 3 dimensions
X = csvread('StackOverflowCluster3Feature.csv',1,0);
%X = meas(:,1:3);
[numInst,numDims] = size(X);

%# K-means clustering
%# (K: number of clusters, G: assigned groups, C: cluster centers)
A = [0];
B = [0];
for K=1:40
[G,C, sumd, D] = kmeans(X, K, 'distance','sqEuclidean', 'start','sample','MaxIter',1000);

%s = silhouette(X,G);

for k=1:size(D)
    A(k) = D(k,G(k))^2;
end
B(K) = mean(A);
end
sB = [NaN,0.505682543,0.465752631,0.45169003,0.445200082,0.461519792,0.437763978,0.397513959,0.443268719,0.434389687,0.428747402,0.51667781,0.463651386,0.46784453,0.462640898,0.508668456,0.372088112,0.431438718,0.545423659,0.431418243,0.431111896,0.541897151,0.572535143,0.587685504,0.52369741,0.530113887,0.505859225,0.530121908,0.567797771,0.500925005,0.511152057,0.563621614,0.58139313,0.586606323,0.592460037,0.497085058,0.643573178,0.581927927,0.536950287,0.587974068];
yyaxis left
x = linspace(1,40,40);
plot(x,B)
 ylabel('Mean Squared Distance')
yyaxis right
plot(x,sB)
xlabel('Number of Clusters'), ylabel('Mean Silhouette')