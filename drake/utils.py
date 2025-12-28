#drake/utils.py

import numpy as np

def probability_at_least_one(N_samples):
    """
    Compute P(N >= 1).
    """
    return np.mean(N_samples >= 1)


def summarize_distribution(x):
    """
    Standard numeric summary for distributions.
    """
    return {
        "mean": float(np.mean(x)),
        "median": float(np.median(x)),
        "std": float(np.std(x)),
        "p5": float(np.percentile(x, 5)),
        "p95": float(np.percentile(x, 95)),
    }


def log_safe(x, eps=1e-12):
    """
    Safe log for heavy-tailed distributions.
    """
    return np.log(np.maximum(x, eps))
