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

numb=int(input("enter number:"))
fact(numb)



#Using recursion:

def rec_fact(num):
    if num==0 or num==1:
        return 1
    elif num<0:
        return "cannot define"
    else:
        return num*rec_fact(num-1)

num=int(input("enter a num:"))
result=rec_fact(num)
print(result)