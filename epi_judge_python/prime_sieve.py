from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # TODO - you fill in here.
    '''
    BRUTE FORCE
    Create an empty array to keep all the prime number called p
    Add 2 to p because 2 is always a prime number
    Loop i from 3 to n:
        Go through each element in p
            if i%an element in p == 0: continue
        Add i to p because it is also a prime number


    if n < 2:
        return []
    p = [2]
    for i in range(3, n+1):
        # print(p)
        for num in p:
            prime = False
            if i % num == 0:
                #print("Non prime: ", i)
                # print("Check")
                prime = True
                break
        if not prime:
            p.append(i)
    '''

    '''
    OPTIMAL
    Create an array A with n+1 elements, set entry 0th and 1st to be 0 because they are not prime, set the rest to
    be 1 because they are potentially a prime number
    Loop through this array
        If A[i] == 1, then add it to the prime list
            Find all multiple of A[i] till it bigger than n, mark all the multiple to be 0 in array A
    Return prime number list
    '''
    A = [0] * (n+1)
    for i in range(len(A)):
        if i >= 2:
            A[i] = 1

    p = []
    for i in range(2, len(A)):
        if A[i] == 1:
            p.append(i)
            # Update the multiple of A[i] in A to be 0
            temp = i
            while i*temp <= n:
                A[i*temp] = 0
                temp += 1
    return p


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
