import ROOT
from array import array

ffile = ROOT.TFile.Open("writing.root")
readtree = ffile.Get("MyTree")   

variable = array("f", [0])
branch = readtree.GetBranch("Random_Gaussian_numbers")
branch.SetAddress(variable)

histo = ROOT.TH1F("Histogram","",100,-5,5)
histo.SetStats(0)

for i in range(0,readtree.GetEntries(),1):
    readtree.GetEvent(i)
    histo.Fill(variable[0])
    
canvas = ROOT.TCanvas("reading","",500,500)
canvas.cd()
gaus = ROOT.TF1("gaus","gaus",-5,5)
gaus.SetLineWidth(4)
    
histo.SetLineColor(1)
histo.SetLineWidth(2)
histo.SetFillColor(5)
histo.SetTitle("Histogram of random numbers fitted with Gaussian")
histo.GetXaxis().SetTitle("Random number")
histo.GetYaxis().SetTitle("Number of occurences")
histo.Fit(gaus)
histo.Draw("")
canvas.Print("histogram.C")
canvas.Print("histogram.png")