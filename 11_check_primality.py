#!/usr/bin/env python
# user enters number and program determines whether prime.

def check_primality(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)

    if len(divisors) > 1:
        return "Not a prime number"
    else:
        return "Prime number"

num = int(raw_input("Enter a number to learn whether it's prime -> "))
print check_primality(num)
