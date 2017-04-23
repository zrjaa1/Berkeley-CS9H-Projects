# Function Name: main
# Function Description: load arguments from the command line and convert value in source unit to value in dest unit.

# Function Input:
#  -source_value: value in source unit.
#  -source_unit: unit of source value.
#  -dest_unit: Which unit you want to convert to.

# Function Output: 
#  -print dest value on the screen.
import sys,os

def source_to_base(source_unit, source_value):

	Distance = {'ft': 0.3048, 'cm': 0.01, 'mm': 0.001, 'mi': 1609.34, 'm': 1, 'yd': 0.9144, 'km': 1000, 'in': 0.0254};
	Weight   = {'lb': 0.453592, 'mg': 0.000001, 'kg': 1, 'oz': 0.0283495, 'g': 0.001};
	Volume   = {'floz': 0.0295735, 'qt': 0.946353, 'cup': 0.236588, 'mL': 0.001, 'L': 1, 'gal': 3.78541, 'pint': 0.473176};

	if Distance.has_key(source_unit):
		base_unit = 'm'
		base_value = source_value * Distance[source_unit]
		return base_unit, base_value

	elif Weight.has_key(source_unit):
		base_unit = 'kg'
		base_value = source_value * Weight[source_unit]
		return base_unit, base_value

	elif Volume.has_key(source_unit):
		base_unit = 'L'
		base_value = source_value * Volume[source_unit]
		return base_unit, base_value

	else:
		print 'Wrong source unit'

def base_to_dest(base_unit, base_value, dest_unit):

	Distance = {'ft': 3.28084, 'cm': 100, 'mm': 1000, 'mi': 0.000621371, 'm': 1, 'yd': 1.09361, 'km': 0.001, 'in': 39.3701};
	Weight   = {'lb': 2.20462, 'mg': 1000000, 'kg': 1, 'oz': 35.274, 'g': 1000};
	Volume   = {'floz': 33.814, 'qt': 1.05669, 'cup': 4.22675, 'mL': 1000, 'L': 1, 'gal': 0.264172, 'pint': 2.11338};

	if base_unit == 'm':
		if Distance.has_key(dest_unit):
			dest_value = base_value * Distance[dest_unit]
			return dest_unit, dest_value
		else:
			print "The source unit and dest unit are not in a category"

	elif base_unit == 'kg':
		if Weight.has_key(dest_unit):
			dest_value = base_value * Weight[dest_unit]
			return dest_unit, dest_value
		else:
			print "The source unit and dest unit are not in a category"

	elif base_unit == 'L':
		if Volume.has_key(dest_unit):
			dest_value = base_value * Volume[dest_unit]
			return dest_unit, dest_value
		else:
			print "The source unit and dest unit are not in a category"
	else:
		print 'System Error'

def main():
	print ""
	print "Welcome to use the powered unit converter designed by Jay in midnight of 2017-02-28"
	print ""
	print "This converter supports units included in Distance, Weight, and Volume category"
	print ""
	print "For the Distance category, we have units include 'ft','cm','mm','mi','m','yd','km','in'"
	print "For the Weight category, we have units include 'lb','mg','kg','oz','g'"
	print "For the Volume category, we have units include 'floz','qt','cup','mL','L','gal','pint'"
	print ""
	print "Please obey the rule 'number source_unit in destination_unit', for example '1 mi in km'"
	print ""

	while (1):
		expression = raw_input("Enter a expression like example above:")

		splited_expression = expression.split()
		if splited_expression[0] == 'q':
			print "Thanks for using this procedure"
			return
		else: 
			source_value = float(splited_expression[0])
			source_unit  = splited_expression[1]
			dest_unit  = splited_expression[3]

			base_unit, base_value = source_to_base(source_unit,source_value)
			dest_unit, dest_value = base_to_dest(base_unit,base_value,dest_unit)
			print source_value, source_unit,'=', dest_value, dest_unit,
        	print "(enter 'q' to quit)"

main()

	