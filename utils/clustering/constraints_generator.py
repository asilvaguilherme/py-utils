import random

from active_semi_clustering.active.pairwise_constraints.example_oracle import MaximumQueriesExceeded
from active_semi_clustering.active.pairwise_constraints.explore_consolidate import ExploreConsolidate
from active_semi_clustering.active.pairwise_constraints.min_max import MinMax
from active_semi_clustering.active.pairwise_constraints.npu import NPU
from active_semi_clustering.semi_supervised.pairwise_constraints.mpckmeans import MPCKMeans


def generate_constraints(X, selector, n_clusters, oracle):
    
    if selector == "RANDOM":
        ml, cl = random_generator(X, oracle)
        
    elif selector == "MINMAX":
        
        active_learner = MinMax(n_clusters)
        active_learner.fit(X, oracle=oracle)
        
        ml, cl = active_learner.pairwise_constraints_[0], active_learner.pairwise_constraints_[1]
    
    elif selector == "ExpConsolidate":
        
        active_learner = ExploreConsolidate(n_clusters)
        active_learner.fit(X, oracle=oracle)
        
        ml, cl = active_learner.pairwise_constraints_[0], active_learner.pairwise_constraints_[1]
    
    elif selector == "NPU":
        
        active_learner = NPU(MPCKMeans(n_clusters))
        active_learner.fit(X=X, oracle=oracle)
        
        ml_array, cl_array = active_learner.pairwise_constraints_[0], active_learner.pairwise_constraints_[1]
        
        ml, cl = [], []
        for [x,y] in ml_array:
            ml.append((x,y))
        for [x,y] in cl_array:
            cl.append((x,y))
    
    return ml, cl

def random_generator(shuffled_X, oracle):
    
    ml, cl = [], []
        
    while True:
        choices = random.sample(range(len(shuffled_X)), 2)
        u,v = choices[0], choices[1]
        
        try:
            if oracle.query(u,v) :
                ml.append((u,v))
            else :
                cl.append((u,v))
                
        except MaximumQueriesExceeded:
            break
    
    return ml, cl