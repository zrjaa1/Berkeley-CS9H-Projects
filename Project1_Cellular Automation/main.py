# Function Name: main
# Function Description: This procedure will generate a array that switches on or off based on its previous status and its neighborhood status, depending on specific rules( as an input.)

# Function Input:
#  -rule: rule that is written in decimal, will be transfered into a binary string in the future.
#  -step: how many steps does the loop should be excuted.

# Function Output: print the rule, step and whole series of array that are generated.

import sys,os

def generate_next_bit(bit_rule,left,mid,right):

    position = left*4 + mid*2 + right;
    if bit_rule[position] == '1' :
    	return '1'
    else :
     	return '0'
    
def generate_next_row(pre_row,bit_rule):

    length = len(pre_row)
    next_row = ''
    for i in range(length):
        if i == 0 :
    		left = 0
    		mid = pre_row[i]
    		right = pre_row[i+1]
    	if i == length - 1:
    		left = pre_row[i-1]
    		mid = pre_row[i]
    		right = 0
    	else :
    		left = pre_row[i-1]
    		mid = pre_row[i]
    		right = pre_row[i+1]

        row_element = generate_next_bit(bit_rule,int(left),int(mid),int(right))
        next_row = next_row + row_element
    return next_row

def main(rule,step):

    bit_rule = str(rule%2) + str(rule%4/2) + str(rule%8/4) + str(rule%16/8) + str(rule%32/16) + str(rule%64/32) + str(rule%128/64) + str(rule/128)
    
    initial_row = '0'*step + '1' + step*'0'

    print "P1",step*2+1,step
    for i in range(step):
    	if i == 0 :
    		print initial_row
    		next_row = generate_next_row(initial_row,bit_rule)
        else :
        	print next_row
        	next_row = generate_next_row(next_row,bit_rule)

rule = int(sys.argv[1])
step = int(sys.argv[2])
main(rule,step)
