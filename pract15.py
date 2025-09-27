# hopfield netwoek
import numpy as np

nb_patterns = 4      # Number of patterns to learn
pattern_width = 5
pattern_height = 3
max_iterations = 10

# Define Patterns
patterns = np.array([
    [1,-1,-1,-1,1,
     1,-1,1,-1,1,
     1,-1,-1,-1,1],     # Letter D

    [1,1,1,1,1,
     1,-1,-1,-1,-1,
     1,1,1,1,1],        # Letter J

    [1,1,1,1,1,
     1,-1,-1,-1,-1,
     1,1,1,1,1],        # Letter C

    [1,-1,-1,-1,1,
     1,1,-1,1,1,
     1,-1,-1,-1,1]      # Letter M
], dtype=float)

# Train the network
W = np.zeros((pattern_width * pattern_height, pattern_width * pattern_height))

for i in range(pattern_width * pattern_height):
    for j in range(pattern_width * pattern_height):
        if i == j or W[i, j] != 0.0:
            continue
        w = 0.0
        for n in range(nb_patterns):
            w += patterns[n, i] * patterns[n, j]
        w = w / patterns.shape[0]
        W[i, j] = w
        W[j, i] = w  # Ensure symmetry

# Test the Network
# Create a corrupted pattern
s = np.array([
    1, -1, -1, -1, 1,
    -1, 1, -1, 1, -1,
    1, -1, -1, -1, 1
], dtype=float)

h = np.zeros((pattern_width * pattern_height))

# Defining Hamming Distance matrix for seeing convergence
hamming_distance = np.zeros((max_iterations, nb_patterns))

for iteration in range(max_iterations):
    for i in range(pattern_width * pattern_height):
        i = np.random.randint(pattern_width * pattern_height)
        h[i] = 0
        for j in range(pattern_width * pattern_height):
            h[i] += W[i, j] * s[j]
        
        s[i] = np.where(h[i] < 0, -1, 1)

    for i in range(nb_patterns):
        hamming_distance[iteration, i] = (patterns[i] != s).sum()

print(hamming_distance)