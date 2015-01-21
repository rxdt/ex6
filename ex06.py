"""The text file, scores.txt, contains a series of local restaurant ratings. 
Each line looks like this: Restaurant Name:Rating
Your job is to write a program named 'sorted_data.py' that reads the file, 
then spits out the ratings in alphabetical order by restaurant.
"""
#allows script to read from CL
from sys import argv

#assigns these variables to user's CL input
script, score_file, alpha_output = argv

#opens original score data file for reading
input_file_data = open(score_file, 'r')

#initialize new dictionary
d = {}

#read each line in original score data file and tokenize it
for line in input_file_data:
    data = line.rstrip().split(':')
    rest_name = data[0]
    rest_score = data[1]
    #add tokens to our dictionary
    d[rest_name] = rest_score

#create new list to store a sorted version of our dictionary
ordered_list = sorted(d.items())

#open a new file where we will eventually store the standard output
final_output = open(alpha_output, 'w')

#look through sorted list and print for each one the rest name and associated score
#will write in output file each entry to a new line
for rest_name, rest_score in sorted(d.items()):
     final_output.write("Restaurant %r is rated at %s.\n" % (rest_name, rest_score))

#close files
input_file_data.close()
final_output.close()
