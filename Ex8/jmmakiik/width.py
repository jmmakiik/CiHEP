from ROOT import *
import re
from array import array

index1 = 0
key1 = re.compile(" id ")
key2 = re.compile(" [a-zA-Z]+")
for row, line in enumerate(open("particlelist.txt")):
	for i in re.finditer(key1, line):
		for j in re.finditer(key2, line):
			if j.group() == " mWidth":
				break
			index1 += 1
					
index2 = 1			
higgskey1 = re.compile("h0")
higgskey2 = re.compile(" [a-zA-Z0-9]+\.*[a-zA-Z0-9]*")
for row, line in enumerate(open("particlelist.txt")):
	for i in re.finditer(higgskey1, line):
		for j in re.finditer(higgskey2, line):
			if index2 == index1: width1 = j.group()
			index2 += 1
	

massvalues = []
key = re.compile("Higgs mass \d*\ is \d*\.\d*")
for row, line in enumerate(open("mass.txt")):
	for match in re.finditer(key, line):
		masses = match.group().split(" ")
		massvalues.append(float(masses[-1]))

variable = array("f",[0])
N = len(massvalues)
	
widthrootfile = TFile("width.root","RECREATE")
tree1 = TTree("MyTree","tree")
tree1.Branch("Higgs_masses",variable,"variable/F")
	
for i in range(0,N):
	variable[0] = massvalues[i]
	tree1.Fill()
tree1.Write()
widthrootfile.Close()
	
ffile = TFile.Open("width.root")	
readtree = ffile.Get("MyTree")  
		
branch = readtree.GetBranch("Higgs_masses")
branch.SetAddress(variable)
	
histo = TH1F("Histogram","",100,124.5,125.5)
histo.SetStats(0)
	
for i in range(0,readtree.GetEntries(),1):
	readtree.GetEvent(i)
	histo.Fill(variable[0])
	
canvas = TCanvas("width","",700,700)
canvas.cd()

histo.SetLineColor(1)
histo.SetLineWidth(2)
histo.SetFillColor(5)
histo.SetTitle("Histogram of Higgs masses")
histo.GetXaxis().SetTitle("Higgs mass [GeV]")
histo.GetYaxis().SetTitle("Number of occurences")
histo.Draw("")
canvas.Print("histogram.C")
canvas.Print("histogram.png")
	
centervalue = 0
halfmax = histo.GetMaximum() / 2
for i in range(N):
	if histo.GetBinContent(i) > halfmax:
		centervalue += 1
		
width2 = histo.GetBinWidth(1)

print("Problem 1 answer is",width1,"GeV")
print("Problem 2 answer is",width2,"GeV")
