import pandas as pd

def load_bridges():
    df = pd.read_csv("C:\\alves\\git\\py-utils\\data\\bridges.v2.data",header=None)
    
    X = df.loc[:,list(range(1,11))].values
    y = df.loc[:,12].values.ravel()
    
    return X,y

if __name__ == "__main__":
    load_bridges()
    
# https://archive.ics.uci.edu/ml/datasets/Pittsburgh+Bridges

# 1. IDENTIF / -- / -- / identifier of the examples
# 2. RIVER / n / A, M, O / --
# 3. LOCATION / n / 1 to 52 / --
# 4. ERECTED / c,n / 1818-1986 ; CRAFTS, EMERGING, MATURE, MODERN / --
# 5. PURPOSE / n / WALK, AQUEDUCT, RR, HIGHWAY / --
# 6. LENGTH / c,n / 804-4558 ; SHORT, MEDIUM, LONG / --
# 7. LANES / c,n / 1, 2, 4, 6 ; 1, 2, 4, 6 / --
# 8. CLEAR-G / n / N, G / --
# 9. T-OR-D / n / THROUGH, DECK / --
# 10. MATERIAL / n / WOOD, IRON, STEEL / --
# 11. SPAN / n / SHORT, MEDUIM, LONG / --
# 12. REL-L / n / S, S-F, F / --
# 13. TYPE / n / WOOD, SUSPEN, SIMPLE-T, ARCH, CANTILEV, CONT-T / --