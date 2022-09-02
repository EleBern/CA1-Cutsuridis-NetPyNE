from netpyne import sim, specs
from neuron import gui

netParams = specs.NetParams()

#############################################
netParams.importCellParams(label='Pyramidalcell', conds={'cellType': 'Pyramidalcell', 'cellModel': 'Pyramidal_model'}, \
fileName='pyramidal_cell_14Vb.hoc', cellName='PyramidalCell', importSynMechs=False)

netParams.importCellParams(label='OLMcell', conds={'cellType': 'OLMcell', 'cellModel': 'OLM_model'}, \
fileName='olm_cell2.hoc', cellName='OLMCell', importSynMechs=False)
#netParams.cellParams['OLMcell'].globals.Rm=20000.

netParams.importCellParams(label='BScell', conds={'cellType': 'BScell', 'cellModel': 'BS_model'}, \
fileName='bistratified_cell13S.hoc', cellName='BistratifiedCell', importSynMechs=False)

netParams.importCellParams(label='Basketcell', conds={'cellType': 'Basketcell', 'cellModel': 'B_model'}, \
fileName='basket_cell17S.hoc', cellName='BasketCell', importSynMechs=False)

netParams.importCellParams(label='AAcell', conds={'cellType': 'AAcell', 'cellModel': 'AA_model'}, \
fileName='axoaxonic_cell17S.hoc', cellName='AACell', importSynMechs=False)
    
#Setting thresholds

cells=['Pyramidalcell','OLMcell','BScell','Basketcell','AAcell']

for i in cells:
 	for sec in netParams.cellParams[i].secs:
  		netParams.cellParams[i].secs[sec].threshold = -10.0    
    
    
netParams.saveCellParamsRule(label='Pyramidalcell', fileName='Pyramidalcell.json')

netParams.saveCellParamsRule(label='OLMcell', fileName='OLMcell.json')

netParams.saveCellParamsRule(label='BScell', fileName='BScell.json')

netParams.saveCellParamsRule(label='Basketcell', fileName='Basketcell.json')

netParams.saveCellParamsRule(label='AAcell', fileName='AAcell.json')