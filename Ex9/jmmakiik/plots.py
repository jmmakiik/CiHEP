from ROOT import *
import re
from array import array
import numpy as np

#Reading the values from the text file to arrays
with open("resultlist.txt") as file:
	data = [line.strip() for line in file]

eta = []
pT = []	

for line in data:
	datas = line.split()
	pT.append(float(datas[0]))
	eta.append(float(datas[1]))

file.close()

total = len(pT)

p = array("f",[0])
e = array("f",[0])

#Creating a ROOT file for the results
	
resultfile = TFile("result.root","RECREATE")
tree1 = TTree("Transverse_momentum","treep")
tree1.Branch("p",p,"p/F")
tree2 = TTree("Pseudorapidity","treee")
tree2.Branch("e",e,"e/F")
	
for i in range(0,total):
	p[0] = pT[i]
	tree1.Fill()
	e[0] = eta[i]
	tree2.Fill()
	
tree1.Write()
tree2.Write()
resultfile.Close()

#Reading the created root file and plotting transverse momentum pT
		
ffile = TFile.Open("result.root", "READ")	
readtree1 = ffile.Get("Transverse_momentum")  
		
branch1 = readtree1.GetBranch("p")
branch1.SetAddress(p)
	
histo1 = TH1F("Histogram","",100,np.floor(min(pT)),np.ceil(max(pT)))
histo1.SetStats(0)
	
for i in range(0,readtree1.GetEntries(),1):
	readtree1.GetEvent(i)
	histo1.Fill(p[0])
	
canvas1 = TCanvas("transverse_momentum","",700,700)
canvas1.cd()

histo1.SetLineColor(1)
histo1.SetLineWidth(2)
histo1.SetFillColor(5)
histo1.SetTitle("Histogram of transverse momentum")
histo1.GetXaxis().SetTitle("Transverse momentum")
histo1.GetYaxis().SetTitle("Number of occurences")
histo1.Draw("")
canvas1.Print("pTplot.C")
canvas1.Print("pTplot.png")

#Copy of the previous lines to plot pseudorapidity
readtree2 = ffile.Get("Pseudorapidity")  
		
branch2 = readtree2.GetBranch("e")
branch2.SetAddress(p)
	
histo2 = TH1F("Histogram","",100,np.floor(min(eta)),np.ceil(max(eta)))
histo2.SetStats(0)
	
for i in range(0,readtree2.GetEntries(),1):
	readtree2.GetEvent(i)
	histo2.Fill(p[0])
	
canvas2 = TCanvas("pseudorapidity","",700,700)
canvas2.cd()

histo2.SetLineColor(1)
histo2.SetLineWidth(2)
histo2.SetFillColor(5)
histo2.SetTitle("Histogram of pseudorapidity")
histo2.GetXaxis().SetTitle("Pseudorapidity")
histo2.GetYaxis().SetTitle("Number of occurences")
histo2.Draw("")
canvas2.Print("etaplot.C")
canvas2.Print("etaplot.png")

#Calculating and printing the probability for muon detection in the specified ranges
detected = 0

for iD in range(len(pT)):
	if float(pT[iD]) > 5 and np.abs(float(eta[iD])) < 2.5:
		detected += 1
		
print("For problem 2, the probability of detecting a muon from a minimum bias event is %.5f" % float(detected/total))
