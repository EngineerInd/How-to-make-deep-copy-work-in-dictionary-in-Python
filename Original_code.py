//How to achieve deepcopy in dictionaries?




li1 = ['Column_6', 'Column_11']
delimiters = ['a','b','c','d']
inner_dict = dict.fromkeys(delimiters,[0,0])
delim_dict = dict.fromkeys(li1 ,None)
for k,v in delim_dict.items():
    delim_dict[k] = copy.deepcopy(inner_dict)


print (delim_dict) gives


{'Column_6': {'a': [0, 0], 'b': [0, 0], 'c': [0, 0], 'd': [0, 0]},
 'Column_11': {'a': [0, 0], 'b': [0, 0], 'c': [0, 0], 'd': [0, 0]}}
