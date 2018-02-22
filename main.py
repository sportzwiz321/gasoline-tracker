import sys

fuelDay = {}

data = open("sample.txt", "r")
data_line = data.readlines()
for x in range(0, len(data_line)):
	plain_line = data_line[x].split("\n")[0]
	split_line = plain_line.split("/")
	if len(split_line) >= 3:

		cost = data_line[x + 1].split("\n")[0].split(" ")[0]
		gas = data_line[x + 2].split("\n")[0].split(" ")[0]
		mileage = data_line[x + 3].split("\n")[0].split(" ")[0]

		if cost and gas and mileage:
			trip = {
				"cost": float(cost),
				"gas": float(gas),
				"mileage": float(mileage)
			}

			fuelDay[plain_line] = trip

if len(sys.argv) != 4 and len(sys.argv) != 1:
	print "Usage Error:\nmain.py expected"
	print "Usage Error:\nmain.py [cost] [volume] [distance] expected"
	sys.exit()

if len(sys.argv) == 4:
	gas_total_cost = float(sys.argv[1])
	gas_volume = float(sys.argv[2])
	distance = float(sys.argv[3])
else:
	# gas_total_cost = input("Enter the total cost:")
	# gas_volume = input("Enter the total gas:")
	# distance = input("Enter distance traveled:")

	total_cost = 0.0
	total_gas = 0.0
	total_mileage = 0.0

	for day in fuelDay:
		trip = fuelDay[day]
		total_cost += trip["cost"]
		total_gas += trip["gas"]
		total_mileage += trip["mileage"]

	print "total cost:", "%.2f" % total_cost
	print "total gas:", "%.3f" % total_gas
	print "total mileage:", "%.1f" % total_mileage

	print

	total_cpg = total_cost / total_gas
	total_mpg = total_mileage / total_gas
	total_cpm = total_cost / total_mileage
	total_mpd = total_mileage / total_cost

	print "overall cost per gallon:", "%.3f" % total_cpg
	print "overall miles per gallon:", "%.2f" % total_mpg
	print "overall cost per mile:", "%.2f" % total_cpm
	print "overall miles per dollar", "%.3f" % total_mpd



# print "%.2f" % gas_total_cost
# print "%.3f" % gas_volume
# print "%.1f" % distance

# gas_price = gas_total_cost / gas_volume
# mpg = distance / gas_volume

# print

# print "total_cost:", "%.2f" % gas_total_cost
# print "gallons:", "%.3f" % gas_volume
# print "mileage:", "%.1f" % distance

# print

# print "dollars per gallon:", "%.3f" % gas_price
# print "miles per gallon:", "%.2f" % mpg