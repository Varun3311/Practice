#to find minimum in the list

n=int(input("enter no of elements in the list"))
lst=[]
for i in range(n):
    num=int(input("enter elements:"))
    lst.append(num)

result= lst[0]
for i in lst:
    if i<result:
        result=i

print(result)

print(lst)

print(min(lst))

lst.sort()
a=lst[0]
print(a)


print(type(lst))