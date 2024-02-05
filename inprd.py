import numpy as np
def innerproduct(X,Z=None):
    if Z is None: # case when there is only one input (X)
        Z=X
    G=np.dot(X,Z.T)
    return G