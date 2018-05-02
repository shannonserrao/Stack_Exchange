%# load dataset of 150 instances and 3 dimensions
X = csvread('StackOverflowCluster17Feature.csv',1,0);
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
sB = [NaN,0.226133278,0.198474662,0.188043939,0.127930984,0.133663111,0.118502039,0.117876895,0.116838497,0.109177456,0.116376852,0.110153474,0.106809823,0.109731439,0.108526258,0.094650208,0.099117195,0.095895752,0.095735137,0.096098975,0.095362676,0.094073866,0.09088907,0.091397291,0.087407746,0.088938579,0.0916634,0.089870485,0.091622034,0.087462888,0.08410213,0.084719334,0.086508954,0.083183751,0.089567793,0.082169364,0.081702229,0.085184066,0.08297394,0.089237622];
yyaxis left
x = linspace(1,40,40);
plot(x,B)
 ylabel('Mean Squared Distance')
yyaxis right
plot(x,sB)
xlabel('Number of Clusters'), ylabel('Mean Silhouette')