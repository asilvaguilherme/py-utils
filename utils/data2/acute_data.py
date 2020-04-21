import pandas as pd

def load_acute_inf():
    df = pd.read_csv("C:\\alves\\git\\py-utils\\data\\acute_inflamations.data",header=None)
    
    X = df.loc[:,list(range(0,6))].values
    y = df.loc[:,7].values.ravel()
    
    return X,y

if __name__ == "__main__":
    load_acute_inf()
    
# https://archive.ics.uci.edu/ml/datasets/Acute+Inflammations

# a1 Temperature of patient { 35C-42C }
# a2 Occurrence of nausea { yes, no }
# a3 Lumbar pain { yes, no }
# a4 Urine pushing (continuous need for urination) { yes, no }
# a5 Micturition pains { yes, no }
# a6 Burning of urethra, itch, swelling of urethra outlet { yes, no }
# d1 decision: Inflammation of urinary bladder { yes, no }
# d2 decision: Nephritis of renal pelvis origin { yes, no }