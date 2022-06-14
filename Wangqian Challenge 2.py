# Wangqian Challenge 2
# by Dan Le
import numpy as np
from mpi4py import MPI

# Start of MPI
comm = MPI.COMM_WORLD
rank = comm.rank  # current process
p = comm.Get_size()  # number of processes
dest = 0

# Using NumPy library to create array
array = np.linspace(1, 10000, num=10000, dtype=int)

n = len(array)//p  # length of local calculation of array

# local calculations within array
local_a = rank * n
local_b = (rank+1) * n
local_sum = sum(array[local_a:local_b])

total = comm.reduce(local_sum)

if rank == 0:
    print("The sum of all values in the array is ", total)

MPI.Finalize()

# Execute this script in console with mpiexec -np 4 python main.py
