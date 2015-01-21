"""The text file, scores.txt, contains a series of local restaurant ratings. 
Each line looks like this: Restaurant Name:Rating
Your job is to write a program named 'sorted_data.py' that reads the file, 
then spits out the ratings in alphabetical order by restaurant.
"""

from sys import argv

script, score_file, alpha_output = argv

input_file_data = open(score_file, 'r')


d = {}

for line in input_file_data:
    data = line.rstrip().split(':')
    rest_name = data[0]
    rest_score = data[1]
    d[rest_name] = rest_score

print d.items()    




# final_output = open(alpha_output, 'w').write(input_file_data)
# print final_output