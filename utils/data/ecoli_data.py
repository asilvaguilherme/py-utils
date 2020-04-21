import pandas as pd

def load():
    df = pd.read_csv("C:\\alves\\git\\py-utils\\data\\ecoli.data",header=None)
    
    X = df.loc[:,list(range(1,8))].values
    y = df.loc[:,8].values.ravel()
    
    return X,y

if __name__ == "__main__":
    load()