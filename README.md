# Drake-Equation-Simulations
An analysis of different simulation methodologies to create a dashboard, which will showcase the likelihood of extraterrestrial life.

# Drake Equation Simulation Dashboard

An interactive, probabilistic exploration of the Drake Equation using
Monte Carlo simulation, Gaussian assumptions, and Copula-based dependency modeling.

Built with **Python**, **Streamlit**, and **scientifically grounded uncertainty modeling**.

---

## Project Overview

The Drake Equation estimates the number of active, communicative extraterrestrial
civilizations in the Milky Way galaxy. Traditionally, it is presented as a
single deterministic formula.

This project modernizes the equation by:
- Treating each term as a **random variable**
- Supporting **multiple modeling assumptions**
- Allowing users to explore **uncertainty, sensitivity, and correlation**
  interactively

---

## 🧠 Modeling Approaches

Users can toggle between:

### 🔹 Monte Carlo (Independent Terms)
- Assumes all Drake parameters are independent
- Best for baseline uncertainty exploration

### 🔹 Gaussian Approximation
- Assumes normality for each term
- Useful for analytic intuition and fast computation

### 🔹 Copula-Based Modeling
- Introduces **dependencies between terms**
- Enables correlated astrophysical and biological assumptions
- Most realistic (and most computationally intensive)
