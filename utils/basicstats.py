import numpy as np
from utils.data_loader import Loader


loader = Loader("../downloaded")

while loader.has_next_train_dataset():
    dataset_name, n_clusters, X, Y = loader.next_dataset()
    for i in range(len(X[0])):
        bins=5
        h = np.histogram(X[:,i], bins=bins)
        print(h[0], end=' ', flush=True)
    print()