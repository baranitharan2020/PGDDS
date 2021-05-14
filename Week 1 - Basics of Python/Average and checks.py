#Take input here
#we will take input using ast sys
import ast
input_str = input()
input_list = ast.literal_eval(input_str)

#Remember how we took input in the Alarm clock Question in previous Session?
#Lets see if you can finish taking input on your own

data=input_list[0]
check=input_list[1]
sum=0
#start writing your code to find if check is above average of data 
for item in data:
    sum=sum+item
#print(sum)
av=sum/len(data)
#print(av)
if av<check:
    print("True")
else:
    print("False")


