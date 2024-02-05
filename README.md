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
$G$(the Gram matrix/inner product matrix ) $=G_{ij}=x_iz_j^\top $

Whereas $S_{ij}=x_ix_i^{\top}$, $R_{ij}=z_jz_j^{\top}.$

A visualization of matrices $S$ and $R$ is like:

$$
S = \begin{bmatrix}
x_1 x_1^\top & x_1 x_1^\top & \cdots & x_1 x_1^\top\\
x_2 x_2^\top & x_2 x_2^\top & \cdots & x_2 x_2^\top\\
\vdots & \vdots & \ddots & \vdots\\
x_n x_n^\top & x_n x_n^\top & \cdots & x_n x_n^\top\\
\end{bmatrix}, \ 
R = \begin{bmatrix}
z_1 z_1^\top & z_2 z_2^\top & \cdots & z_m z_m^\top\\
z_1 z_1^\top & z_2 z_2^\top & \cdots & z_m z_m^\top\\
\vdots & \vdots & \ddots & \vdots\\
z_1 z_1^\top & z_2 z_2^\top & \cdots & z_m z_m^\top\\
\end{bmatrix}.
$$

The cleverness of this prompt is that we can prove that the distance matrix $D^2$, which is by definition $=(\mathbf{x}_i-\mathbf{z}_j)(\mathbf{x}_i-\mathbf{z}_j)^\top$ can be expressed as a linear combination of the matrix $S, G, R$:

$$
\forall i,j: 
\begin{align}D^2_{ij}&=(x_i-z_j)(x_i-z_j)^T\\
&=x_ix_i^T-x_iz_j^T-z_jx_i^T+z_jz_j^T\\  
&=x_ix_i^T-x_iz_j^T-(x_iz_j^T)^T+z_jz_j^T\\
&=x_ix_i^T-\sum_{k=1}^n x_{ik}z^T_{kj}-\sum_{k=1}^n z_{jk}x^T_{ki} +z_jz_j^T\\
&=x_ix_i^T-\sum_{k=1}^n x_{ik}z^T_{kj}-\sum_{k=1}^n z_{jk}x_{ik} +z_jz_j^T\\
&=x_ix_i^T-\sum_{k=1}^n x_{ik}z^T_{kj}-\sum_{k=1}^n x_{ik}z^T_{kj} +z_jz_j^T\\
\Rightarrow D^2&=S-2G+R \text{ (by def.)}
\end{align}\\
\quad 
$$

Using this algo., we can use `numpy` to easily achieve without a single loop.

*The code is divided into 2 parts, where `ip.py` achieves the inner product part (matrix $G$) and the `eudist.py` importing methods from `ip.py` achieves the matrix $S$, matrix $R$ and linear combination part.*
