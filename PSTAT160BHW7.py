"""
This is the Python HW 7
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

"""
A coin that comes up heads (H) with probability p between 0 and 1 
and tails(T) with probability 1 - p is continually flipped
"""

def Part_A():
	# Using simulation, find expected number  of flips until either sequence
	# THHT or sequence TTT occurs for each p
	# And show graph as a function of p between 0 and 1
	# Make lists to store p values, expected counts and sequences
	seq_THHT = [0, 1, 1, 0]
	seq_TTT = [0, 0, 0]
	p_values = []
	exp_counts = []
	num_sim = 1000
	# Loop through various values between 0 and 1
	for i in range(1, 20):
		exp_flips = 0
		# Keep track of p value
		p = (i / 20)
		p_values.append(p)
		# Do 1000 simulations
		for j in range(0, num_sim):
			# Set counter for number of flips for each trial
			seq = []
			# Provide 1000 number sequences
			for k in range(0, num_sim):
				# We're gonna using the binomial call with n = 1
				bern_rv = np.random.binomial(1, p)
				# Therefore we will get the outcome 1 with probability p
				# Thus 1 represents Heads (H) and 0 represents Tails (T)
				# Which is consistent with above sequences
				# Append the random variable
				seq.append(bern_rv)
			# Go through sequence and check for either sequence
			for l in range(0, len(seq)):
				# Sequence matches the first sequence
				if seq[l:l + len(seq_THHT)] == seq_THHT:
					# Append the index + 1 at the end of sequence
					num_flips = l + len(seq_THHT) + 1
					exp_flips += num_flips
					# End loop
					break
				# Sequence matches second sequence
				if seq[l:l + len(seq_TTT)] == seq_TTT:
					num_flips = l + len(seq_TTT) + 1
					# Append the index + 1 at the end of sequence
					exp_flips += num_flips
					# End loop
					break
		# Get expected number of flips
		exp_counts.append(exp_flips / num_sim)

	# Now graph stuff
	plt.plot(p_values, exp_counts)
	plt.show()

def Part_B():
	# Using simulation, find probability that TTT occurs first in A
	# When p = 0.7
	# Display sequences
	seq_THHT = [0, 1, 1, 0]
	seq_TTT = [0, 0, 0]
	num_sim = 1000
	p = 0.7
	TTT_first = 0

	# Taken from part above
	# Do 1000 simulations
	for j in range(0, num_sim):
		# Set counter for number of flips for each trial
		seq = []
		# Provide 1000 number sequence
		for k in range(0, num_sim):
			# We're gonna using the binomial call with n = 1
			bern_rv = np.random.binomial(1, p)
			# Therefore we will get the outcome 1 with probability p
			# A 0 represents a Tails, a 1 represents Heads
			# Append the random variable
			seq.append(bern_rv)
		# Go through sequence and check for either sequence
		for l in range(0, len(seq)):
			# Sequence matches second sequence
			if seq[l:l + len(seq_TTT)] == seq_TTT:
				TTT_first += 1
				# End loop
				break
			# Sequence matches first sequence
			if seq[l:l + len(seq_THHT)] == seq_THHT:
				# End loop
				break
	# Calculate probability
	prob = TTT_first / num_sim
	print("The probability that TTT occurs first in a %d number sequence is %f" % (num_sim, prob))


Part_A()
Part_B()







