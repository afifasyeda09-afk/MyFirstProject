from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

value = rank * 10
gathered = comm.gather(value, root=0)

if rank == 0:
    print("Gathered values:", gathered)
