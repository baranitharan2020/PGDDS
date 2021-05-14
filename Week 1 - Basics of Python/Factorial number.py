#take the input here
number=input()



#the function definition starts here
def factorial(n):
    num=int(n)
    t=num
    if num>0:
            for d in range(num):
                if num>=d:
                    t=t*(num-1)
                    num=num-1
            print(t)
            
    else:
        print('-1')

#do not alter the code typed below
k=factorial(number)

