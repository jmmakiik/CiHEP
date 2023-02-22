void exercise1(){

  int N = 1000;
  Float_t variable;
  gRandom->SetSeed(7);
  
  TFile* exercise1 = new TFile("exercise1.root","RECREATE");
  TTree* tree1 = new TTree("MyTree","tree");
  tree1->Branch("Random_Gaussian_numbers",&variable,"variable/F");

  for(int i = 0; i < N;i++){
    variable = gRandom->Gaus();
    tree1->Fill();
  }
  
  tree1->Write();
  exercise1->Close();

}
