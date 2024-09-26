import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Enable interactive mode for Jupyter notebook
%matplotlib notebook

# Define the initial condition
def initial_condition(x):
    return np.sin(x)  # Example initial condition for the Riemann equation

# Discretize the x domain and time
x_values = np.linspace(-5, 5, 1000)  # Spatial resolution
t_values = np.linspace(0, 2, 300)   # Time range up to t=2
dt = t_values[1] - t_values[0]
dx = x_values[1] - x_values[0]

# Store solution for all time steps
u_sol = np.zeros((len(t_values), len(x_values)))

# Initial condition at t=0
u_sol[0, :] = initial_condition(x_values)

# Time evolution for the Riemann equation u_t = u_x (linear advection)
for i in range(1, len(t_values)):
    for j, x in enumerate(x_values):
        # Get the value at x at the previous time step
        u0 = u_sol[i-1, j]

        # Calculate the characteristic coordinate (x0) for u_t = u_x
        # Here, the characteristic speed is 1, so we use x0 = x - t
        x0 = x - dt  # characteristic speed is 1
        
        # Use the initial condition to get the value at the new location
        # We need to ensure x0 is within the bounds of the original x_values
        if -5 < x0 < 5:
            # Use linear interpolation to find the value at x0
            u_sol[i, j] = np.interp(x0, x_values, u_sol[i-1, :])
        else:
            # Apply boundary condition (e.g., reflective or periodic)
            u_sol[i, j] = u_sol[i, j-1] if j > 0 else 0  # Reflective boundary

# Create a figure and axis for the animation
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

# Set plot limits
ax.set_xlim(x_values[0], x_values[-1])
ax.set_ylim(np.min(u_sol), np.max(u_sol))
ax.set_xlabel('x')
ax.set_ylabel('u(x, t)')
ax.set_title('Evolution of the Solution to the Riemann Equation')

# Function to initialize the background of the plot
def init():
    line.set_data([], [])
    return line,

# Function to update the plot at each time step
def update(frame):
    line.set_data(x_values, u_sol[frame, :])
    ax.set_title(f'Evolution at t={t_values[frame]:.3f}')  # Display finer time values
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(t_values), init_func=init, blit=True)

# Display the animation in the notebook
HTML(ani.to_jshtml())

# Plot characteristics curves
plt.figure()
for i, x0 in enumerate(np.linspace(-5, 5, 10)):  # Take 10 initial points
    plt.plot([x0, x0 + t_values[-1]], [0, t_values[-1]], 'r--', label=f'x0={x0}' if i == 0 else "")
plt.xlim(-5, 5)
plt.ylim(0, t_values[-1])
plt.xlabel('x')
plt.ylabel('t')
plt.title('Characteristics for u_t = u_x')
plt.legend(loc='upper left')
plt.show()
