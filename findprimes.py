def primes(x,y):
    prime_list = []
    for i in range(x, y):
        # A number must be > 1 to be prime
        if i > 1:
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else:
                # This else belongs to the 'for' loop
                prime_list.append(i)
    return prime_list

result=primes(3,20)
print(result)




'''

import math

# Step 1: Define the function to check primality
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Step 2: Loop through the range between two numbers
def find_primes_between(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage
print(find_primes_between(10, 30)) # Output: [11, 13, 17, 19, 23, 29]
'''