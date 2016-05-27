from sklearn.neighbors import NearestNeighbors

X = [[0., 0., 0.],
     [0., .5, 0.],
     [1., 1., .5]]

neigh = NearestNeighbors(n_neighbors=1)
neigh.fit(X)
A = neigh.kneighbors([[1., 1., 1.]])
print A