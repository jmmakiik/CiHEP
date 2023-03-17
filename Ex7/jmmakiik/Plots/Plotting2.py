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

with open(r"output.txt") as f2:
    linesFH = f2.readlines()

for line in linesFH:
    y = line.split()
    massesFH.append(float(y[0]))
    widthsFH.append(float(y[1]))
    
for i in range(100):
    ratios.append(widthsFH[i]/widthsHDECAY[i])

N = len(massesHDECAY)
	
canvas = ROOT.TCanvas("Width as a function of mass","",1000,1000)
canvas.SetFillColor(0)
canvas.Divide(1,2)

canvas.cd(1)
frame = ROOT.TH2F("graph","Width as a function of mass",1,100,550,300,0.001,300)
frame.SetStats(0)
frame.GetXaxis().SetTitle("m_{H} (GeV)")
frame.GetYaxis().SetTitle("#Gamma(H_{SM})")
frame.GetYaxis().SetTitleOffset(1.25)
frame.Draw("same")
ROOT.gPad.SetLogy()

massesarr = array("d", massesHDECAY)
widthsarr = array("d", widthsHDECAY)
massesarr2 = array("d", massesFH)
widthsarr2 = array("d", widthsFH)
ratiosarr = array("d", ratios)

graph = ROOT.TGraph(N,massesarr,widthsarr)
graph.SetMarkerStyle(2)
graph.SetLineColor(2)
graph.SetLineWidth(4)
graph.Draw("L")

frame2 = ROOT.TH2F("graph2","Width as a function of mass",1,100,550,300,0.001,300)
frame2.SetStats(0)
frame2.GetXaxis().SetTitle("m_{H} (GeV)")
frame2.GetYaxis().SetTitle("#Gamma(H_{SM})")
frame2.GetYaxis().SetTitleOffset(1.25)
frame2.Draw("same")

graph2 = ROOT.TGraph(N,massesarr2,widthsarr2)
graph2.SetMarkerStyle(8)
graph2.SetLineColor(8)
graph2.SetLineWidth(2)
graph2.Draw("L")

leg = ROOT.TLegend()
leg.AddEntry(graph,"HDECAY", "l")
leg.AddEntry(graph2,"FeynHiggs","l")
leg.Draw()


canvas.cd(2)
frame3 = ROOT.TH2F("graph3","Ratio of widths",1,100,550,300,0.001,2)
frame3.SetStats(0)
frame3.GetXaxis().SetTitle("m_{H} (GeV)")
frame3.GetYaxis().SetTitle("#Gamma(H_{FH})/#Gamma(H_{HDECAY})")
frame3.Draw()

graph3 = ROOT.TGraph(N,massesarr2,ratiosarr)
graph3.SetMarkerStyle(8)
graph3.SetLineColor(1)
graph3.SetLineWidth(2)
graph3.Draw("L")


canvas.Print("Problem2.png")
canvas.Print("Problem2.C")

print("The width for m_H = 125 GeV using HDECAY is",widthsHDECAY[0])
print("The width for m_H = 125 GeV using FeynHiggs is",widthsFH[0])



