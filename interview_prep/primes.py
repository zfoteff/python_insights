#   Output specified number of primes to stdout
import sys

def isPrime(num):
    if num == 0:
        return False

    if num % 2 == 0 and num != 2:
        return False

    if num % 3 == 0 and num != 3:
        return False

    counter = 4
    while counter < num/2:
        if num % counter == 0:
            return False
        
        counter += 1

    return True



def findPrimes(num):
    primes = []
    x = 2

    while len(primes) < num:
        if isPrime(x):
            primes.append(x)

        x += 1
            
    print(primes)
    return primes


def main():
    primes = findPrimes(20)

main()
