"""
This is HW 1
For PSTAT 160B
Prof Ichiba
TA: Mousavi
"""
# import modules
from __future__ import division
import numpy as np

# Define variables for Part A
n = 3
mean = 1

def part_a():
    # Generate 3 random exponential variables
    X1 = np.random.exponential(scale = 1.0)
    X2 = np.random.exponential(scale = 1.0)
    X3 = np.random.exponential(scale = 1.0)
    
    # Find the max via if statements
    max = X1
    subscript = 1
    if X2 > max:
        max = X2
        subscript = 2
    if X3 > max: 
        max = X3
        subscript = 3
    
    # Print out results
    print("The max Xi for i = 1, 2, 3 is X{0}, with a value of {1}").format(subscript, max)

def part_b():
    # Declare variables for simulations
    num_sim = 1000
    current_sim = 0
    # Create lists to store the min and max values of every conditioned simulation
    min_Xi = []
    max_Xi = []
    min_Xi_2 = []
    max_Xi_2 = []

    while current_sim < num_sim:
        # Generate random variables
        X1 = np.random.exponential(scale = 1.0)
        X2 = np.random.exponential(scale = 1.0)
        X3 = np.random.exponential(scale = 1.0)

        # Check conditions for Part ii and iii of Part B
        # Part i will be calculated later
        if X1 < X2:
            # Part ii
            min = X1

            if X2 < min:
                min = X2
            if X3 < min:
                min = X3

            min_Xi.append(min)
           
            # Part iii
            max = X1

            if X2 > max:
                max = X2
            if X3 > max:
                max = X3

            max_Xi.append(max)
            
        # Check condition for Part iv and v of Part B
        if X1 < X2 < X3:
            # Part iii
            # Since X1 < X2 < X3, X1 is ALWAYS the minimum value
            min_2 = X1

            # Would use this code if it was necessary
            """
            if X2 < min_2:
                min_2 = X2
            if X3 < min_2:
                min_2 = X3
            """
            min_Xi_2.append(min_2)
            
            # Part iv
            # Since X1 < X2 < X3, X1 is ALWAYS the maximum value
            max_2 = X3

            # Would use this code if it was necessary
            """
            if X2 > max_2:
                max_2 = X2
            if X3 > max_2: 
                max_2 = X3
            """
            max_Xi_2.append(max_2)

        # Increment the count
        current_sim += 1

    # Solve Part i of B using length of either min_Xi_2 or max_Xi_2
    # Since the lengths of both are the number of times that X1 < X2 < X3
    prob = len(min_Xi_2) / num_sim
    print("P(X1 < X2 < X3) = %.3f" % prob)

    # Part ii
    exp_min_1 = sum(min_Xi) / len(min_Xi)
    print("E[minimum Xi for i = 1, 2, 3 | X1 < X2] = %.2f" % exp_min_1)

    # Part iii
    exp_max_1 = sum(max_Xi) / len(max_Xi)
    print("E[maximum Xi for i = 1, 2, 3 | X1 < X2] = %.2f" % exp_max_1)

    # Part iv
    exp_max_2 = sum(max_Xi_2) / len(max_Xi_2)
    print("E[maximum Xi for i = 1, 2, 3 | X1 < X2 < X3] = %.2f" % exp_max_2)

    # Part iv
    exp_min_2 = sum(min_Xi_2) / len(min_Xi_2)
    print("E[minimum Xi for i = 1, 2, 3 | X1 < X2 < X3] = %.2f" % exp_min_2)

# Call functions
part_a()
part_b()
