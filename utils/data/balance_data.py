import pandas as pd

def load():
    df = pd.read_csv("C:\\alves\\git\\py-utils\\data\\balance-scale.data",header=None)
    
    X = df.loc[:,list(range(1,5))].values
    y = df.loc[:,0].values.ravel()
    
    return X,y

if __name__ == "__main__":
    load()