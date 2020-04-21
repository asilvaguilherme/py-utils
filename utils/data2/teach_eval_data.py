import pandas as pd

def load_teach_eval():
    df = pd.read_csv("C:\\alves\\git\\py-utils\\data\\teaching_assist_eval.data",header=None)
    
    X = df.loc[:,list(range(0,4))].values
    y = df.loc[:,5].values.ravel()
    
    return X,y

if __name__ == "__main__":
    load_teach_eval()
    
# https://archive.ics.uci.edu/ml/datasets/Teaching+Assistant+Evaluation

# 1. Whether of not the TA is a native English speaker (binary); 1=English speaker, 2=non-English speaker
# 2. Course instructor (categorical, 25 categories)
# 3. Course (categorical, 26 categories)
# 4. Summer or regular semester (binary) 1=Summer, 2=Regular
# 5. Class size (numerical)
# 6. Class attribute (categorical) 1=Low, 2=Medium, 3=High