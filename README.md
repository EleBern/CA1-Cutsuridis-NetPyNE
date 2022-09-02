# CA1-NetPyNE-model

## Description
NetPyNE (www.netpyne.org) version of a model of CA1 microcircuits published by [Cutsuridis et al].

Original model and publication: https://modeldb.yale.edu/234233 

This is a functional model of the CA1 that studies the storage and retrieval of spatiotemporal patterns. 
In this branch I am removing an increasing number of EC inputs from an increasing number of CA1 cells to test how this affects the network's performance. For more details on the network see the main branch. 
## Setup

Requires NEURON with Python. 
Requires MPI to run batch simulations

## Execution

1. Type `nrnivmodl mod` to compile the `.mod` files. This should create a directory called either i686 or x86_64, depending on your computer's architecture. 

2. To run a single simulation type: `python init.py`

3. To run a batch simulation type: `mpiexec -np 64 nrniv -python -mpi batch.py` where 64 is the number of cores used. 

## Overview of file structure:

* /batch.py: Runs the batch simulations

* /init.py: Main executable; calls functions from other modules. Sets what parameter file to use.

* /netParams.py: Network parameters

* /cfg.py: Simulation configuration

## Expected outputs

If the simulation runs correctly the following files are expectes as outputs:
1. 441 `data.json` which contain the simulation data, the network parameters and the simulation configuration for all simulations run
2. 441 `spike_data.json` which contain the spike times of all cells for all simulations run
3. 441 rater plots, 1 for each simulation
4. 441 `.run ` and `.err` files, which contain the standard output and error for each simulation.
5. A copy of the original `netParams.py` and `batch.py` files
6. a `.json` file with the batch parameters and run option used.


## Contact information

For further information please contact: ely97ber@gmail.com 

[Cutsuridis et al]: https://onlinelibrary.wiley.com/doi/10.1002/hipo.20661
