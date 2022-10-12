"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes > 0:
        num = 1
        while len(list) < number_of_primes:
            num = num + 1
            if isPrime(num):
                list.append(num)
    else:
        raise ValueError('The number of primes must be greater than 0.')
    return list

def isPrime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True