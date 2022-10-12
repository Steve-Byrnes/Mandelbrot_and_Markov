import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_generate(n, N_max, threshold):
    """
    n -> size of grid
    N_max -> number of iterations
    threshold -> determining whether points belong in set
    """
    # Creates the 2D array of (x,y) in range [-2, 1] x [-1.5, 1.5]
    x_space = np.linspace(-2, 1, n)
    y_space = np.linspace(-1.5, 1.5, n)
    
    # Creates meshgrid for computing on each value in 2D array
    x, y = np.meshgrid(x_space,y_space)

    # Given code for computing on each corresponding (x,y)
    c = x + 1j*y

    # Set starting value of z to be 0
    z = 0

    # Iterates the function N_Max times, for each computed value of c
    for j in range(N_max):
        z = z**2 + c
    
    # Boolean mask for whether a given point is within a certain treshhold, and not diverging    
    mask = (abs(z) < threshold)

    # Create plot for generating the mandelbrot set
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')

# Testing the function for inputted 5000 values in grid, 50 iterations, and 50 threshhold
testing = mandelbrot_generate(5000, 50, 50)