import re
import ROOT
from array import array

with open(r"br.sm2") as f:
    linesHDECAY = f.readlines()

valuelines = r"[0-9]"

massesHDECAY = []
widthsHDECAY = []
massesFH = []
widthsFH = []
ratios = []

for line in linesHDECAY:
    matchvalue = re.search(valuelines, line)
    if matchvalue != None:
        mass_value = "%.3f" % float(line[0:11].strip())
        width_value = "%.4f" % float(line[68:-1].strip())
        massesHDECAY.append(float(mass_value))
        widthsHDECAY.append(float(width_value))
        continue
    continue

N = len(massesHDECAY)
	
canvas = ROOT.TCanvas("Width as a function of mass","",1000,1000)
canvas.SetFillColor(0)

frame = ROOT.TH2F("graph","Width as a function of mass",1,100,550,300,0.001,300)
frame.SetStats(0)
frame.GetXaxis().SetTitle("m_{H} (GeV)")
frame.GetYaxis().SetTitle("#Gamma(H_{SM})")
frame.GetYaxis().SetTitleOffset(1.25)
frame.Draw("same")
ROOT.gPad.SetLogy()

massesarr = array("d", massesHDECAY)
widthsarr = array("d", widthsHDECAY)

graph = ROOT.TGraph(N,massesarr,widthsarr)
graph.SetMarkerStyle(2)
graph.SetLineColor(2)
graph.SetLineWidth(4)
graph.Draw("L")

canvas.Print("Problem1.png")
canvas.Print("Problem1.C")

print("The width for m_H = 125 GeV using HDECAY is",widthsHDECAY[0])



