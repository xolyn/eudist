# eudist
the traditional faster way to compute the Euclidean distance of 2 vectors in n-dimension
## Recap:
### Inner product
$$\forall x,z \in \mathbb{R}^{1 \times m}, \text{their inner product,}  \langle x,z \rangle = x\cdot z=xz^{\top}$$

By def.:
$$\langle x,z \rangle = \sum_{i=1}^m x_i  z_i$$

### Norm (2-norm)
Using the definition above, the 2 norm (most common one) of a vector $x, ||x||_2$ is just the square root of the inner product with itself, namely:

$$||x||_{2}=\sqrt{\langle x,x \rangle}=\sqrt{xx^{\top}}=\sqrt{\sum_{i=1}^m x_i ^2}$$

### Euclidean distances
For same $x$ and $z$ above, consider these 2 matrices: $X=[ x_1,\dots, x_n]\in{\mathbb{R}}^{n\times d}$, where the $i^{th}$ row is a vector $\vec x_i$ and similarly $Z=[ z_1,\dots, z_m]\in{\mathbb{R}}^{m\times d}$ the Euclidean distance is defined by:
$$D_{ij}=\sqrt{(\vec x_i-\vec z_j)(\vec x_i-\vec z_j)^\top}.$$
