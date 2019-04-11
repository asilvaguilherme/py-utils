import math
import os
import random

import numpy as np
import pandas as pd


def load_data(filename):
    
    data = pd.read_csv(filename, sep=',',header=None)
    instances = data.values
    
    total_num_instances = np.size(instances,0)
    class_index = num_attrib = np.size(instances,1) - 1
    
    X = instances[:,0:num_attrib]
    Y = instances[:,class_index ]
    
    indices = [i for i in range(total_num_instances)]
    random.shuffle(indices)
       
    shuffled_X = X[indices]
    shuffled_Y = (Y[indices])[:,].flatten().tolist()
    
    return len(set(Y)), shuffled_X, shuffled_Y


class Loader:
    
    def __init__(self, filepath, reduction_rate=None):
        
        self.filepath = filepath
        self.files_list = []
        self.next = 0
        
        for root,_,files in os.walk(filepath):
            for file in files:
                if file.endswith(".data"):
                    self.files_list.append(file)
            
        if reduction_rate is not None:
            if reduction_rate > 1 or reduction_rate < 0:
                raise Exception('Check the value of reduction_rate. It should belongs to [0,1] or should be None otherwise')
            current = len(self.files_list)
            goal = math.ceil(current * reduction_rate)
            
            while len(self.files_list) > goal:
                selected = int(random.uniform(0, len(self.files_list)))
                del self.files_list[selected]
                    
        self.root = root
        
        
    def next_dataset(self):
        n_clusters, X, Y = load_data(os.path.join(self.root,self.files_list[self.next]))
        self.next += 1
        return self.files_list[self.next - 1], n_clusters, X, Y
    
    def load_by_index(self,index):
        n_clusters, X, Y = load_data(os.path.join(self.root,self.files_list[index]))
        return self.files_list[index], n_clusters, X, Y
    
    def has_next(self):
        return self.next < len(self.files_list)
    
    def all_datasets(self):
        dataset_list = []
        while self.has_next():
            dataset_list.append((self.next_dataset()))
        return dataset_list
        
        