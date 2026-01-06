from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

number = rank + 1
total = comm.reduce(number, op=MPI.SUM, root=0)

if rank == 0:
    print("Sum of all ranks:", total)
