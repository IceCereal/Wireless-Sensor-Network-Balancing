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

print ("Sensors & their Gateways::")

for i in range(len(sensors)):
	print (i, '\t', sensors[i])