# eudist
the faster way to compute the Euclidean distance of 2 vectors in n-dimension
## Recap:
### Inner product
$$\forall x,z \in \mathbb{R}^{1 \times m}, \text{their inner product,}  \langle x,z \rangle = x\cdot z=xz^{\top}$$

By def.:
$$\langle x,z \rangle = \sum_{i=1}^m x_i  z_i$$

### Norm (2-norm)
Using the definition above, the 2 norm (most common one) of a vector $x,||x||_2$ is just the square root of the inner product with itself, namely:

$$\sqrt{\langle x,x \rangle}=\sqrt{xx^{\top}}=\sqrt{\sum_{i=1}^m x_i ^2}$$

### Euclidean distance
For same $x$ and $z$ above, consider these 2 matrices: $X=[ x_1,\dots, x_n]\in{\mathbb{R}}^{n\times d}$, where the $i^{th}$ row is a vector $\vec x_i$ and similarly $Z=[ z_1,\dots, z_m]\in{\mathbb{R}}^{m\times d}$. And the Euclidean distance is defined by:

$$D_{ij}=\sqrt{( x_i- z_j)( x_i- z_j)^\top}.$$

Per se definition, the following is a traditional method to compute the Euclidean distance by looping thru every dimension of vector $x$ and $z$:

```python
# Cr: CS5780 staff@Cornell
def l2distanceSlow(X,Z=None):
    if Z is None:
        Z = X
    n, d = X.shape     # dimension of X
    m= Z.shape[0]   # dimension of Z
    D=np.zeros((n,m)) # allocate memory for the output matrix
    for i in range(n):     # loop over vectors in X
        for j in range(m): # loop over vectors in Z
            D[i,j]=0.0; 
            for k in range(d): # loop over dimensions
                D[i,j]=D[i,j]+(X[i,k]-Z[j,k])**2; # compute l2-distance between the ith and jth vector
            D[i,j]=np.sqrt(D[i,j]); # take square root
    return D
```

This seems to work well until the dimension goes to larger than 500, which would cost 20-30 seconds according to computers' CPU. 

A new method creates 3 supplementary matrix, $S,R,G$ s.t.:
$G$(the Gram matrix/inner product matrix ) $=G_{ij}=\mathbf{x}_i\mathbf{z}_j^\top $

Whereas $S_{ij}=\mathbf{x}_i\mathbf{x}_i^\top$, $R_{ij}=\mathbf{z}_j\mathbf{z}_j^\top.$
