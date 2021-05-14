#Take input here
#we will take input using ast sys
import ast
input_str = input()

#ast.literal_eval() will evaluate the string and make a data structure for the same
#here the input is a list since input is in '[...]', so ast.literal_eval() will
#make a list with the same data as passed
input_list = ast.literal_eval(input_str)

#the data or the two values in list is now changed to separate variables
day_of_the_week = input_list[0] #first element is an integer denoting the day of the week
is_on_vacation = input_list[1] #this is a boolean denoting if its vacation or not

# write your code here

weekend=[6,7]
if is_on_vacation and (day_of_the_week not in weekend):
    print("10:00")
elif is_on_vacation and day_of_the_week in weekend:
    print("off")
elif day_of_the_week not in weekend and (not is_on_vacation):
    print("7:00")
else:
    print("10:00")
    

