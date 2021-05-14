
Dictionary And List
Description
You will be converting a dictionary, of string(keys) and list of string (values),  to a list of strings. Please check the sample input/output for clarification.


Input:
A dictionary with keys as strings and values as a list of strings.

Output:
A list of strings


Sample input:
{‘Mobile’: [‘Redmi’, ‘Samsung’, ‘Realme’], 
‘Laptop’: [‘Dell’, ‘HP’],
‘TV’: [‘Videocon’, ‘Sony’] }

Sample output:
[‘Mobile_Redmi’, ‘Mobile_Samsung’, ‘Mobile_Realme’, ‘Laptop_Dell’, ‘Laptop_HP’, ‘TV_Videocon’, ‘TV_Sony’]


Sample input:
{ 'Pen': ['Gel', 'Ink', 'ball'],
'Mobile': ['Android', 'apple'] }

Sample output:
['Pen_Gel', 'Pen_Ink', 'Pen_ball', 'Mobile_Android', 'Mobile_apple']



#input has been taken for you
import ast
input_str = input()
#input dictionary has been received in input_dict
d= ast.literal_eval(input_str)
l=[]
for key in d.keys():
    for w in d[key]:
        l.append(key+'_'+w)

#start writing your code here

print(l)

