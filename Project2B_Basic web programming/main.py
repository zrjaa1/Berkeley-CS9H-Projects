# Function Name: main
# Function Description: print the film names that are recently shown, and its score on rotten tomato.

# Function Input:
# nothing

# Function Output: 
#  -print film name and its score on the screen.

import urllib

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def main():

	url = urllib.urlopen("https://www.rottentomatoes.com/browse/opening/")
	html = url.read()
	begin_index_list = list(find_all(html,"\"title\":"))
	end_index_list = list(find_all(html,"\",\"url\":\"/m/"))
	score_index_list = list(find_all(html,"tomatoScore"))

	print "score" + "    ",
	print "film name"



	for i in range(len(begin_index_list)):
		if html[score_index_list[i]+15] == ',':
			print html[score_index_list[i]+13:score_index_list[i]+15] + "       ",
		else :
			print html[score_index_list[i]+13:score_index_list[i]+16] + "      ",

		print html[begin_index_list[i]+9:end_index_list[i]]
		
main()