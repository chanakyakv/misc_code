import math
# Calculate all points of land given distance and orientation to next point 

# # Santhosh-Survey-161
# lat1=13.4055860
# lon1=78.0193340
# # d=68.5
# # θ = 4.416103311502732
# d=[68.50000000, 42.13327148, 73.30148313, 117.39473095, 89.41867278, 140.99085621, 94.60210018, 407.03331761, 97.02905519, 74.41843978]
# θ=[4.41610331,  2.2524052,  -72.8533002, -40.7526524,  -67.2035655, -85.4057398,  -155.9003152, 132.8531797,  17.1559075,  87.2280825]

# Santhosh-Survey-161 - Orientation adjusted as per Village Map - -1.9080879 Degrees anti-clock-wise rotation
lat1=13.4055860
lon1=78.0193340
# d=68.5
# θ = 4.416103311502732
d=[68.50000000, 42.13327148, 73.30148313, 117.39473095, 89.41867278, 140.99085621, 94.60210018, 407.03331761, 97.02905519, 74.41843978]
θ=[2.50801538,  0.3443172,  -74.7613881, -42.6607404,  -69.1116534,  -87.3138277, -157.8084031, 130.9450918,  15.2478196,  85.3199946]

# # Village-Map-161
# lat1=13.4055860
# lon1=78.0193340
# d=[61.64170172, 49.25050271, 75.41848538, 118.1029134, 90.48648619, 139.9315259, 95.6321864, 407.9748, 97.86765597, 73.97281644]
# θ=[2.89043207, 1.68131751, -75.86737817, -41.77727553, -70.07485861, -86.91692523, -158.3377401, -229.0549082, 15.09546134, 85.26713635]

# # Village Map 160
# lat1=13.40468157
# lon1=78.01841703
# d=[407.9748, 226.1693121, 413.5059905, 181.8331197]
# θ=[-49.05490824, -159.1601384, -235.8967943, 14.72726398]

# # Village Map 159
# lat1=13.4055860
# lon1=78.0193340
# d=[73.97281644, 97.86765597, 181.8331197, 214.1686841, 207.4622137, 53.89180799, 135.9456098, 74.97507427]
# θ=[-94.73286365, -164.9045387, -165.272736, -236.6089027, 17.04651178, 18.31828205, -16.01657151, -79.12583612]

# # Village Map 189
# lat1=13.4055860
# lon1=78.0193340
# d=[
# 	74.97507427, 41.03987563, 65.25602483, 117.0907535, 61.64170172
# ]
# θ=[
# 	-259.1258361, -260.2678979, 4.2147498, -81.37217537, -177.1095679
# ]

# # Village Map 129
# lat1=13.4061395
# lon1=78.01936273
# d=[
# 	49.25050271, 75.41848538, 118.1029134, 90.48648619, 139.9315259, 95.6321864, 226.1693121, 95.67853869, 93.46722266, 196.2701952, 43.6847399, 446.2683623, 42.55789285, 69.14383169, 97.15943851, 123.3145472, 87.28352849, 23.3226813, 26.76689947, 38.53399484, 27.64223073, 57.56593017, 38.87802191, 72.49485187, 60.35223234, 74.42063193, 23.05602525, 102.806671, 54.37546393, 20.02354508, 75.68913015, 17.57840888, 70.30697392, 48.4948214, 17.08455102, 59.30652082, 16.43427955, 72.3053591, 65.8388738, 19.715784, 106.4240067, 15.12679405, 29.75588358, 111.4654567, 259.1678417, 61.08943139, 135.9456098, 41.03987563, 65.25602483, 117.0907535
# ]
# θ=[
# 	1.68131751, -75.86737817, -41.77727553, -70.07485861, -86.91692523, -158.3377401, -159.1601384, -59.15656381, 21.07736097, -1.85232243, 87.10968264, -263.7005537, -178.0357136, -246.5966098, -245.6223879, -242.8245378, -181.1115537, -259.7811586, 82.32802872, 63.94273112, -170.598753, -257.739095, 10.87853947, -265.2379015, 13.52077722, -83.46995343, 5.61940171, -257.7480022, -165.5747223, -116.7982514, -175.1520307, -264.4743053, 40.5606578, 61.25550156, -7.07477323, 76.1893177, -234.9493674, -143.0837568, -171.5477334, -257.5990413, -174.3894655, -77.32391538, -162.4690602, -78.0981425, -78.0981425, -78.0981425, -16.01657151, -260.2678979, 4.2147498, -81.37217537
# ]

# # Village Map 196
# lat1=13.40369178
# lon1=78.02325501
# d=[
# 	64.81937764, 46.6375602, 82.24820861, 49.62420633, 84.27573471, 16.38424661
# ]
# θ=[
# 	-265.8025624, 71.25108798, -17.83475375, -84.31911036, -156.1348435, -179.5079732
# ]

# # Village Map 197
# lat1=13.4042852
# lon1=78.02036059
# d=[
# 	53.89180799, 66.01821481, 50.49786505, 61.08943139
# ]
# θ=[
# 	-161.681718, -260.763322, 13.22407899, -78.0981425
# ]

def get_next_lat_long(lat1, lon1, d, θ):
	R = 6372.795477598e3
	R = 6376.997e3
	lat2 = math.degrees( math.asin( math.sin(math.radians(lat1)) * math.cos( (d / R) ) + math.cos( math.radians(lat1) ) * math.sin( d / R ) * math.cos( math.radians(θ) ) ) )
	lon2 = lon1 + math.degrees(math.atan2(math.sin( math.radians(θ) ) * math.sin( (d / R) ) * math.cos( math.radians(lat1) ), math.cos( d / R ) - math.sin( math.radians(lat1) ) * math.sin( math.radians(lat2) )))
	print(lat2,",", lon2)
	return(lat2, lon2)

for d1, θ1 in zip(d, θ):
	(lat2, lon2) = get_next_lat_long(lat1, lon1, d1, θ1)
	lat1 = lat2
	lon1 = lon2