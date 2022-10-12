import numpy as np
import matplotlib.pyplot as plt

def markov_generate(n, N):
    """
    n -> size of nxn array for transition matrix
    N -> number of steps in Markov Chain
    """

    # Create vector of size nx1 with random entries
    randV = np.random.rand(n,1)
    
    # Normalize entries so sum is equal to 1
    sum = np.sum(randV)
    p = randV / sum

    # Create nxn transition matrix with random entries
    P = np.random.rand(n,n)

    # Iterate through P and normalize so each row sums to 1
    for i in range(n):
        sum = np.sum(P[i,:])
        P[i,:] = P[i,:] / sum

    # Create transpose of P, where columns will add to 1
    P_T = np.transpose(P)

    # Generate eigenvalues and eigenvectors for P_T
    # w -> eigenvalues, v -> eigenvectors
    w, v = np.linalg.eig(P_T)

    # Find the index in eigenvector array, corresponding to the largest eigenvalue
    maxInd = np.argmax(w)
    # Assign the stationary point, p_stationary, based on this index
    p_stationary = v[maxInd]

    # Normalize p_stationary so each entry sums to 1
    sum = np.sum(p_stationary)
    for i in range(n):
        p_stationary[i] = p_stationary[i] / sum

    # Iterate through N steps for markov chain to get the updated value for p
    # and the difference between p and stationary point
    normList = []
    for i in range(N):
        normList.append(np.linalg.norm(p - p_stationary))
        p = np.dot(P_T, p)
    
    # Generate plot for difference between p and p_stationary
    plt.plot(normList)
    plt.title('Iterating the Difference Between p and p_stationary')
    plt.ylabel('Norm of p - p_stationary')
    plt.show()

# Testing values for generating markov chain of 5x5 transition matrix and 50 steps
testing = markov_generate(5, 50)