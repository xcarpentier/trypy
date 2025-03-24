from typing import List


def euclyde():
    primes: List[int] = []
    number: int = 2
    prime_range: int = 1
    while True:
        is_prime: bool = True
        for prime in primes:
            if number % prime == 0:
                is_prime = False
                break

        if is_prime == True:
            print(f"{prime_range}. {number}")
            primes.append(number)
            prime_range += 1

        number += 1


euclyde()
