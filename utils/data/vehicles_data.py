import pandas as pd

def load_vehicles():
    
    df = pd.read_csv("..\\..\\data\\vehicle\\xaa.dat",header=None)
    

    nfiles = ["xab","xac","xad","xae","xaf","xag","xah","xai"]
    
    for nfile in nfiles:
        df2 = pd.read_csv("..\\..\\data\\vehicle\\"+nfile+".dat",header=None)
        
        df = pd.concat([df, df2], axis=0)
    
    X = df.loc[:,list(range(18))].values
    y = df.loc[:,18].values.ravel()
    
    return X,y

if __name__ == "__main__":
    load_vehicles()
    
# from 