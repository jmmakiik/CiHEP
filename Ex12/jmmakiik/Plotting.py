from ROOT import *

file1 = TFile.Open("Problem1.root", "READ")
histo1 = file1.Get("npileups")

canvas1 = TCanvas("Canvas1", "", 700, 700)
canvas1.SetFillColor(0)
canvas1.cd()

histo1.SetLineColor(1)
histo1.SetLineWidth(2)
histo1.SetFillColor(5)
histo1.SetTitle("Histogram of pileups with COFFEA")
histo1.GetXaxis().SetTitle("Amount of primary vertices")
histo1.GetYaxis().SetTitle("Number of occurences")
histo1.Draw("")
canvas1.Print("Problem1_plot.C")
canvas1.Print("Problem1_plot.png")

file2 = TFile.Open("Problem2.root", "READ")
histo2 = file2.Get("npileups")

canvas2 = TCanvas("Canvas2", "", 700, 700)
canvas2.SetFillColor(0)
canvas2.cd() 

histo2.SetLineColor(1)
histo2.SetLineWidth(2)
histo2.SetFillColor(5)
histo2.SetTitle("Histogram of pileups with RDataFrame")
histo2.GetXaxis().SetTitle("Amount of primary vertices")
histo2.GetYaxis().SetTitle("Number of occurences")
histo2.Draw("")
canvas2.Print("Problem2_plot.C")
canvas2.Print("Problem2_plot.png")
