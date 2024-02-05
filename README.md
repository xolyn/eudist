# eudist
the traditional faster way to compute the Euclidean distance of 2 vectors in n-dimension
## Recap:
### Inner product
$$\forall x,z \in \mathbb{R}^{1 \times m}, \text{their inner product,}  \langle x,z \rangle = x\cdot z=xz^{\top}$$

By def.:
$$\langle x,z \rangle = \sum_{i=1}^m x_i  z_i$$

### Norm
Using the definition above, the norm of a vector $x$ is just the square root of the inner product with itself, namely:
$$\sqrt{\langle x,x \rangle}=\sqrt{xx^{\top}=\sum_{i=1}^m x_i ^2 $$

### Euclidean distances

