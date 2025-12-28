import numpy as np
from scipy.stats import norm, multivariate_normal

def gaussian_copula_sample(corr_matrix, n_samples):
    """
    Sample from a Gaussian copula.
    """
    dim = corr_matrix.shape[0]
    z = multivariate_normal.rvs(
        mean=np.zeros(dim),
        cov=corr_matrix,
        size=n_samples
    )
    u = norm.cdf(z)
    return u


def clayton_copula_sample(theta, n_samples, dim):
    """
    Sample from a Clayton copula (lower-tail dependence).
    """
    if theta <= 0:
        raise ValueError("Clayton copula theta must be > 0")

    u = np.random.uniform(size=(n_samples, dim))
    w = np.random.gamma(shape=1 / theta, scale=1, size=(n_samples, 1))
    samples = (1 + u / w) ** (-1 / theta)
    return samples


def apply_marginals(u_samples, marginal_inverse_cdfs, keys):
    """
    Transform copula samples into physical parameter samples.
    """
    samples = {}
    for i, key in enumerate(keys):
        inv_cdf = marginal_inverse_cdfs[key]
        samples[key] = inv_cdf(u_samples[:, i])
    return samples
