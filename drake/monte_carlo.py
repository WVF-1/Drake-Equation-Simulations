# drake/monte_carlo.py

import numpy as np
from drake.Simulation import simulate_once

def run_monte_carlo(params, n_simulations=10_000):
    """
    Run many Drake Equation simulations.
    """

    results = [simulate_once(params) for _ in range(n_simulations)]

    N_values = np.array([r["N"] for r in results])

    return {
        "raw": results,
        "N": N_values,
        "summary": {
            "mean": float(np.mean(N_values)),
            "median": float(np.median(N_values)),
            "std": float(np.std(N_values)),
            "p5": float(np.percentile(N_values, 5)),
            "p95": float(np.percentile(N_values, 95)),
        },
    }
