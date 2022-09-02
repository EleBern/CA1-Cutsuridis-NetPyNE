# CA1-NetPyNE-model

## Description
NetPyNE (www.netpyne.org) version of a model of CA1 microcircuits published by [Cutsuridis et al].

Original model and publication: https://modeldb.yale.edu/234233 

This is a functional model of the CA1 that studies the storage and retrieval of spatiotemporal patterns.

## Setup

Requires NEURON with Python. The following commands are for Linux users. 

1. Install NEURON
`pip install neuron`

2. Install NetPyNE
`pip install netpyne`

3. Install other required Python packages (numpy, matplotlib)
`pip install numpy matplotlib`

## Execution

1. Type `nrnivmodl mod` to compile the `.mod` files. This should create a directory called either i686 or x86_64, depending on your computer's architecture. 

2. To run type: `python init.py`

## Overview of file structure:

* /init.py: Main executable; calls functions from other modules. Sets what parameter file to use.

* /netParams.py: Network parameters

* /cfg.py: Simulation configuration

* /convert_cell_models.py: Generates `.json` files of all cell types. Converts NEURON `.hoc` files to NetPyNE. 

## Expected outputs

If the simulation runs correctly the following files are expectes as outputs:
1. `model_output.json` which contains the simulation data, the network parameters and the simulation configuration
2. `rater_data.json` which contains the spike times of all cells
3. 2 figures, 1 with the voltage trace and 1 rater plot

## Useful information 

In the `netParams.py` file,
`FPATT` at line 308 indicates the pattern file to be used in the simulation.
`FCONN` at line 374 defines the weights between CA1 and CA3 pyramidal cells, the ones that can be modified by an STDP learning rule to memorize a new pattern.

To test only retrieval of a pattern:
- `FPATT` at line 308 and `FCONN` at line 374 must be equivalent. For example:
`FCONN = "Weights/wgtsN100S20P5.dat"` and `FPATT = "Weights/pattsN100S20P1.dat"`
- The STDP depression and potentiation factiors `STDPDFAC` and `STDPPFAC` at lines 160 and 161 must be set to 0
- The EC input weight `ECWGT` at line 143 must be set to 0

To test only storage of a pattern:
- `FPATT` at line 308 and `FCONN` at line 374 must be different. For example:
`FCONN = "Weights/wgtsN100S20P5.dat"` and `FPATT = "Weights/pattsN100S20P10.dat"`
- The STDP depression and potentiation factiors `STDPDFAC` and `STDPPFAC` at lines 160 and 161 must NOT be 0
- The EC input weight `ECWGT` at line 143 must NOT be 0
- In the `init.py` file, run the simulation with `sim.run()` instead of `sim.runSimWithIntervalFunc(sim.updateInterval, removeStore)`

To test both storage and retrieval of a pattern follow the instructions for testing only storage, but run the simulation with `sim.runSimWithIntervalFunc(sim.updateInterval, removeStore)`.

## Contact information

For further information please contact: ely97ber@gmail.com 

[Cutsuridis et al]: https://onlinelibrary.wiley.com/doi/10.1002/hipo.20661
