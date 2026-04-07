def fact(n):
    f=1
    if n==0:
        print(1)
    elif n<0:
        print("cannot define")
    else:
        for i in range(1,n+1):
            f= f*i
        print(f)

num=int(input("enter number:"))
fact(num)



#Using recursion:
