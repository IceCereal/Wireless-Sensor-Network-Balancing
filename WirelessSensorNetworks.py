"""
	Implement a shuffled complex evolution algorithm to balancing loads on gateways in Wireless Sensor Networks
	$ Design and Analysis of Algorithms
"""

### INPUT:
### 12 sensors: [Each sensor has gateways it falls under]

sensors = [	[0, 1],
		[1, 2, 3],
		[0, 3],
		[1, 2],
		[0, 3],
		[0, 1, 3],
		[1, 3],
		[1, 2],
		[0, 1, 2, 3],
		[0, 2],
		[0, 1, 2],
		[0, 2, 3]
	]

print ("Sensors & their Gateways:")

for i in range(len(sensors)):
	print (i, '\t', sensors[i])

### CHECK:
### Whether Sensors > Gateways

maxGateway = 0

for i in range(len(sensors)):
	if max(sensors[i]) > maxGateway:
		maxGateway = max(sensors[i])

if maxGateway > len(sensors):
	print ("There are more gateways than the number of sensors")
	print ("Exit")
	exit()

### Define:
### Genetic/Evolutionary algorithms vars

popSize = 12	# Population Size

def Fitness(child, load = None, gamma = None):
	"""
		Fitness Function
		
		params:
			child (list):	Evaluate fitness on this child
			load (list):	The Load on every Gateway: defaults to [30, 14, 20, 8]
			gamma (int):	The constant: defaults to 0.25

		returns:
			fitness (int):	The fitnes of the child
	"""

	mean = 0	# Mean of the Loads
	gamma = 0	# Gamma (a constant)
	Load = []	# Loads on each Gateway. Can also be (num_bits * %_energy_in_gateway)
	T_upper = 0	# Upper Threshold for granted number of gateways (mean + gamma*mean)
	T_lower = 0	# Lower Threshold for granted number of gateways (mean - gamma*mean)
	Load_Ratio = []	# Defined per each Gateway. Load_of_current_gateway / Highest_load
	Exp_GLoad = 0 	# Expected Gateway Load = Sigma(Load_Ratio)/ Number_of_Gateways

	Fitness = 0	# Fitness Function = Exp_GLoad * Num_Granted_Gateways / Number_of_Gateways

	if load == None:
		load = [30, 14, 20, 8]
	if gamma == None:
		gamma = 0.25
	
