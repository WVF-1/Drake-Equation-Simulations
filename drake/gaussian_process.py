# drake/gaussian_process.py

import numpy as np

def rbf_kernel(x1, x2, length_scale=1.0):
    """
    Radial Basis Function (Gaussian) kernel.
    """
    sqdist = np.subtract.outer(x1, x2) ** 2
    return np.exp(-0.5 * sqdist / length_scale**2)

def gp_sample(x, mean=0.0, length_scale=1.0, noise=1e-6):
    """
    Draw a GP sample over x.
    """

    K = rbf_kernel(x, x, length_scale)
    K += noise * np.eye(len(x))

    return np.random.multivariate_normal(
        mean=np.full(len(x), mean),
        cov=K
    )
