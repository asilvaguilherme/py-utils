import pandas as pd

def load():
    df = pd.read_csv("C:\\alves\\git\\py-utils\\data\\glass.data",header=None)
    
    X = df.loc[:,list(range(0,10))].values
    y = df.loc[:,10].values.ravel()
    
    return X,y

if __name__ == "__main__":
    load()
    
