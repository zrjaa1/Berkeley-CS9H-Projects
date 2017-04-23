# Function Name: source_to_base
# Function Description: transfer the source unit into base unit.
# Function Input
#   - source_unit: the unit of source, such as mile, cm.
#   - source_value: the value in source unit.

# Function Output
#   - base_unit: the unit of base, such as m, kg, L
#   - base_value: the value in base unit.

def source_to_base(source_unit, source_value):

	Distance = {'ft': 0.3048, 'cm': 0.01, 'mm': 0.001, 'mi': 1609.34, 'm': 1, 'yd': 0.9144, 'km': 1000, 'in': 0.0254};
	Weight   = {'lb': 0.453592, 'mg': 0.000001, 'kg': 1, 'oz': 0.0283495, 'g': 0.001};
	Volume   = {'floz': 0.0295735, 'qt': 0.946353, 'cup': 0.236588, 'mL': 0.001, 'L': 1, 'gal': 3.78541, 'pint': 0.473176};

	if Distance.has_key(source_unit):
		base_unit = 'm'
		base_value = source_value * Distance[source_unit]
		print base_unit, base_value
		return base_unit, base_value

	elif Weight.has_key(source_unit):
		base_unit = 'kg'
		base_value = source_value * Weight[source_unit]
		print base_unit, base_value
		return base_unit, base_value

	elif Volume.has_key(source_unit):
		base_unit = 'L'
		base_value = source_value * Volume[source_unit]
		print base_unit, base_value
		return base_unit, base_value

	else:
		print 'Wrong source unit'


source_to_base('lb',100)