def is_prime(n):
    # Prime numbers must be greater than 1
    if n <= 1:
        return f"{n} is not a prime"
    
    # Check for factors from 2 up to the square root of n for efficiency
    for i in range(2, int(n**0.5) + 1,):
        if n % i == 0:
            return f"{n} is not a prime"  #Not prime, exit the function immediately
    return f"{n} is prime"
 # If the loop finishes without finding a factor, it is prime

user_input = int(input("Pick a number: "))
ans= is_prime(user_input)
print(ans)


