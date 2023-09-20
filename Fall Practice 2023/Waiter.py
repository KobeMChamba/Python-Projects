#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q

def waiter(number, q):
    def generate_primes(q):
        N = 10000  # Choose a reasonably large value for N, 1200th prime is 9733
        primes = []
        is_prime = [True] * (N + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, N + 1):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, N + 1, i):
                    is_prime[j] = False

                if len(primes) == q:
                    break

        return primes

    def sort_plates(piles, iterations):
        answers = []
        primes = generate_primes(iterations)

        for i in range(iterations):
            current_prime = primes[i]
            Bi = []
            Ai = []

            while piles:
                plate = piles.pop()
                if plate % current_prime == 0:
                    Bi.append(plate)
                else:
                    Ai.append(plate)

            answers.extend(reversed(Bi))
            piles = Ai

        answers.extend(reversed(piles))
        return answers

    return sort_plates(number, q)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
