from mpi4py import MPI
import time
import sys
from multiprocessing import Pool


comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
cluster_size = comm.Get_size()


end_number = int(sys.argv[1])

start_time = time.time()

# Split work between nodes by changing the start number (*2 as it skipps even numbers)
start = (my_rank * 2) + 1

def func(candidate_number):
    found_prime = True
    for div_number in range(2, candidate_number):
        if candidate_number % div_number == 0:
            found_prime = False
            break
    if found_prime:
        return True # If it's a prime, return true.
    return False

if __name__ == "__main__":
    with Pool(4) as p:
        primes = [sum(p.map(func, range(start, end_number, cluster_size * 2)))] # Cluster size starts at 1, with a 4 node server this will iterate by 8


print(my_rank, "Done")
results = comm.gather(primes, root=0)

if my_rank == 0:
    end = round(time.time() - start_time, 2)

    print('Find all primes up to: ' + str(end_number))
    print('Nodes: ' + str(cluster_size))
    print('Time elasped: ' + str(end) + ' seconds')

    merged_primes = [item for sublist in results for item in sublist]
    merged_primes.sort()
    print(merged_primes) # Prints out the number found per node
    print('Primes discovered: ' + str(sum(merged_primes)))

