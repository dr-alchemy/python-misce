import csv
import json

with open('mylist.txt','r') as my_file:
    reader = csv.reader(my_file)
    my_list = list(reader)

# print my_list
print "\n\n"

data = []
data2 = []

keys = ['label', 'field', 'data_type', 'default_value']

for x in my_list:
    # temp = {}
    # temp['label'] = x[0]
    # temp['field'] = x[1]
    # data.append(temp)
    
    temp = dict(zip(keys, x))
    temp['data_type'] = ''
    temp['default_value'] = ''
    data2.append(temp)

# print data
# print json.dumps(data)

print "\n\n"

print json.dumps(data2)