'''
Created on 31 oct. 2019

@author: galvesda
'''

import numpy as np

def algos(partition,n):
    
    labels = np.zeros((n))
    for i in range(len(partition)):
        group = partition[i]
        for j in group:
            labels[j] = i
            
    return labels
