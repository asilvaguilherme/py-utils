from sklearn.neighbors.unsupervised import NearestNeighbors


def rvalue(X, Y, n_neighbors=10, theta=1):
    
    neigh = NearestNeighbors(n_neighbors=n_neighbors).fit(X)
    
    sum = 0
    
    for i in range(len(X)):
        _, [indices] = neigh.kneighbors([X[i]])
        
        diff = [Y[index] for index in indices if Y[index] != Y[i]]
        
        if len(diff) > theta:
            sum += 1
    
    return sum / len(X)
