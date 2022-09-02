from netpyne import specs
from netpyne.batch import Batch


def batchRemoveConns():
        # Create variable of type ordered dictionary (NetPyNE's customized version)
        params = specs.ODict()

        # fill in with parameters to explore and range of values (key has to coincide with a variable in simConfig)
        params['receptorRemoved'] = ['AMPA', 'NMDA', 'Both']
        params['lesion_CA3'] = list(range(0,20+1))
        params['percent_lesion_CA1'] = [0, 1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        # create Batch object with parameters to modify, and specifying files to use
        b = Batch(params=params, cfgFile='nrn_cfg.py', netParamsFile='netParams.py',)

        # Set output folder, grid method (all param combinations), and run configuration
        b.batchLabel = 'removeCA3'
        b.saveFolder = 'removeCA3toCA1'
        b.method = 'grid'
        b.runCfg = {'type': 'mpi_bulletin', 
                        'script': 'init.py', 
                        'skip': True}


        # Run batch simulations
        b.run()

# Main code
if __name__ == '__main__':
        batchRemoveConns()