import pandas as pd

def load_dermatology():
    df = pd.read_csv("C:\\alves\\git\\py-utils\\data\\soybean-small.data",header=None)
    
    X = df.loc[:,list(range(1,34))].values
    y = df.loc[:,35].values.ravel()
    
    return X,y

if __name__ == "__main__":
    load_dermatology()
    
# used in the papers

# A matching based clustering algorithm for categorical data
# https://arxiv.org/pdf/1812.03469.pdf