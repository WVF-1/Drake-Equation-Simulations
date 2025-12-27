"""
Drake Equation parameter distributions.
"""
from scipy import stats

def sample_star_formation_rate(n, mean=1.5, std=0.5, low=0.5, high=3.0):
    """Sample Milky Way star formation rate (stars/year)."""
    samples = stats.truncnorm(
        (low - mean) / std,
        (high - mean) / std,
        loc=mean,
        scale=std
    ).rvs(size=n)
    return samples

def sample_fp(n, alpha=50, beta=2):
    """Fraction of stars with planetary systems."""
    return stats.beta(alpha, beta).rvs(size=n)

def sample_ne(n, mean=0.2, sigma=0.5):
    """Habitable-zone planets per system."""
    return stats.lognorm(s=sigma, scale=mean).rvs(size=n)

def sample_fl(n, alpha=1, beta=1):
    """Fraction of habitable planets where life arises."""
    return stats.beta(alpha, beta).rvs(size=n)

def sample_fi(n, alpha=2, beta=20):
    """Fraction of life-bearing planets where intelligence arises."""
    return stats.beta(alpha, beta).rvs(size=n)

def sample_fc(n, alpha=3, beta=10):
    """Fraction of intelligent civilizations that communicate."""
    return stats.beta(alpha, beta).rvs(size=n)

def sample_L(n, xm=100, alpha=1.7):
    """
    Lifetime of communicating civilizations (years).
    Type I Pareto with minimum lifetime xm.
    """
    return (stats.pareto(alpha, scale=xm)).rvs(size=n)
