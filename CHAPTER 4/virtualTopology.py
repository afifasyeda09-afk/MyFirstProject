from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

dims = [size]   # 1D topology
periods = [False]
reorder = False
cart_comm = comm.Create_cart(dims, periods, reorder)

coords = cart_comm.Get_coords(rank)
print(f"Process {rank} has coordinate {coords}")
