from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

send_data = [rank] * size
recv_data = comm.alltoall(send_data)

print(f"Process {rank} received: {recv_data}")
