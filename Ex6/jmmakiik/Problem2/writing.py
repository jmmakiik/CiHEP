import ROOT
from array import array

N = 1000
variable = array("f",[0])
ROOT.gRandom.SetSeed(7)
	
writing = ROOT.TFile("writing.root","RECREATE")
tree1 = ROOT.TTree("MyTree","tree")
tree1.Branch("Random_Gaussian_numbers",variable,"variable/F")
	
for i in range(0,N,1):
    variable[0] = ROOT.gRandom.Gaus()
    tree1.Fill()
	
tree1.Write()
writing.Close()
