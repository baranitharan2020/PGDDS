ommon Prefix
Description
You will be given two strings. You have to find the largest prefix common in both the strings.

----------------------------------------------------------------------
Input:
Two lines of input, one string on each line

Output:
The common largest prefix for both strings. Check sample input/output for clarification. -1 if no prefix is common.

----------------------------------------------------------------------
Sample input:
abshdksajd
abshiehand

Sample output:
absh

----------------------------------------------------------------------
Sample input:
upgradData
upGradScience

Sample output:
upgrad



#input has been taken for you

a=input()
b=input()

#start writing your code to find largest common prefix here


a=a.lower()
b=b.lower()
l1=len(a)
l2=len(b)
l3=min(l1,l2)
for i in range(l3):
    if a[i]!=b[i]:
        break
if i==0:
    print(-1)
else:
    print(a[:i])

