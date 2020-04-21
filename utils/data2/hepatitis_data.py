import pandas as pd

def load_hepatitis():
    df = pd.read_csv("C:\\alves\\git\\py-utils\\data\\hepatitis.data",header=None)
    
    X = df.loc[:,list(range(1,19))].values
    y = df.loc[:,0].values.ravel()
    
    return X,y

if __name__ == "__main__":
    load_hepatitis()
    
# https://archive.ics.uci.edu/ml/datasets/Hepatitis
 
# 1. Class: DIE, LIVE
# 2. AGE: 10, 20, 30, 40, 50, 60, 70, 80
# 3. SEX: male, female
# 4. STEROID: no, yes
# 5. ANTIVIRALS: no, yes
# 6. FATIGUE: no, yes
# 7. MALAISE: no, yes
# 8. ANOREXIA: no, yes
# 9. LIVER BIG: no, yes
# 10. LIVER FIRM: no, yes
# 11. SPLEEN PALPABLE: no, yes
# 12. SPIDERS: no, yes
# 13. ASCITES: no, yes
# 14. VARICES: no, yes
# 15. BILIRUBIN: 0.39, 0.80, 1.20, 2.00, 3.00, 4.00
# -- see the note below
# 16. ALK PHOSPHATE: 33, 80, 120, 160, 200, 250
# 17. SGOT: 13, 100, 200, 300, 400, 500,
# 18. ALBUMIN: 2.1, 3.0, 3.8, 4.5, 5.0, 6.0
# 19. PROTIME: 10, 20, 30, 40, 50, 60, 70, 80, 90
# 20. HISTOLOGY: no, yes