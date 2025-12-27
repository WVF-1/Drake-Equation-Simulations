"""
Baseline parameters for Drake Equation distributions.
"""

BASELINE_PARAMS = {
    "R_star": {
        "mean": 1.5,
        "std": 0.5,
        "low": 0.5,
        "high": 3.0
    },
    "fp": {
        "alpha": 50,
        "beta": 2
    },
    "ne": {
        "mean": 0.2,
        "sigma": 0.5
    },
    "fl": {
        "alpha": 1,
        "beta": 1
    },
    "fi": {
        "alpha": 2,
        "beta": 20
    },
    "fc": {
        "alpha": 3,
        "beta": 10
    },
    "L": {
        "xm": 100,
        "alpha": 1.7
    }
}
