"""
This is the Python HW 3
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

def Part_A():

	# We can simulate the arrival times of each event in the non-homogenous Poisson Process
	# By generating exponential RVs with mean 1 (T1,....Tn)
	# Here Ti = m(Si), so T is
	T = [] 
	T.append(np.random.exponential(1))

	# By inverting the m function we can find Si
	# Therefore Si = m^-1(Ti)
	# Here m(t) = 4log(1 + t)
	# m^-1(t) = (exp(m(Si) / 4)) - 1 = (exp(Ti / 4))
	# Because Ti is m(Si)
	S = []
	S.append(np.exp(T[0] / 4) - 1)

	for i in range(0, 10000):
		if S[i] > 10:
			break

		Ti = T[i]
		nextTi = Ti + np.random.exponential(1)
		T.append(nextTi)
		Si = np.exp(nextTi / 4) - 1
		S.append(Si)

	events = [i for i in range(0, len(S))]
	plt.step(S, events)
	plt.show()
	

def Part_B():
	# Repeat part A 10,000 times to estimate 
	# E[T1] and Var(T1)
	# Where T1 is the first event time
	n0 = 0
	n = 10000
	T1 = []

	while n0 < n:
		# We can simulate the arrival times of each event in the non-homogenous Poisson Process
		# By generating exponential RVs with mean 1 (T1,....Tn)
		# Here Ti = m(Si), so T is
		T = [] 
		T.append(np.random.exponential(1))

		# By inverting the m function we can find Si
		# Therefore Si = m^-1(Ti)
		# Here m(t) = 4log(1 + t)
		# m^-1(t) = (exp(Ti / 4)) - 1
		# Because Ti is Si evaluated in m
		S = []
		S.append(np.exp(T[0] / 4) - 1)

		for i in range(0, 1000):
			if S[i] > 10:
				break

			Ti = T[i]
			nextTi = Ti + np.random.exponential(1)
			T.append(nextTi)
			Si = np.exp(nextTi / 4) - 1
			S.append(Si)

		T1.append(T[0])

		# Increment count 
		n0 += 1

	# Now estimate E[T1] and Var[T1]
	ET1 = np.mean(T1)
	VarT1 = np.var(T1)

	print("\nPart B:")
	print("Our estimate of E[T1] is: %f" % ET1)
	print("Our estimate of Var[T1] is: %f" % VarT1)
	

def Part_C():
	# Simulate a sample path of a non-homogenous Poisson Process 
	# Whose mean value function is given by m(t) = t^2 + 2t
	# From 0 <= t <= 10
	# We can simulate the arrival times of each event in the non-homogenous Poisson Process
	# By generating exponential RVs with mean 1 (T1,....Tn)
	# Here Ti = m(Si), so T is
	T = [] 
	T.append(np.random.exponential(1))

	# By inverting the m function we can find Si
	# Therefore Si = m^-1(Ti)
	# Here m(t) = t^2 + 2t
	# m^-1(t) = -1 (+-) sqrt(m(Si) + 1) = -1 + sqrt(Ti + 1)
	# Because Ti is Si evaluated in m
	# And we disregard the negative t values 
	S = []
	S.append(-1 + np.sqrt(T[0] + 1))

	for i in range(0, 10000):
		if S[i] > 10:
			break

		Ti = T[i]
		nextTi = Ti + np.random.exponential(1)
		T.append(nextTi)
		Si = (-1 + np.sqrt(nextTi + 1))
		S.append(Si)

	events = [i for i in range(0, len(S))]
	plt.step(S, events)
	plt.show()
	

def Part_D():
	# Repeat Part C sufficiently many times
	# To obtain a good estimate of the probability
	# That exactly 5 events occur between time t = 4 and t = 5
	# Copied from Part C above
	n = 10000
	n0 = 0
	count = 0

	while n0 < n:
		# We can simulate the arrival times of each event in the non-homogenous Poisson Process
		# By generating exponential RVs with mean 1 (T1,....Tn)
		# Here Ti = m(Si), so T is
		T = [] 
		T.append(np.random.exponential(1))

		# By inverting the m function we can find Si
		# Therefore Si = m^-1(Ti)
		# Here m(t) = t^2 + 2t
		# m^-1(t) = -1 (+-) sqrt(m(Si) + 1) = -1 + sqrt(Ti + 1)
		# Because Ti is Si evaluated in m
		# And we disregard the negative t values 
		S = []
		S.append(-1 + np.sqrt(T[0] + 1))

		# Make counter for events between times t = 4 and t = 5
		events4to5 = 0

		for i in range(0, 10000):
			if S[i] > 10:
				break

			# Keep track of the number of events between time t = 4 and t = 5
			if S[i] > 4 and S[i] < 5:
				events4to5 += 1 

			Ti = T[i]
			nextTi = Ti + np.random.exponential(1)
			T.append(nextTi)
			Si = (-1 + np.sqrt(nextTi + 1))
			S.append(Si)

		# Check if the number of events between time t = 4 and t = 5 equals 5
		if events4to5 == 5:
			count += 1
		
		# Increment count
		n0 += 1

	# Now let's see how often this happens
	# *whispers* probably not often
	prob = count / n
	print("\nPart D:")
	print("The probability that exactly 5 events will occur between time t = 4 and t = 5 is %f" % prob)


# Call functions
Part_A()
Part_B()
Part_C()
Part_D()