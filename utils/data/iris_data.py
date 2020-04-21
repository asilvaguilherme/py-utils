from sklearn import datasets

def load():
    iris = datasets.load_iris()
    X = iris.data[:,:]  
    y = iris.target
    
    return X,y

if __name__ == "__main__":
    load()