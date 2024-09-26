# Riemann Equation Solver with Characteristics Visualization 

This project numerically solves the Riemann equation: `u_t = u_x` using the method of characteristics and provides an animation of the evolving solution as well as a plot of the characteristic curves. The project uses Python with NumPy for numerical computations and Matplotlib for visualization.

## Table of Contents 
- [Overview](#overview) 
- [Mathematical Background](#mathematical-background)
- [Files](#files)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [References](#references)

## Overview 
The Riemann equation `u_t = u_x` is a linear advection equation that describes how a wave or signal propagates with a constant speed. The project solves this PDE using the **method of characteristics**, which involves tracking the solution along characteristic lines in the `(x, t)`-plane. 

This approach works well for linear equations like the Riemann equation, as it captures the propagation of the wave without introducing numerical diffusion.

### Features: 
- A numerical solver for the Riemann equation. - An animated plot showing the evolution of the solution over time. - A plot of the characteristic curves, which represent the paths along which the solution propagates.

## Mathematical Background The Riemann equation can be expressed as: 

`u_t - u_x = 0` 

which is also written as: 

`∂u/∂t = ∂u/∂x`

### Characteristics: 
For linear hyperbolic equations like this one, characteristics are lines along which the solution remains constant. These lines are given by: `x(t) = x₀ + t` where `x₀` is the initial position at time `t = 0`.

### Numerical Solution: 
The method of characteristics calculates how each point in the domain propagates over time. At each time step, the solution is updated by interpolating along the characteristic curves.

## Files - **`riemann_solver.py`**: 
The main Python script that includes the solver, animation, and characteristic curve plotting. - **`README.md`**: This documentation file.

## Requirements This project requires the following Python libraries: 
- `numpy` - `matplotlib` - `IPython` (for inline animations in Jupyter Notebooks) You can install the dependencies using the following command: ```bash pip install numpy matplotlib ipython ```


## Usage 1. 
Run the Python script `riemann_solver.py`: ```bash python riemann_solver.py ``` 2. If you're using a Jupyter Notebook, you can execute the script inline by running the code within a notebook cell. The animation of the wave solution and characteristic curves will be displayed.

## Example Output ### Wave Solution Evolution: 
The code provides an animation showing the evolution of the wave as it propagates over time, using the method of characteristics. ### Characteristic Curves: Alongside the wave solution, you can visualize the characteristic curves, which indicate the direction and speed of the wave propagation.





