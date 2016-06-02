from sklearn.cluster import KMeans
reg = KMeans(n_clusters = 2)

x = [[1,1],[1,0],[1,2],[2,2],[5,5],[5,6],[5,4],[6,6]]
reg.fit(x)

print reg.predict([0,0])
print reg.predict([-1,0])
print reg.predict([7,7])
print reg.predict([4,7])
