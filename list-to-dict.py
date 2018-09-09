import csv
import json

with open('mylist.txt','rb') as my_file:
    reader = csv.reader(my_file)
    my_list = list(reader)

print my_list
print "\n\n"

data = []

for x in my_list:
    temp = {}
    temp['label'] = x[0]
    temp['field'] = x[1]
    temp['data_type'] = ''
    temp['default_value'] = ''
    
    data.append(temp)

print data