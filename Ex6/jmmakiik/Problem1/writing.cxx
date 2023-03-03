#include <iostream>

#include "TTree.h"
#include "TBranch.h"
#include "TFile.h"
#include "TRandom.h"

using namespace std;

int main(){

  Int_t N = 1000;
  Float_t variable[0];
  gRandom->SetSeed(7);
  
  TFile f("writing.root","RECREATE");
  TTree tree1("MyTree","tree");
  tree1.Branch("Random_Gaussian_numbers",&variable,"variable/F");

  for(Int_t i = 0; i < N;i++){
    variable[0] = gRandom->Gaus();
    tree1.Fill();
  }
  
  tree1.Write();
  f.Close();
  
}
