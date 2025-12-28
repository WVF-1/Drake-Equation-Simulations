"""
Drake Equation parameter distributions.
"""
from scipy import stats

def sample_star_formation_rate(params):
    """Sample Milky Way star formation rate (stars/year)."""
    mean = params.get('R_star_mean', 1.5)
    std = params.get('R_star_std', 0.5)
    low = params.get('R_star_low', 0.5)
    high = params.get('R_star_high', 3.0)
    
    sample = stats.truncnorm(
        (low - mean) / std,
        (high - mean) / std,
        loc=mean,
        scale=std
    ).rvs()
    return sample

def sample_fp(params):
    """Fraction of stars with planetary systems."""
    alpha = params.get('fp_alpha', 50)
    beta = params.get('fp_beta', 2)
    return stats.beta(alpha, beta).rvs()

def sample_ne(params):
    """Habitable-zone planets per system."""
    mean = params.get('ne_mean', 0.2)
    sigma = params.get('ne_sigma', 0.5)
    return stats.lognorm(s=sigma, scale=mean).rvs()

def sample_fl(params):
    """Fraction of habitable planets where life arises."""
    alpha = params.get('fl_alpha', 1)
    beta = params.get('fl_beta', 1)
    return stats.beta(alpha, beta).rvs()

def sample_fi(params):
    """Fraction of life-bearing planets where intelligence arises."""
    alpha = params.get('fi_alpha', 2)
    beta = params.get('fi_beta', 20)
    return stats.beta(alpha, beta).rvs()

def sample_fc(params):
    """Fraction of intelligent civilizations that communicate."""
    alpha = params.get('fc_alpha', 3)
    beta = params.get('fc_beta', 10)
    return stats.beta(alpha, beta).rvs()

def sample_L(params):
    """
    Lifetime of communicating civilizations (years).
    Type I Pareto with minimum lifetime xm.
    """
    xm = params.get('L_xm', 100)
    alpha = params.get('L_alpha', 1.7)
    return stats.pareto(alpha, scale=xm).rvs()