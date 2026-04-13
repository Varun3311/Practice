'''Python Program for Find Remainder of Array squaring and adding Divided by N'''

nums=int(input("enter number of elements in array:"))
array=[]
for i in range(nums):
    n=int(input("enter number:"))
    array.append(n)
N=int(input("enter N:"))
sum=0
for i in array:
    sum=(sum+ (i**2))

print(sum%N)




