# drake/bayesian_models.py

import numpy as np

def hierarchical_prior(group_means, group_stds):
    """
    Simple hierarchical normal prior sampler.
    """

    return np.random.normal(group_means, group_stds)

def sample_bayesian_fp(hyper_mu, hyper_sigma):
    """
    Example Bayesian model for fp.
    """

    fp = np.random.normal(hyper_mu, hyper_sigma)
    return np.clip(fp, 0, 1)
