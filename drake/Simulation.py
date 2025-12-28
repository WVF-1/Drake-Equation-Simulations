# drake/simulation.py

from drake.Distributions import (
    sample_star_formation_rate,
    sample_fp,
    sample_ne,
    sample_fl,
    sample_fi,
    sample_fc,
    sample_L,
)

def simulate_once(params):
    """
    Simulate one realization of the Drake Equation.
    """

    R_star = sample_star_formation_rate(params)
    fp = sample_fp(params)
    ne = sample_ne(params)
    fl = sample_fl(params)
    fi = sample_fi(params)
    fc = sample_fc(params)
    L = sample_L(params)

    N = R_star * fp * ne * fl * fi * fc * L

    return {
        "R_star": R_star,
        "fp": fp,
        "ne": ne,
        "fl": fl,
        "fi": fi,
        "fc": fc,
        "L": L,
        "N": N,
    }
