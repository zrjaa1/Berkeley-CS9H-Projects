# Function Name: generate_next_bit
# Function Description: This is a function called by "generate_next_row", which generate a single big based on the left, mid, right number and the rule.
# Function Input
#   - bit_rule: the rule that is written by 8-bit string.
#   - left: the left side bit.
#   - mid: the middle side bit.
#   - right: the right side bit.

# Function Output: return a single bit in string form.

  
def generate_next_bit(bit_rule,left,mid,right):

    position = left*4 + mid*2 + right;
    if bit_rule[position] == '1' :
        print '1'
    	return '1'
    else :
        print '0'
     	return '0'
        

generate_next_bit("01010101",0,0,0)
generate_next_bit("01010101",0,0,1)
