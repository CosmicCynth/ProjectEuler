def prime_factors(number):
    factors = []

    # Divide by 2 until the number is odd
    while number % 2 == 0:
        factors.append(2)
        number //= 2

    # Start checking for odd divisors from 3 onwards
    divisor = 3
    while number != 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 2

    return factors


# Test the function
number = 600851475143
print(f"{prime_factors(number)}")
