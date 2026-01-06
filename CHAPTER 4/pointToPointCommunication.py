from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = "Message from Process 0"
    comm.send(data, dest=1)
    print("Process 0 sent data.")
elif rank == 1:
    received = comm.recv(source=0)
    print(f"Process 1 received: {received}")
