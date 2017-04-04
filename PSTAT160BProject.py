"""
This is the Option Python Project
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
from collections import OrderedDict

# Problem 1, Homework 6
"""
A job shop consists of three machines and two repairmen. The amount of time a machine
works before breaking down is exponentially distributed with mean 10. If the amount of time it
takes a single repairman to fix a machine is exponentially distributed with mean 8, then (a) what
is the average number of machines not in use? (b) what proportion of time are both repairmen
busy?
"""

class Machine:
	def __init__(self):
		#self.broken_down = []
		self.is_broken = 0
		self.last_repaired = 0
		self.breakdown = 10
		self.breaktime = None
		self.fix = 8
		self.repairtime = None

	def update(self, time, num_workers):
		# Update broken_down
		if time == 0:
			self.breakdown = self.calc_breaktime()

		# Check broken machines
		if self.is_broken:
			print("Yeah Boyyyyyyyyyyyyyyyyyyyyyyyyyyyy")

			# If machine is broken but nobody was available to fix it :-(
			if not self.repairtime:
				# Calculate new repairtime if there are workers available
				if num_workers > 0:
					self.repairtime = self.calc_repairtime() + time

			# If there IS a worker available to fix it
			# If we are past the end time of repair
			elif time >= self.repairtime:
				# Calculate new breaktime
				self.breaktime = self.calc_breaktime() + time
				# Change is_broken back to zero
				self.is_broken = 0
				# Set to None
				self.repairtime = None

		else:
			# This is what killz da machine
			if time >= self.breaktime:
				# Change is_broken to 1 to signify brokenness
				self.is_broken = 1
				# Set to None
				self.breaktime = None

	def calc_breaktime(self):
		# Calculate breaktime
		return np.random.exponential(self.breakdown)

	def calc_repairtime(self):
		# Calculate repairtime
		return np.random.exponential(self.fix)


def Part_A():
	# Find the average number of machines not in use
	# Define constants
	machines = 3
	repairmen = 2
	fix = 8
	breakdown = 10
	# "States" will represent the number of machines not in use
	states = [0, 1, 2, 3]

	# Going from 0 --> 1 --> 2 --> 3
	# lambda_0 = 3 * (1/10) = 3/10, lambda_1 = 2 * (1/10) = 2/10, lambda_2 = 1/10
	# mu_1 = 1/8, mu_2 = 2 * (1/8) = 2/8, mu_3 = 2 * (1/8) = 2/8

	# For the sake of this problem we will assume that we start with 3 working machines
	# Since this is a stochastic process it does not matter which state we start in
	# Now let's run 1000 simulations of this
	
	states = OrderedDict({0:0})
	available_workers = 2
	time_steps = 1000
	increment = 0.01
	machine1 = Machine()
	machine2 = Machine()
	machine3 = Machine()
	machines = [machine1, machine2, machine3]

	for t in np.arange(0, time_steps, increment):
		broken_machines = 0
		for m in machines:
			m.update(t, available_workers)
			broken_machines += m.is_broken
			if broken_machines >= 2:
				available_workers = 0
			else:
				available_workers = 2 - broken_machines

		states[t] = broken_machines
		if t % 1 == 0:
			print(t)

	sums = [0, 0, 0, 0]
	for state in states.values():
		sums[state] += increment

	proportions = []
	for num in sums:
		proportions.append(num / time_steps)

	print(sums)
	print(proportions)

	# Calculate the average number of machines not in use
	avg_broken = 0
	index = 0
	for prop in proportions:
		avg_broken += (index * prop)
		index += 1

	print("Average number of machines not in use is %f" % avg_broken)
	# Call Part B
	Part_B(proportions)

def Part_B(proportions):
	# Now calculate the proporition of time both repairmen busy
	both_repairmen_busy = proportions[2] + proportions[3]
	# Since the indexes match the number of machines broken
	print("Proportion of time both repairmen are busy is %f" % both_repairmen_busy)

Part_A()



