from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = [i for i in range(size)]
else:
    data = None

received = comm.scatter(data, root=0)
print(f"Process {rank} got {received}")
