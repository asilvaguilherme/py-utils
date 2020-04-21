import pandas as pd

def load_mushrooms():
    df = pd.read_csv("C:\\alves\\git\\py-utils\\data\\mushrooms.data",header=None)
    
    X = df.loc[:,list(range(1,22))].values
    y = df.loc[:,0].values.ravel()
    
    return X,y

if __name__ == "__main__":
    load_mushrooms()
    
