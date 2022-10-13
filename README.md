# Mandelbrot_and_Markov
Uses python libraries (NumPy, MatPlotLib) to generate the Mandelbrot Set and Markov Chains.

For mandelbrot.py:

Function with arguments n -> points, N_max -> number of iterations, and threshold -> factor for determining divergence
- 2D grid of n values is made, where each (x,y) pair is in [-2, 1] x [-1.5, 1.5], using linespace() function
- Mesh grid is created for computing on each value in the 2D array
- c is calculated for each point in the grid
- set z = 0 for our initial value
- Recursively iterate through f(z) = z^2 + c, for each point in the grid, for N_max iterations
- Use a boolean mask over the values, determining which do not diverge
- Results are plotted and saved to a png file
The function is then tested with respective values of 5000, 50, and 50.

For markov_chain.py:

Function with arguments n -> size of transition matrix (n x n). and N -> number of iterations
- Create a normalized n x 1 vector with random entries (p)
- Create an n x n matrix with random entries (P)
- Scale entries in P so that each row's sum adds to 1
- Transpose P for computations on probabilities and eigenvalues
- Compute eigenvalues and eigenvectors with linalg.eig() function
- Set eigenvector with corresponding largest eigenvalue to p_stationary
- Scale entries in p_stationary so that entries sum to 1
- Iterate through for N steps, with P_T * p, using dot() function
- Each step, compare norm of p - p_stationary, using norm() function
- Results are plotted and displayed
The function is then tested with respective values of 5 and 50.
