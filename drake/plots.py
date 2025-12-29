import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --------------------------------------------------
# Global Space Theme
# --------------------------------------------------
SPACE_THEME = dict(
    paper_bgcolor="#05080f",
    plot_bgcolor="#05080f",
    font=dict(color="#d6e1ff"),
    colorway=["#00ff9c", "#4cc9f0", "#7209b7", "#f72585"],
)

# --------------------------------------------------
# Helper
# --------------------------------------------------
def apply_theme(fig):
    fig.update_layout(**SPACE_THEME)
    fig.update_xaxes(showgrid=True, gridcolor="rgba(255,255,255,0.05)")
    fig.update_yaxes(showgrid=True, gridcolor="rgba(255,255,255,0.05)")
    return fig

# --------------------------------------------------
# Graph 1: Distribution of N
# --------------------------------------------------
def plot_N_distribution(results):
    N = np.array(results["N"])

    fig = go.Figure()

    fig.add_trace(
        go.Histogram(
            x=N,
            nbinsx=50,
            name="N Distribution",
            opacity=0.6,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=np.sort(N),
            y=np.linspace(0, 1, len(N)),
            name="Empirical CDF",
            yaxis="y2",
            line=dict(width=2),
        )
    )

    fig.update_layout(
        title="Distribution of Intelligent Civilizations (N)",
        xaxis_title="N",
        yaxis_title="Count",
        yaxis2=dict(
            overlaying="y",
            side="right",
            title="CDF",
            showgrid=False,
        ),
    )

    return apply_theme(fig)

# --------------------------------------------------
# Graph 2: Contribution Breakdown (Bar Chart)
# --------------------------------------------------
def plot_contributions(results):
    df = pd.DataFrame(results)

    factors = ["R_star", "fp", "ne", "fl", "fi", "fc", "L"]
    contributions = {f: np.mean(df[f]) for f in factors}

    fig = px.bar(
        x=list(contributions.keys()),
        y=list(contributions.values()),
        labels={"x": "Drake Factor", "y": "Expected Value"},
        title="Expected Contribution by Drake Factor",
    )

    return apply_theme(fig)

# --------------------------------------------------
# Graph 3: Dependencies / Correlations
# --------------------------------------------------
def plot_dependencies(results, method):
    df = pd.DataFrame(results)

    corr = df.corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="Plasma",
        title=f"Parameter Dependencies ({method})",
    )

    return apply_theme(fig)

# --------------------------------------------------
# Graph 4: Sensitivity Analysis (Tornado Plot)
# --------------------------------------------------
def plot_sensitivity(results):
    df = pd.DataFrame(results)

    factors = ["R_star", "fp", "ne", "fl", "fi", "fc", "L"]
    N = df["N"].values

    sensitivities = {}

    for f in factors:
        x = df[f].values
        sensitivities[f] = np.corrcoef(np.log(x + 1e-9), np.log(N + 1e-9))[0, 1]

    sens_df = (
        pd.DataFrame({
            "Factor": sensitivities.keys(),
            "Sensitivity": sensitivities.values(),
        })
        .sort_values("Sensitivity")
    )

    fig = go.Figure(
        go.Bar(
            x=sens_df["Sensitivity"],
            y=sens_df["Factor"],
            orientation="h",
        )
    )

    fig.update_layout(
        title="Sensitivity of N to Drake Parameters (Tornado Plot)",
        xaxis_title="Sensitivity (log–log correlation)",
        yaxis_title="Drake Parameter",
    )

    return apply_theme(fig)
