from netpyne import specs, sim
# from netParams import STARTDEL, THETA

#############################################
####		SIMULATION PARAMETERS		#####
#############################################

cfg = specs.SimConfig()

STARTDEL = 50.	# msecs
THETA = 250.	 # msecs (4 Hz)

cfg.dt = 0.05                 # Internal integration timestep to use
cfg.verbose = 0
# cfg.duration = 1
cfg.duration = STARTDEL + THETA*8
#cfg.duration = STARTDEL + THETA
cfg.recordStim = True
cfg.recordStep = 0.1             # Step size in ms to save data (e.g. V traces, LFP, etc)
sim.updateInterval = STARTDEL + THETA*4

cfg.hParams['celsius'] = 34.

cfg.saveJson = True
cfg.analysis['plotRaster'] = True   # Plot a raster
cfg.analysis['plotRaster'] = {'saveData': True, 'saveFig': True} # Plot raster 
cfg.saveDataInclude=['simData', 'netParams', 'simConfig']

# For batch simulations
cfg.lesion_CA3 = 5
cfg.percent_lesion_CA1 = 10
cfg.receptorRemoved = 'NMDA'