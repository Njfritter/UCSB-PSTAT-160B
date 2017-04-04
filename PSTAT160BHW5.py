"""
This is the Python HW 5
for PSTAT 160B
Prof Ichiba 
TA: Mousavi
Section: W 1:00 - 1:50pm
"""

# Import libraries
from __future__ import division
import random
import math
import matplotlib.pyplot as plt
import numpy as np

# In the class we see the simple symmetric random walk approximates the standard Brownian motion

def Part_A():
	# Simulate a Brownian motion-like sample path
	# Graphing (ti, U(ti)) from i = 0, 1, ... N where 2 ^ N
	# Where ti := i / N
	# And U(ti) = sum of iid normal random variables with mean 0 and variance 1 / N 
	# Define constants
	N = (2 ** 10)
	mean = 0
	var = (1 / N)
	sd = math.sqrt(var)
	Ti = [0] # Initialize first time as zero
	values = [0] # Initialize the first point as zero

	# Loop through 0 to N
	# Get time values and generate iid normal random variables
	for i in range(1, N):
		Ti.append(i / N)
		cospi = np.random.normal(mean, sd)
		values.append(cospi)

	# Get the cumulative sum and save as a list
	# Thank you numpy
	# These U(ti) values represent B(ti) values
	UTi = np.cumsum(values)

	# Plot the sample path
	plt.plot(Ti, UTi)
	plt.show()

def Part_B():
	#  Repeat this simulation 10000 times to estimate the joint probability
	# P((max B(s) from (0 <= s <= 1) > b), B(1) < a) for b >= a, b >= 0
	# Can choose appropriate range of (b, a)
	# Here a = 0, b = 2
	a = 0
	b = 1
	count = 0

	num_sim = 10000
	current_sim = 0
	# Define constants (taken from part A)
	N = (2 ** 10)
	mean = 0
	var = (1 / N)
	sd = math.sqrt(var)

	# Run simulations
	while current_sim < num_sim:
		# Taken from part A
		Ti = [0] # Initialize first time as zero
		values = [0] # Initialize the first point as zero

		# Loop through 0 to N
		# Get time values and generate iid normal random variables
		for i in range(1, N):
			Ti.append(i / N)
			cospi = np.random.normal(mean, sd)
			values.append(cospi)

		# Get the cumulative sum and save as a list
		# Thank you numpy
		# These U(ti) values represent B(ti) values
		UTi = np.cumsum(values)

		# Check conditions: if max value is greater than b
		# And if the last value is less than a
		# If so increment the count
		maximum = max(UTi)
		last_point = UTi[-1]
		if maximum > b and last_point < a:
			count += 1

		# Increment count
		current_sim += 1

	# Print the probability
	prob = count / num_sim
	print("Part B:")
	print("The probability that P((max B(s) from (0 <= s <= 1) > b), B(1) < a) for b >= a, b >= 0 is %f" %prob)

def Part_C():
	# Let us denote T by the uniform random variable on the unit interval [0, 1] 
	# independent of Brownian motion. 
	# As in part b, estimate the tail probability P(|B(T)| >= x) ; x > 0

	# First we'll repeat Part A
	# Simulate a Brownian motion-like sample path
	# Graphing (ti, U(ti)) from i = 0, 1, ... N where 2 ^ N
	# Where ti := i / N
	# And U(ti) = sum of iid normal random variables with mean 0 and variance 1 / N 
	# Define constants
	N = (2 ** 10)
	mean = 0
	var = (1 / N)
	sd = math.sqrt(var)
	Ti = [0] # Initialize first time as zero
	values = [0] # Initialize the first point as zero
	# Pick a value for x, x > 0
	x = 0.5

	num_sim = 1000
	current_sim = 0
	count = 0

	# Run simulations
	while current_sim < num_sim:
		# Taken from part A
		# Loop through 0 to N
		# Get time values and generate iid normal random variables
		for i in range(1, N):
			Ti.append(i / N)
			cospi = np.random.normal(mean, sd)
			values.append(cospi)

		# Get the cumulative sum and save as a list
		# Thank you numpy
		# These U(ti) values represent B(ti) values
		UTi = np.cumsum(values)

		# Generate uniform random variable
		T = np.random.uniform(0, 1)

		# Since time is linear and represents a proportion from 0 to 1
		# And t(0) corresponds to B(0), t(N) corresponds to B(N)
		# t(T) corresponds to B(T * N)
		TN = math.floor(T * N)

		# Now we index B(s) (or UTi) for the appropropriate value with T plugged in
		# We want the absolute value as well
		BT = abs(UTi[TN])

		# Check if the the absolute value is greater than x
		if BT > x:
			count += 1

		# Increment count 
		current_sim += 1
		if current_sim % 100 == 0:
			print(current_sim)

	# Print results
	prob = count / num_sim
	print("Part C:")
	print("Our estimate of the tail probability P(|B(T)| >= x) ; x > 0 is %f" %prob)



Part_A()
Part_B()
Part_C()
