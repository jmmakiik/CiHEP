import pythia8
pythia = pythia8.Pythia()

pythia.readString("Beams:eCM = 13600")
pythia.readString("HiggsSM:all = on")
pythia.readString("PhaseSpace:mHatMin = 100.")
#pythia.readString("Next:numberShowEvent = 0")
#pythia.readString("PDF:pSet = LHAPDF6:cteq6l1")

pythia.init()

Higgs = 25

for i in range(0, 1000):
	if pythia.next() != True: continue
	iD = 0
	for j in range(0,pythia.event.size()):
		if pythia.event[j].id() == Higgs:
			iD = j
	print("Higgs mass",i+1,"is",pythia.event[iD].m())
