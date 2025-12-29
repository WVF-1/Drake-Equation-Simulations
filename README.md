# Drake Equation Simulations 🌌

An advanced statistical analysis framework for exploring the Drake Equation through Monte Carlo simulations, Bayesian methods, and machine learning surrogates. This project provides both analytical notebooks and an interactive dashboard for investigating the probability of extraterrestrial civilizations in our galaxy.

## Overview

The [Drake Equation](https://en.wikipedia.org/wiki/Drake_equation) estimates the number of detectable alien civilizations in the Milky Way:
```
N = R★ × fp × ne × fl × fi × fc × L
```

Where:
- **R★**: Star formation rate (stars/year)
- **fp**: Fraction of stars with planets
- **ne**: Number of habitable planets per planetary system
- **fl**: Fraction of habitable planets where life emerges
- **fi**: Fraction of life-bearing planets where intelligence evolves
- **fc**: Fraction of intelligent civilizations that develop communication
- **L**: Lifetime of communicating civilizations (years)
- **N**: Number of detectable civilizations in the galaxy

## Features

### Analysis Modules
- **Monte Carlo Simulations**: Run thousands of parameter combinations with uncertainty propagation
- **Copula Models**: Capture complex dependencies between Drake parameters
- **Sensitivity Analysis**: Identify which parameters most influence outcomes (Sobol indices, tornado diagrams)
- **Bayesian Methods**: Update beliefs with new evidence and quantify uncertainty
- **Gaussian Process Surrogates**: 871x faster predictions with maintained accuracy

### Interactive Dashboard
- Real-time parameter adjustment
- Dynamic visualizations of probability distributions
- Comparative analysis across different scenarios
- Export results and figures

## Project Structure
```
Drake-Equation-Simulations/
├── Dashboard/
│   ├── app.py              # Streamlit/Dash dashboard application
│   └── plots.py            # Visualization components
├── Notebooks/
│   ├── 01_baseline_exploration.ipynb
│   ├── 02_copula_comparison.ipynb
│   ├── 03_sensitivity_analysis.ipynb
│   ├── 04_bayesian_hierarchical_models.ipynb
│   └── 05_gaussian_process_surrogates.ipynb
└── drake/
    ├── __init__.py
    ├── Parameters.py       # Baseline parameter distributions
    ├── Distributions.py    # Statistical distributions for each parameter
    ├── Simulation.py       # Core Drake Equation simulation
    ├── monte_carlo.py      # Monte Carlo engine
    ├── Copulas.py          # Copula dependency models
    ├── Sensitivity.py      # Sensitivity analysis tools
    ├── bayesian_models.py  # Bayesian inference methods
    ├── gaussian_process.py # GP surrogate models
    └── utils.py            # Helper functions
```

## Installation

### Prerequisites
- Python 3.8+
- Anaconda or pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/WVF-1/Drake-Equation-Simulations.git
cd Drake-Equation-Simulations
```

2. Create a virtual environment:
```bash
conda create -n drake python=3.12
conda activate drake
```

3. Install dependencies:
```bash
pip install numpy pandas matplotlib seaborn scipy scikit-learn
pip install jupyter notebook
pip install streamlit  # For dashboard

# Optional: Advanced analysis packages
pip install SALib      # Sobol sensitivity analysis
pip install pymc arviz # Bayesian modeling
```

4. **Important**: Use NumPy 1.x for compatibility:
```bash
pip install "numpy<2.0"
```

## Usage

### Running the Notebooks
```bash
jupyter notebook
```

Navigate to the `Notebooks/` folder and run them in order:
1. **Baseline Exploration**: Understand basic parameter distributions and correlations
2. **Copula Comparison**: Model parameter dependencies
3. **Sensitivity Analysis**: Identify critical parameters
4. **Bayesian Models**: Update beliefs with evidence
5. **GP Surrogates**: Fast approximations for large-scale exploration

### Launching the Dashboard
```bash
cd Dashboard
streamlit run app.py  # or python app.py for Dash
```

### Basic Python Usage
```python
from drake.Parameters import BASELINE_PARAMS
from drake.Simulation import simulate_once
from drake.monte_carlo import run_monte_carlo

# Single simulation
result = simulate_once(BASELINE_PARAMS)
print(f"Estimated civilizations: {result['N']:.2f}")

# Monte Carlo with 10,000 runs
mc_results = run_monte_carlo(BASELINE_PARAMS, n_simulations=10_000)
results_df = pd.DataFrame(mc_results['raw'])
print(f"Mean N: {results_df['N'].mean():.2f}")
```

## Key Results

- **Baseline estimate**: Mean N ≈ [your result]
- **Parameter importance**: L (civilization lifetime) and fi (intelligence evolution) show highest sensitivity
- **GP Surrogate performance**: 871x speedup with R² > 0.95
- **Uncertainty**: 95% credible interval spans [your range]

## Methodology

### Statistical Distributions
- **R★**: Truncated normal (0.5 - 3.0 stars/year)
- **fp**: Beta distribution (α=50, β=2) - high confidence
- **ne**: Lognormal - wide uncertainty
- **fl, fi, fc**: Beta distributions - highly uncertain
- **L**: Pareto Type I distribution - heavy-tailed

### Analysis Techniques
- **Monte Carlo**: 10,000+ simulations with Latin Hypercube Sampling
- **Copulas**: Gaussian and Archimedean families for dependency modeling
- **Sensitivity**: Sobol indices, Morris screening, tornado diagrams
- **Bayesian**: Sequential updating with conjugate priors
- **ML Surrogate**: RBF kernel GP with hyperparameter optimization

## Dependencies

Core:
- numpy (<2.0)
- pandas
- scipy
- matplotlib
- seaborn
- scikit-learn

Optional:
- SALib (sensitivity analysis)
- pymc + arviz (Bayesian modeling)
- streamlit or dash (dashboard)

## Contributing

Contributions welcome! Areas for enhancement:
- Additional parameter distributions based on recent exoplanet discoveries
- Integration with astronomical databases
- Alternative ML surrogate models
- Extended dashboard features

## References

1. Drake, F. (1961). "The Drake Equation"
2. Burchell, M. J. (2006). "W(h)ither the Drake equation?" *International Journal of Astrobiology*
3. Sandberg et al. (2018). "Dissolving the Fermi Paradox"
4. Recent exoplanet statistics from NASA Exoplanet Archive

## License

MIT License - see LICENSE file for details

## Author
William V. Fullerton

## Acknowledgments

- Drake equation formulation by Frank Drake (1961)
- Statistical methods inspired by uncertainty quantification literature
- Thanks to the open-source scientific Python community

---

*"Sometimes I think we're alone in the universe, and sometimes I think we're not. In either case, the idea is quite staggering."* - Arthur C. Clarke
