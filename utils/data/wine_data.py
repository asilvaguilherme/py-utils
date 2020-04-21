from sklearn import datasets

def load():
    wine = datasets.load_wine()
    X = wine.data[:,:]  
    y = wine.target
    
    return X,y

if __name__ == "__main__":
    load()