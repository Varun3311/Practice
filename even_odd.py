def even_odd(a):
    if a%2 == 0:
        return "even"
    else:
        return "odd"
num= int(input("enter a number:"))
result = even_odd(num)
print(result)
