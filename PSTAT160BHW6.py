"""
This is the Python HW 6
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
For this problem we have an M/M/2 server queue
People arrive with a Poisson Process (N(t)) rate of 1
And people are served by any two of the servers with an exponential rate lambda
Let X(t) := number of customers in system at time t
Let Y(t) := number of customers that have departed by time t
For simplicity let us consider two lambda values of 1 and 1/3 and compare them
To observe the effect of the different service rates
"""

def Part_A():
	# Simulate sample path of {X(t), Y(t), 0 <= t <= 100} with lambda = 1
	# Generate Poisson Process (will be Poisson(t) = Poisson(100))
	lmda = 1
	t_start = 0
	t_end = 100
	num_customers = np.random.poisson(lmda * t_end)

	# Since the interarrival times are exponential
	# We can generate uniform random variables
	# Showing when people have arrive
	times = []
	for i in range(0, num_customers):
		time = np.random.uniform(t_start, t_end)
		times.append(time)

	# Now sort said times to get interarrival times
	# Thank god for numpy
	times_sorted = np.sort(times)

	# Now we will simulate the process
	# Loop through interarrival times
	server_1_time = 0
	server_2_time = 0
	server_times = []

	for arrival_time in times_sorted:
		
		# If server 1 will be free by the interarrival time
		# Put em on server 1
		# The overall end time will be the arrival time plus their service time
		# Append to the server 1 times list if t < 100
		if (arrival_time > server_1_time):
			server_1_time = arrival_time + np.random.exponential(lmda)
			if server_1_time < t_end:
				server_times.append(server_1_time)

		# If server 2 will be free by the interarrival time
		# Put em on server 2
		# The overall end time will be the arrival time plus their service time
		# Append to the server 2 times list if t < 100
		elif (arrival_time > server_2_time):
			server_2_time = arrival_time + np.random.exponential(lmda)
			if server_2_time < t_end:
				server_times.append(server_2_time)

		# Otherwise...
		else:
			# If server 1 has the minimum completition time
			# Append to the server 1 times list if t < 100
			if server_1_time < server_2_time:
				server_1_time += np.random.exponential(lmda)
				if server_1_time < t_end:
					server_times.append(server_1_time)
			# If server 2 has the minimum completition time
			# Append to the server 2 times list of t < 100
			else:
				server_2_time += np.random.exponential(lmda)
				if server_2_time < t_end:
					server_times.append(server_2_time)


	# Generate Yt and plot it
	Yt = [i for i in range(t_start, len(server_times))]
	t_cust_leaves = sorted(server_times)
	plt.step(t_cust_leaves, Yt)
	plt.show()

	# Generate Xt
	index_n = 0
	index_y = 0
	t_cust_arrives = times_sorted
	total_times = []
	Xt = []
	cust_in_sys = 0
	# Loop through things and keep track of shit
	while (index_n < len(t_cust_arrives) and index_y < len(t_cust_leaves)):
		if (t_cust_arrives[index_n] < t_cust_leaves[index_y]):
			total_times.append(t_cust_arrives[index_n])
			index_n += 1
			cust_in_sys += 1
			Xt.append(cust_in_sys)

		else:
			total_times.append(t_cust_leaves[index_y])
			index_y += 1
			cust_in_sys -= 1
			Xt.append(cust_in_sys)

	# Put both things together
	tXt = [total_times, Xt]
	# Sort times (in the 0 index for column)
	tXt_sorted = sorted(tXt, key = lambda x: x[0])

	# Graph it
	plt.bar(tXt_sorted[0], tXt_sorted[1])
	plt.show()
	
	print("\nPart A:")
	print("Number of customers that arrived in time 0 --> 100 is %d" % num_customers)
	print("Number of customers that have left by time t = 100 are %d" % len(server_times))
	print("Number of customers that are still in the system by time t = 100 are %d" % (num_customers - len(server_times)))


def Part_B():
	# Simulate sample path of {X(t), Y(t), 0 <= t <= 100} with lambda = 1/3
	# Generate Poisson Process (will be Poisson(t) = Poisson(100))
	lmda = (1 / 3)
	t_start = 0
	t_end = 100
	num_customers = np.random.poisson(lmda * t_end)

	# Since the interarrival times are exponential
	# We can generate uniform random variables
	# Showing when people have arrive
	times = []
	for i in range(0, num_customers):
		time = np.random.uniform(t_start, t_end)
		times.append(time)

	# Now sort said times to get interarrival times
	# Thank god for numpy
	times_sorted = np.sort(times)

	# Now we will simulate the process
	# Loop through interarrival times
	server_1_time = 0
	server_2_time = 0
	server_times = []

	for arrival_time in times_sorted:
		
		# If server 1 will be free by the interarrival time
		# Put em on server 1
		# The overall end time will be the arrival time plus their service time
		# Append to the server 1 times list if t < 100
		if (arrival_time > server_1_time):
			server_1_time = arrival_time + np.random.exponential(lmda)
			if server_1_time < t_end:
				server_times.append(server_1_time)

		# If server 2 will be free by the interarrival time
		# Put em on server 2
		# The overall end time will be the arrival time plus their service time
		# Append to the server 2 times list if t < 100
		elif (arrival_time > server_2_time):
			server_2_time = arrival_time + np.random.exponential(lmda)
			if server_2_time < t_end:
				server_times.append(server_2_time)

		# Otherwise...
		else:
			# If server 1 has the minimum completition time
			# Append to the server 1 times list if t < 100
			if server_1_time < server_2_time:
				server_1_time += np.random.exponential(lmda)
				if server_1_time < t_end:
					server_times.append(server_1_time)
			# If server 2 has the minimum completition time
			# Append to the server 2 times list of t < 100
			else:
				server_2_time += np.random.exponential(lmda)
				if server_2_time < t_end:
					server_times.append(server_2_time)


	# Generate Yt and plot it
	Yt = [i for i in range(t_start, len(server_times))]
	t_cust_leaves = sorted(server_times)
	plt.step(t_cust_leaves, Yt)
	plt.show()

	# Generate Xt
	index_n = 0
	index_y = 0
	t_cust_arrives = times_sorted
	total_times = []
	Xt = []
	cust_in_sys = 0
	# Loop through things and keep track of shit
	while (index_n < len(t_cust_arrives) and index_y < len(t_cust_leaves)):
		if (t_cust_arrives[index_n] < t_cust_leaves[index_y]):
			total_times.append(t_cust_arrives[index_n])
			index_n += 1
			cust_in_sys += 1
			Xt.append(cust_in_sys)

		else:
			total_times.append(t_cust_leaves[index_y])
			index_y += 1
			cust_in_sys -= 1
			Xt.append(cust_in_sys)

	# Put both things together
	tXt = [total_times, Xt]
	# Sort times (in the 0 index for column)
	tXt_sorted = sorted(tXt, key = lambda x: x[0])

	# Graph it
	plt.bar(tXt_sorted[0], tXt_sorted[1], )
	plt.show()
	
	print("\nPart B:")
	print("Number of customers that arrived in time 0 --> 100 is %d" % num_customers)
	print("Number of customers that have left by time t = 100 are %d" % len(server_times))
	print("Number of customers that are still in the system by time t = 100 are %d" % (num_customers - len(server_times)))

def Part_C():
	# Simulate the sample path long enough to 
	# estimate the stationary distribution of 
	# {X(t), t >= 0} with lambda = 1 .
	lmda = 1
	t_start = 0
	t_end = 100
	num_customers = np.random.poisson(lmda * t_end)

	# Since the interarrival times are exponential
	# We can generate uniform random variables
	# Showing when people have arrive
	times = []
	for i in range(0, num_customers):
		time = np.random.uniform(t_start, t_end)
		times.append(time)

	# Now sort said times to get interarrival times
	# Thank god for numpy
	times_sorted = np.sort(times)

	# Now we will simulate the process
	# Loop through interarrival times
	server_1_time = 0
	server_2_time = 0
	server_times = []

	for arrival_time in times_sorted:
		
		# If server 1 will be free by the interarrival time
		# Put em on server 1
		# The overall end time will be the arrival time plus their service time
		# Append to the server 1 times list if t < 100
		if (arrival_time > server_1_time):
			server_1_time = arrival_time + np.random.exponential(lmda)
			if server_1_time < t_end:
				server_times.append(server_1_time)

		# If server 2 will be free by the interarrival time
		# Put em on server 2
		# The overall end time will be the arrival time plus their service time
		# Append to the server 2 times list if t < 100
		elif (arrival_time > server_2_time):
			server_2_time = arrival_time + np.random.exponential(lmda)
			if server_2_time < t_end:
				server_times.append(server_2_time)

		# Otherwise...
		else:
			# If server 1 has the minimum completition time
			# Append to the server 1 times list if t < 100
			if server_1_time < server_2_time:
				server_1_time += np.random.exponential(lmda)
				if server_1_time < t_end:
					server_times.append(server_1_time)
			# If server 2 has the minimum completition time
			# Append to the server 2 times list of t < 100
			else:
				server_2_time += np.random.exponential(lmda)
				if server_2_time < t_end:
					server_times.append(server_2_time)


	# Generate Yt and plot it
	Yt = [i for i in range(t_start, len(server_times))]
	t_cust_leaves = sorted(server_times)

	# Generate Xt
	index_n = 0
	index_y = 0
	t_cust_arrives = times_sorted
	total_times = []
	Xt = []
	cust_in_sys = 0
	# Loop through things and keep track of shit
	while (index_n < len(t_cust_arrives) and index_y < len(t_cust_leaves)):
		if (t_cust_arrives[index_n] < t_cust_leaves[index_y]):
			total_times.append(t_cust_arrives[index_n])
			index_n += 1
			cust_in_sys += 1
			Xt.append(cust_in_sys)

		else:
			total_times.append(t_cust_leaves[index_y])
			index_y += 1
			cust_in_sys -= 1
			Xt.append(cust_in_sys)

	
	# Make list of frequencies
	freq = [0] * (len(Xt) - 1)
	for xt in Xt:
		freq[xt] += 1

	# Make list of numbers
	num = [i for i in range(0, len(Xt) - 1)]

	# Graph to get probability distribution
	# Set axes limits (most of the x values will be at 0)
	axes = plt.gca()
	axes.set_xlim([0, 10])
	plt.plot(num, freq)
	plt.show()

	# Here's a bar graph showing the approximate numbers
	plt.bar(num, freq)
	plt.show()

# Execute functions
Part_A()
Part_B()
Part_C()


