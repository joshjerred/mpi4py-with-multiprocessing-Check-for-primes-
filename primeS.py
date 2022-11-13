import sys
import math
import time

if len(sys.argv) < 1:
    print("Syntax: python3 primeS.py [number to check up to] ['-s' to only print total]")
    sys.exit()

silent = False

if (len(sys.argv) >= 3) and (sys.argv[2] == "-s"): # Check for -s arg
    silent = True


def isPrime(candidate_number):
    found_prime = True
    for div_number in range(2, math.isqrt(candidate_number) + 1): # math.issqrt returns the floor of the sqrt, +1 as range is not inclusive.
        if candidate_number % div_number == 0:
            found_prime = False
            break
    if found_prime:
        return True # If it's a prime, return true.
    return False

if __name__ == "__main__":
    numPrimes = 0
    start_time = time.time()
    start = 1
    end_number = int(sys.argv[1])
    for i in range(start, end_number, 2):
        if isPrime(i): numPrimes += 1
    end = round(time.time() - start_time, 2)

    if not silent: print('Find all primes up to: ' + str(end_number))
    if not silent: print('Nodes: ' + str(1) + ' - Single Thread')
    if not silent: print('Time elasped: ' + str(end) + ' seconds')
    if not silent: print('Primes discovered: ' + str(numPrimes))
    data = [str(end_number), str(numPrimes), str(end), "local", 1]
    if silent: print("Primes in: {:<15} Found: {:<10} Seconds: {: <10} Nodes: {: <10} Threads Per Node: {: <10}".format(*data))