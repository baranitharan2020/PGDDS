Recruit New Members
Description

Suppose you are a manager as a big firm and now are looking for new members for your team. You sent out an advertisement and have received a few applications. You have a habit of scoring people on a scale of 100. You have given scores to all the members of your team and the new applications. The process of selection is going to be very straightforward if the applicant improves the average of the team then you hire the applicant to join the team or else reject the application. Remember the order of processing applications is going to be important here.


You may see this as an extension of the previous problem, which it is. You may use the code written in the previous question as a function to improve the code quality.


----------------------------------------------------------------------

Input:

Two lists on two separate lines.

The first line will have the list of scores of current team members

The second line will have the list of scores of the applicants.


Output:

The list consisting of scores of the final team after hiring from the pool of applicants.


----------------------------------------------------------------------

Sample input:

[23,45,34,76]

[70,34,94]


Sample output:

[23, 45, 34, 76, 70, 94]


Explanation:

The first applicant has score 70, and the team average is 44.5 hence the applicant is hired making the team average 49.6

The second applicant has score 34, and the team average is 49.6 hence the applicant is rejected keeping the team average same 49.6

The third applicant has score 94, and the team average is 49.6 hence the applicant is hired making the team average 57


----------------------------------------------------------------------

Sample input:

[10,20,30,40,50]

[30,60,80,40]


#you have to take input on your own here

import ast
team = ast.literal_eval(input())
ap=ast.literal_eval(input())
#write your code here
sum=0
for item in team:
    sum=sum+item

av=int(sum/len(team))
tem=[]
for item in ap:
    if item>av:
        tem.append(item)

fin=team+tem
fin = list(dict.fromkeys(fin))

print(fin)












