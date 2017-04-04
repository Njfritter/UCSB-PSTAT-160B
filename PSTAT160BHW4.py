"""
This is the Python HW 4
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

# In this exercise we shall simulate the two-dimensional Poisson process 
# (Poisson Point Process in the plane and its subsets such as a square and a disc).

def Part_A():
	# In the setup of the above Problem 1 simulate the two-dimensional Poisson process 
	# in the rectangle region [-1, 1] x [-1, 1]. Choose lambda appropriately

	# So the area of this region corresponds to -1 < x < 1 & -1 < y < 1
	# The length of the x values is 2, as well as for the y values
	# Therefore the area of this region is 2 x 2 = 4
	length = 2
	width = 2
	area = length * width

	# Choose lambda appropriately?
	# Cash me oussside how bout dat?
	lmda = 1

	# Generate randomly occurring event
	# Because this is continuous intensity
	# I assume this is a homogenous Poisson Process
	NT = np.random.poisson(area * lmda)

	random_points = []

	for i in range(0, NT + 1):
		random_point = np.random.uniform(-1, 1)
		random_points.append(random_point)

	sorted_points = sorted(random_points)
	events = [i for i in range(0, NT + 1)]

	# Now lets do a stepwise plot
	plt.step(sorted_points, events)
	plt.show()

def Part_B():
	# Simulate the two-dimensional Poisson process in a circular region (disc) of radius 1 and
	# of center at the origin (0, 0)
	radius = 1
	area = math.pi * (radius ** 2)

	# Choose lambda appropriately?
	# Cash me oussside how bout dat?
	lmda = 1

	# Generate randomly occurring event
	# Because this is continuous intensity
	# I assume this is a homogenous Poisson Process
	NT = np.random.poisson(area * lmda)

	random_points = []

	for i in range(0, NT + 1):
		random_point = np.random.uniform(-1, 1)
		random_points.append(random_point)

	sorted_points = sorted(random_points)
	events = [i for i in range(0, NT + 1)]

	# Now lets do a stepwise plot
	plt.step(sorted_points, events)
	plt.show()

def Part_C():
	# Estimate the cumulative distribution function F(x) := P(R1 <= x) of R1 for every
	# 0 <= x <= c1 (cf. section 11.5.2) and plot the function F(dot) for 0 <= x <= c1 , where c1 is
	# chosen large enough to represent the whole shape of the function F(dot).x
	radius = 1
	overall_area = math.pi * (radius ** 2)
	lmda = 1

	# Simulate a Poisson Process
	NT = np.random.poisson(overall_area * lmda)
	random_points = []

	# Generate uniform random variable as the points
	# We will take the absolute value of them
	# As we are looking at Euclidean distance
	# So we only care about magnitude
	for i in range(0, NT + 1):
		random_point = np.random.uniform(-1, 1)
		random_points.append(abs(random_point))

	# Iterate through many values of x as "current_radius"
	# Assuming the points in the Poisson Process are uniformly distributed
	# There is a uniform chance the points will be within the radius of the circle
	# Thus if we calculate the area for each successive radius value
	# This acts as the value of the CDF
	# Because the increasing circle contains all radius values smaller in magnitude
	# Now let's declare our parameters and counters
	cum_prob = []
	for i in range(0, len(random_points)):
		disc_area = lmda * (math.pi * (random_points[i] ** 2))
		disc_prob = disc_area / (lmda * overall_area)
		cum_prob.append(disc_prob)

	# Now we sort the points & probabilities to get it in the proper order
	sorted_points = sorted(random_points)
	sorted_probs = sorted(cum_prob)

	print(sorted_points)
	print(sorted_probs)
	# Now lets do a  plot
	plt.plot(sorted_points, sorted_probs)
	plt.show()

def Part_D():
	# Estimate the tail probability Gn(x) := P(Rn > x) for x > 0 , 0 <= x <= c2 , where c2 is
	# chosen large enough to represent the whole shape of function Gn(dot) for n = 1, 2, 3, 4 . Plot
	# the function Gn(dot) for n = 1, 2, 3, 4 in the same graph.
	# First we declare our parameters and counters
	radius = 1
	overall_area = math.pi * (radius ** 2)
	lmda = 1

	# Simulate a Poisson Process
	NT = np.random.poisson(overall_area * lmda)
	random_points = []

	# Generate uniform random variable as the points
	# We will take the absolute value of them
	# As we are looking at Euclidean distance
	# So we only care about magnitude
	for i in range(0, NT + 1):
		random_point = np.random.uniform(-1, 1)
		random_points.append(abs(random_point))

	cum_prob = []

	# Here I will generate the same numbers as in Part C
	# But take the compliment of the probabilities
	# This way we will get the "survival function" rather than the CDF
	# Which is equal to P(Rn > x)
	# The same principles I mentioned in Part C work for Part D
	for i in range(0, len(random_points)):
		disc_area = lmda * (math.pi * (random_points[i] ** 2))
		disc_prob = 1 - (disc_area / (lmda * overall_area))
		cum_prob.append(disc_prob)

	# Now we sort the points ascending
	# And the probabilities descending
	sorted_points = sorted(random_points)
	sorted_probs = sorted(cum_prob, reverse = True)

	print(sorted_points)
	print(sorted_probs)
	# Now lets do a  plot
	plt.plot(sorted_points, sorted_probs)
	plt.show()


Part_A()
Part_B()
Part_C()
Part_D()