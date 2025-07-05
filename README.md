# Equilibrium-Project

# Chemical Equilibrium Simulation : A ⇌ B

This Python script simulates a simple reversible chemical reaction:

A ⇌ B

using Euler's method to integrate the rate equations over time.

## Description

The system starts with :

- Initial concentration of A: `1.0`
- Initial concentration of B: `0.0`
- Forward rate constant: `1.0`
- Reverse rate constant: `0.5`

It models how the concentrations of A and B change over time and approach equilibrium. The simulation uses NumPy for numerical computation and Matplotlib for plotting.

## How It Works

At each time step:
- [A] decreases due to the forward reaction and increases due to the reverse reaction.
- [B] increases due to the forward reaction and decreases due to the reverse reaction.

Euler’s method is used to update concentrations over 1000 time steps from t = 0 to 10 seconds.

The script then plots the concentration of A and B vs. time.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

Install with:

pip install numpy matplotlib

Running the Script

Save the code in a file (e.g., reversible_reaction.py) and run it :

python reversible_reaction.py

This will display a plot showing the concentrations of A and B over time as they reach equilibrium.

Author

This project was developed by Abhinav Dixit. Feel free to fork, contribute, or reach out for questions.

License

Feel free to use and modify this script for educational or research purposes.
