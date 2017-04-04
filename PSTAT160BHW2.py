"""
This is the Python HW 2
for PSTAT 160B
Prof Ichiba 
TA: Mousavi
Section: W 1:00 - 1:50pm
"""
from __future__ import division
import random
import math
import matplotlib.pyplot as plt
import numpy as np

def Part_A():
    # Define the sample path of N(t) for the time interval [0, 10]
    # Let us define start time; end time will be defined below
    start_time = 0
    # Our Poisson process will have parameter lamdba * time 
    # First we define intensity (or lambda)
    lmda = 10
    # Next we define the time variable through which our Poisson Process simulates
    t = 10
    # Now let's simulate a Poisson Process with parameter lambda * time
    N1 = np.random.poisson(lmda * t)
    print("Part A:") 
    print("The number of events that has occurred for our Poisson Process from time t = 0 to t = 10 is %d" % N1)

    # Every event in the Poisson Process arrives uniformly between the time interval [0, 10]
    # We will simulate N uniform random variables to simulate the occurances of the events in the Poisson Process
    # We make a list for these below
    # We initialize 0 as the first value to account for the time between t = 0 and the first event
    interarrival_times = [0]
    # And now simulate those event times
    for i in range(start_time, N1):
        interarrival_time = np.random.uniform(start_time, t)
        interarrival_times.append(interarrival_time)
    
    # The times are not in order so we need to sort them
    sorted_times = sorted(interarrival_times)
    
    # We now have the times of the event occurances
    # Now we need a complimentary list of numbers from 0 to N
    # As we are making a stepwise graph
    # And an event occurs at every interarrival time
    events = [i for i in range(start_time, N1 + 1)]

    # Now lets do a stepwise plot
    plt.step(sorted_times, events)
    plt.show()

def Part_B():
    # We have a Pareto distribution with the following parameters
    scale = (1 / 3)
    shape = 3
    
    # Define Poisson rate parameter
    lmda = 10
    
    # Create an instance of the Pareto distribution
    T = np.random.pareto(shape) * scale
    print(T)
    
    # Now we have to determine N(T)
    # By conditioning on T we can treat it as a constant 
    # And plug it into the Poisson Process
    # This means we simulate a Poisson Process
    # With parameter lambda * T
    N2 = np.random.poisson(lmda * T)
    print("\nPart B:")
    print("The number of events that have occurred up until time T is %d" % N2)

def Part_C():
    # Now we must simulate Part B 10,000 times 
    # We have a Pareto distribution with the following parameters                                                                                                                   
    scale = (1 / 3)
    shape = 3

    # Define Poisson rate parameter                                                                                                                                                 
    lmda = 10

    # Make lists to store values of T and N(T)
    T_values = []
    NT_values = []

    # Run simulations
    current_sim = 0
    num_sim = 10000
    
    while current_sim < num_sim:
        # Create an instance of the Pareto distribution                                                                                                                             
        T2 = np.random.pareto(shape) * scale

        # Now we have to determine N(T)                                                                                                                                            
        # By conditioning on T we can treat it as a constant                                                                                                                       
        # And plug it into the Poisson Process                                                                                                                                      
        # This means we simulate a Poisson Process                                                                                                                                  
        # With parameter lambda * T                                                                                                                                                      
        N3 = np.random.poisson(lmda * T2)

        # Append values
        T_values.append(T2)
        NT_values.append(N3)

        # Increment count
        current_sim += 1

    # Determine Cov(T, N(T)) and Var(N(T)) using the variance covariance matrix
    var_cov = np.cov(T_values, NT_values)
    print("\nPart C:")
    print("Here is the Variance Covariance Matrix of T and N(T):")
    print(var_cov)
    print("\nThe value in the top left, %f, is the Variance of T" % var_cov[0][0])
    print("The values in the top right/bottom left, %f, represent the Covariance of T and N(T)" % var_cov[0][1])
    print("The value in the bottom right, %f, is the Variance of N(T)" % var_cov[1][1])

def Part_D():
    # Now we want to find the standard error of the estimates of Cov(T, N(T)) and Var(N(T))
    # Standard error of a quantity is defined as standard deviation of the quantity divided by square root n
    # In order to do this we will run the 10,000 simulations of T and N(T) 100 times
    # And use that for our estimates
    # We have a Pareto distribution with the following parameters                                                                                                                   
    scale = (1 / 3)
    shape = 3

    # Define Poisson rate parameter                                                                                                                                                 
    lmda = 10

    # Make parameters to simulate the simulations
    num_sim_of_sim = 0
    sim_of_sim = 100

    # Keep track of Cov(T, N(T)) and Var(N(T))
    cov_values = []
    var_values = []

    while num_sim_of_sim < sim_of_sim:
        # Make lists to store values of T and N(T)
        T_values = []
        NT_values = []

        # Run simulations
        current_sim = 0
        num_sim = 10000
        
        while current_sim < num_sim:
            # Create an instance of the Pareto distribution                                                                                                                             
            T3 = np.random.pareto(shape) * scale

            # Now we have to determine N(T)                                                                                                                                            
            # By conditioning on T we can treat it as a constant                                                                                                                       
            # And plug it into the Poisson Process                                                                                                                                      
            # This means we simulate a Poisson Process                                                                                                                                  
            # With parameter lambda * T                                                                                                                                                      
            N4 = np.random.poisson(lmda * T3)

            # Append values
            T_values.append(T3)
            NT_values.append(N4)

            # Increment count
            current_sim += 1

        # Determine Cov(T, N(T)) and Var(N(T)) using the variance covariance matrix
        var_cov = np.cov(T_values, NT_values)

        # Extract Cov(T, N(T)) and Var(N(T)) from above matrix
        cov_T_NT = var_cov[0][1]
        var_NT = var_cov[1][1]

        # Append to the lists made earlier
        cov_values.append(cov_T_NT)
        var_values.append(var_NT)

        # Increment count
        num_sim_of_sim += 1

    # Calculate the standard error of Cov(T, N(T)) and Var(N(T))
    cov_stan_error = (math.sqrt(np.mean(abs(cov_values - np.mean(cov_values)) ** 2))) / sim_of_sim
    var_stan_error = (math.sqrt(np.mean(abs(var_values - np.mean(var_values)) ** 2))) / sim_of_sim

    # Print them out
    print("\nPart D:")
    print("Standard Error of Cov(T, N(T)) is %f" % cov_stan_error)
    print("Standard Error of Var(N(T)) is %f" % var_stan_error)


# Call functions
Part_A()
Part_B()
Part_C()
Part_D()