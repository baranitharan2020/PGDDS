No Spaces
Description
While naming entities, it is a common practice to avoid spaces. That is the reason you see so many people using underscores instead of spaces. 
You will be given a string, containing a few spaces and random upper and lower cases. You have to write a code that will add underscore in place of spaces and also capitalise the letters properly, i.e. the first letter after underscore should be in upper case and the first letter of the string should be in upper case, all of the other letters should be lower case. 
This type of activity is frequently encountered while starting to analyse data. This is called Data cleaning and you will learn more about it in upcoming modules.

----------------------------------------------------------------------
Input:
A string of only alphabets and spaces

Output:
A string formatted as stated above. See sample input/output for more clarification,

----------------------------------------------------------------------
Sample input:
caloRie consuMed

Sample output:
Calorie_Consumed

----------------------------------------------------------------------
Sample input:
data science

Sample output:
Data_Science



#take input here
d=input()

#write code to format the string s as asked 

d=d.title()
d=d.split(' ')
f='_'.join(d)
print(f)






