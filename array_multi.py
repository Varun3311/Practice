'''Python Program for Find Remainder of Array squaring and adding Divided by N'''
import numpy as np
nums=int(input("enter number of elements in array:"))
array1=[] #list 
for i in range(nums):
    n=int(input("enter number:"))
    array1.append(n)
array=np.array(array1) #converting to array type
N=int(input("enter N:"))
sum=0
for i in array:
    sum=(sum+ (i**2))

print(sum%N)

print(type(array))


