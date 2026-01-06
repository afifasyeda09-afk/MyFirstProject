from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    comm.send("Data from 0", dest=1)
    msg = comm.recv(source=1)
    print(f"Process 0 received: {msg}")

elif rank == 1:
    msg = comm.recv(source=0)
    comm.send("Reply from 1", dest=0)
    print(f"Process 1 received: {msg}")
