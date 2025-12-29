import streamlit as st

from drake.monte_carlo import run_monte_carlo
from drake.copulas import run_copula_mc
from drake.gaussian_process import gp_predict

from plots import (
    plot_N_distribution,
    plot_contributions,
    plot_dependencies,
    plot_sensitivity,
)

# --------------------------------------------------
# Page config (must be first Streamlit call)
# --------------------------------------------------
st.set_page_config(layout="wide")

# --------------------------------------------------
# Layout
# --------------------------------------------------
main_col, control_col = st.columns([3, 1])  # 75% / 25%

# --------------------------------------------------
# Control Panel (RIGHT)
# --------------------------------------------------
with control_col:
    st.markdown("## Control Panel")

    st.subheader("Drake Parameters")

    R_star = st.slider("Star Formation Rate (R*)", 0.1, 10.0, 1.5)
    fp = st.slider("Fraction with Planets (fp)", 0.0, 1.0, 0.5)
    ne = st.slider("Habitable Planets per System (ne)", 0.0, 5.0, 1.0)
    fl = st.slider("Fraction Developing Life (fl)", 0.0, 1.0, 0.3)
    fi = st.slider("Fraction Developing Intelligence (fi)", 0.0, 1.0, 0.1)
    fc = st.slider("Fraction Communicating (fc)", 0.0, 1.0, 0.1)
    L = st.slider("Longevity (L, years)", 10, 1_000_000, 10_000, log=True)

    params = {
        "R_star": R_star,
        "fp": fp,
        "ne": ne,
        "fl": fl,
        "fi": fi,
        "fc": fc,
        "L": L,
    }

    st.subheader("Model Selection")
    method = st.radio(
        "Simulation Method",
        ["Monte Carlo", "Copula", "Gaussian Process"]
    )

# --------------------------------------------------
# Run selected model
# --------------------------------------------------
if method == "Monte Carlo":
    results = run_monte_carlo(params)
elif method == "Copula":
    results = run_copula_mc(params)
else:
    results = gp_predict(params)

# --------------------------------------------------
# Main Visualization Area
# --------------------------------------------------
with main_col:
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.markdown("### Distribution of Intelligent Civilizations (N)")
        st.plotly_chart(plot_N_distribution(results), use_container_width=True)

    with col2:
        st.markdown("### Contribution Breakdown")
        st.plotly_chart(plot_contributions(results), use_container_width=True)

    with col3:
        st.markdown("### Parameter Dependencies")
        st.plotly_chart(plot_dependencies(results, method), use_container_width=True)

    with col4:
        st.markdown("### Sensitivity Analysis (Tornado Plot)")
        st.plotly_chart(plot_sensitivity(results), use_container_width=True)
