from inprd import innerproduct
import numpy as np
def l2distance(X,Z=None):
    if Z is None:
        Z=X
    n,d1=X.shape
    m,d2=Z.shape
    assert (d1==d2), "Dimensions of input vectors must match!"

    #matrix S
    xsum_of_squares = np.sum(X**2, axis=1)
    S = np.repeat(xsum_of_squares, m).reshape(n,m)
    #matrix Z
    zsum_of_squares = np.sum(Z**2, axis=1)
    R = np.repeat(zsum_of_squares, n).reshape(m, n).T # note the different shape of Z and S, take transpose after processing normally
    G=innerproduct(X,Z) # can be replaced by np.dot()
    # linear combination
    D2=S-2*G+R
    D2=np.clip(D2, a_min=0, a_max=None) # avoid tiny numbers displayed as negative numbers due to system internal computing characteristics 
    D=np.sqrt(D2)
    return D
