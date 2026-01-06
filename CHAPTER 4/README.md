# Chapter 4: MPI Examples

This folder contains simple MPI examples using `mpi4py`. Each script demonstrates a core MPI concept with clear and easy-to-understand code.

---

## 📄 Topics & Files

1. **Hello World** (`helloworld_MPI.py`)  
   Simple program where each process prints its rank and total number of processes.

2. **Point-to-Point Communication** (`pointToPointCommunication.py`)  
   Demonstrates sending and receiving messages between two processes.

3. **Broadcast** (`broadcast.py`)  
   Root process sends a message to all other processes.

4. **Scatter** (`scatter.py`)  
   Distributes elements of a list from the root process to all processes.

5. **Gather** (`gather.py`)  
   Collects data from all processes to the root process.

6. **All-to-All Communication** (`alltoall.py`)  
   Every process sends data to every other process.

7. **Reduction** (`reduction.py`)  
   Performs a reduction operation (e.g., sum) across all processes.

8. **Virtual Topology** (`virtualTopology.py`)  
   Creates a Cartesian (1D) virtual topology and shows coordinates of each process.

9. **Deadlock Problems** (`deadLockProblems.py`)  
   Demonstrates safe communication patterns to avoid deadlocks.

---

## ⚡ Requirements

- Python 3.x  
- `mpi4py` library (`pip install mpi4py`)  

---

## 🚀 How to Run

Run any script using `mpiexec` with the desired number of processes:

```bash
mpiexec -n 4 python script_name.py
