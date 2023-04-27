from ROOT import *
ROOT.EnableImplicitMT()

def main():
	events = ROOT.RDataFrame("Events", "DYJetsToLL.root")
	events = events.Filter("HLT_IsoMu24", "Events passing the trigger")
	
	filtered_events = events.Define("Passed_particles", "PV_npvs")
	histo = filtered_events.Histo1D(("npileups", ";Amount of primary vertices;Amount of events", 200, 0, 200), "PV_npvs")
	
	fOUT = TFile.Open("Problem2.root","RECREATE")
	histo.Write()
	fOUT.Close()

if __name__ == "__main__":
	main()
