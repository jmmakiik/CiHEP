import pythia8
pythia = pythia8.Pythia()

pythia.readString("Beams:eCM = 13000.")
pythia.readString("SoftQCD:nonDiffractive = on") #This is for minumum-bias setting
pythia.readString("Next:numberShowEvent = 0")
pythia.init();

pT_and_eta = {}

for i in range(0, 30000):
	if pythia.next() != True: continue
	iD = 0
	for j in range(0,pythia.event.size()):
		if pythia.event[j].id() == 13: #Checking if the program produces muons
			iD = j
	if str(pythia.event[iD].pT()) != "0.0":
		pT_and_eta[pythia.event[iD].pT()] = pythia.event[iD].eta()
		
with open("resultlist.txt", "w+") as file:
	for pT, eta in pT_and_eta.items():
		file.write("%s %s\n" % (pT,eta))
