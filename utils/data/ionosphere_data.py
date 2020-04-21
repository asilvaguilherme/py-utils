import pandas as pd

def load_ionosphere():
    df = pd.read_csv("C:\\alves\\git\\py-utils\\data\\ionosphere.data",header=None)
    
    X = df.loc[:,list(range(34))].values
    y = df.loc[:,34].values.ravel()
    
    return X,y

if __name__ == "__main__":
    load_ionosphere()
    
# from 