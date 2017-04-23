# Function Name: base_to_dest
# Function Description: transfer the base unit into destination unit.
# Function Input
#   - base_unit: the unit of base, including m, kg, L.
#   - base_value: the value in base unit.
#   - dest_unit: the unit of destination.

# Function Output
#   - dest_value: the value in destination unit.

def base_to_dest(base_unit, base_value, dest_unit):

	Distance = {'ft': 3.28084, 'cm': 100, 'mm': 1000, 'mi': 0.000621371, 'm': 1, 'yd': 1.09361, 'km': 0.001, 'in': 39.3701};
	Weight   = {'lb': 2.20462, 'mg': 1000000, 'kg': 1, 'oz': 35.274, 'g': 1000};
	Volume   = {'floz': 33.814, 'qt': 1.05669, 'cup': 4.22675, 'mL': 1000, 'L': 1, 'gal': 0.264172, 'pint': 2.11338};

	if base_unit == 'm':
		if Distance.has_key(dest_unit):
			dest_value = base_value * Distance[dest_unit]
			print dest_unit, dest_value
			return dest_unit, dest_value
		else:
			print "The source unit and dest unit are not in a category"

	elif base_unit == 'kg':
		if Weight.has_key(dest_unit):
			dest_value = base_value * Weight[dest_unit]
			print dest_unit, dest_value
			return dest_unit, dest_value
		else:
			print "The source unit and dest unit are not in a category"

	elif base_unit == 'L':
		if Volume.has_key(dest_unit):
			dest_value = base_value * Volume[dest_unit]
			print dest_unit, dest_value
			return dest_unit, dest_value
		else:
			print "The source unit and dest unit are not in a category"
	else:
		print 'System Error'


base_to_dest('L',100,'cup')