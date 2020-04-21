import pandas as pd

def load_thoracic():
    df = pd.read_csv("C:\\alves\\git\\py-utils\\data\\thoraric-surgery.data",header=None)
    
    X = df.loc[:,list(range(0,15))].values
    y = df.loc[:,16].values.ravel()
    
    return X,y

if __name__ == "__main__":
    load_thoracic()
    
# https://archive.ics.uci.edu/ml/datasets/Thoracic+Surgery+Data

# 1. DGN: Diagnosis - specific combination of ICD-10 codes for primary and secondary as well multiple tumours if any (DGN3,DGN2,DGN4,DGN6,DGN5,DGN8,DGN1)
# 2. PRE4: Forced vital capacity - FVC (numeric)
# 3. PRE5: Volume that has been exhaled at the end of the first second of forced expiration - FEV1 (numeric)
# 4. PRE6: Performance status - Zubrod scale (PRZ2,PRZ1,PRZ0)
# 5. PRE7: Pain before surgery (T,F)
# 6. PRE8: Haemoptysis before surgery (T,F)
# 7. PRE9: Dyspnoea before surgery (T,F)
# 8. PRE10: Cough before surgery (T,F)
# 9. PRE11: Weakness before surgery (T,F)
# 10. PRE14: T in clinical TNM - size of the original tumour, from OC11 (smallest) to OC14 (largest) (OC11,OC14,OC12,OC13)
# 11. PRE17: Type 2 DM - diabetes mellitus (T,F)
# 12. PRE19: MI up to 6 months (T,F)
# 13. PRE25: PAD - peripheral arterial diseases (T,F)
# 14. PRE30: Smoking (T,F)
# 15. PRE32: Asthma (T,F)
# 16. AGE: Age at surgery (numeric)
# 17. Risk1Y: 1 year survival period - (T)rue value if died (T,F)

# Class Distribution: the class value (Risk1Y) is binary valued.
# Risk1Y Value: Number of Instances:
# T 70
# N 400