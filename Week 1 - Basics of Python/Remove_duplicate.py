import ast
test_list=ast.literal_eval(input())

res=[]

for i in test_list:
    if i not in res:
        res.append(i)
res=list(res)
print ("" + str(res))
