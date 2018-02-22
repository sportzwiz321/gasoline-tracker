import sys

if len(sys.argv) != 4 and len(sys.argv) != 1:
	print "Usage Error:\nmain.py expected"
	print "Usage Error:\nmain.py [cost] [volume] [distance] expected"
	sys.exit()

# print "Hello World!"

if len(sys.argv) == 4:
	gas_total_cost = float(sys.argv[1])
	gas_volume = float(sys.argv[2])
	distance = float(sys.argv[3])
else:
	gas_total_cost = input("Enter the total cost:")
	gas_volume = input("Enter the total gas:")
	distance = input("Enter distance traveled:")

# print "%.2f" % gas_total_cost
# print "%.3f" % gas_volume
# print "%.1f" % distance

gas_price = gas_total_cost / gas_volume
mpg = distance / gas_volume

print

print "total_cost:", "%.2f" % gas_total_cost
print "gallons:", "%.3f" % gas_volume
print "mileage:", "%.1f" % distance

print

print "dollars per gallon:", "%.3f" % gas_price
print "miles per gallon:", "%.2f" % mpg