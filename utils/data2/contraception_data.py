import pandas as pd

def load_contraception():
    df = pd.read_csv("C:\\alves\\git\\py-utils\\data\\contraception.data",header=None)
    
    X = df.loc[:,list(range(0,8))].values
    y = df.loc[:,9].values.ravel()
    
    return X,y

if __name__ == "__main__":
    load_contraception()
    
# https://archive.ics.uci.edu/ml/datasets/Contraceptive+Method+Choice

# 1. Wife's age (numerical)
# 2. Wife's education (categorical) 1=low, 2, 3, 4=high
# 3. Husband's education (categorical) 1=low, 2, 3, 4=high
# 4. Number of children ever born (numerical)
# 5. Wife's religion (binary) 0=Non-Islam, 1=Islam
# 6. Wife's now working? (binary) 0=Yes, 1=No
# 7. Husband's occupation (categorical) 1, 2, 3, 4
# 8. Standard-of-living index (categorical) 1=low, 2, 3, 4=high
# 9. Media exposure (binary) 0=Good, 1=Not good
# 10. Contraceptive method used (class attribute) 1=No-use, 2=Long-term, 3=Short-term