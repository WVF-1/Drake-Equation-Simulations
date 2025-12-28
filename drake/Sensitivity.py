#drake/sensitivty.py

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from drake.Simulation import simulate_once


def run_oat_sensitivity(params, n_simulations=1000, perturbation=0.1):
    """
    One-at-a-Time sensitivity analysis.
    """
    baseline_results = [
        simulate_once(params)["N"] for _ in range(n_simulations)
    ]
    baseline_mean = np.mean(baseline_results)

    sensitivities = {}

    for key in params.keys():
        perturbed_params = params.copy()
        perturbed_params[key] = params[key].copy()

        if "mean" in perturbed_params[key]:
            perturbed_params[key]["mean"] *= (1 + perturbation)

        perturbed_results = [
            simulate_once(perturbed_params)["N"]
            for _ in range(n_simulations)
        ]

        perturbed_mean = np.mean(perturbed_results)
        sensitivities[key] = perturbed_mean - baseline_mean

    return sensitivities


def run_prcc(params, n_simulations=5000):
    """
    Partial Rank Correlation Coefficients.
    """
    records = []

    for _ in range(n_simulations):
        sim = simulate_once(params)
        records.append(sim)

    df = pd.DataFrame(records)

    prcc = {}
    for col in df.columns:
        if col == "N":
            continue
        corr, _ = spearmanr(df[col], df["N"])
        prcc[col] = corr

    return prcc
