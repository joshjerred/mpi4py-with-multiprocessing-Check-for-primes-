import time
import sys
from multiprocessing import Pool
import math

silent = False

if (len(sys.argv) >= 3) and (sys.argv[2] == "-s"): # Check for -s arg
    silent = True

threads = 4
if (len(sys.argv) >= 4): # Check for -s arg
    threads = int(sys.argv[3])
    
my_rank = 0
cluster_size = 1


end_number = int(sys.argv[1])

start_time = time.time()

# Split work between nodes by changing the start number (*2 as it skipps even numbers)
start = (my_rank * 2) + 1

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
    with Pool(threads) as p:
        primes = [sum(p.map(isPrime, range(start, end_number, cluster_size * 2)))] # Cluster size starts at 1, with a 4 node server this will iterate by 8


if my_rank == 0:
    end = round(time.time() - start_time, 2)

    if not silent: print('Find all primes up to: ' + str(end_number))
    if not silent: print('Local Multicore')
    if not silent: print('Time elasped: ' + str(end) + ' seconds')
    if not silent: print(primes) # Prints out the number found per node
    if not silent: print('Primes discovered: ' + str(sum(primes)))
    data = [str(end_number), str(sum(primes)), str(end), str(cluster_size), str(threads)]
    if silent: print("Primes in: {:<15} Found: {:<10} Seconds: {: <10} Nodes: {: <10} Threads Per Node: {: <10}".format(*data))
