import pandas as pd

def load_lenses():
    df = pd.read_csv("C:\\alves\\git\\py-utils\\data\\lenses.data",header=None)
    
    X = df.loc[:,list(range(1,4))].values
    y = df.loc[:,5].values.ravel()
    
    return X,y

if __name__ == "__main__":
    load_lenses()
