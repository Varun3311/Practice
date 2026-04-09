num=int(input("enter a number:"))
power=len(str(num))
num2=str(num)
sum=0
for i in num2:
    sum=sum+int(i)**power

if sum==num:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")
