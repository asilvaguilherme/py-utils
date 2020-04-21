import pandas as pd

def load():
    df = pd.read_csv("C:\\alves\\git\\py-utils\\data\\heart.dat",header=None)
    
    X = df.loc[:,list(range(13))].values
    y = df.loc[:,13].values.ravel()
    
    return X,y

if __name__ == "__main__":
    load()
    
# from http://archive.ics.uci.edu/ml/datasets/statlog+(heart)