import numpy as np
import multiprocessing
import hist
import uproot
from coffea import processor

class Analysis(processor.ProcessorABC):
    	def __init__(self):
        	self.histograms = {}
        	self.histograms["npileups"] = (hist.Hist.new.Reg(200, 0 ,200, name="x", label="Amount of primary vertices").Double()) 
        	
    	def process(self, events):
        	self.histograms["npileups"].fill(x=events[events.HLT_IsoMu24 == True].PV_npvs)
        	out = {}
        	out.update(self.histograms)
        	return out
        	
    	def postprocess(self, accumulator):
        	pass
        	
def main():
	MAX_WORKERS = max(multiprocessing.cpu_count()-1,1)
	CHUNKSIZE = 1000000
	MAXCHUNKS = None
	
	rootfile = {'DYJetsToLL': ['DYJetsToLL.root']}
	
	job_executor = processor.FuturesExecutor(workers = MAX_WORKERS)
	
	run = processor.Runner(executor = job_executor, chunksize = CHUNKSIZE, maxchunks = MAXCHUNKS)
	
	result = run(rootfile, 'Events', Analysis())
	
	with uproot.recreate("Problem1.root") as fOUT:
		for key in result.keys():
			fOUT[f"{key}"] = result[key]
            		
if __name__ == "__main__":
	main()
        	
