#take input here
a1=input()
a2=input()

#code here to check if they are anagrams or no

a1=sorted(a1)
a2=sorted(a2)

if a1==a2:
    print('True')
else:
    print('False')
