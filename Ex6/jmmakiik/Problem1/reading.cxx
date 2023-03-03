#include "TTree.h"
#include "TBranch.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TH1F.h"

using namespace std;

int main(){

    TFile f("writing.root");
    TTree* readtree = (TTree*)f.Get("MyTree");    

    Float_t variable[0];
    readtree->SetBranchAddress("Random_Gaussian_numbers",&variable);
//    readtree.Branch.SetAddress(&variable);
    
    TH1F histo("Histogram","",100,-5,5);
    histo.SetStats(0);
    
    Int_t nevents = readtree->GetEntries();

    for(Int_t i = 0; i < nevents; ++i){
      readtree->GetEntry(i);
      histo.Fill(variable[0]);
    }
    
    TCanvas canvas("reading","",500,500);
    canvas.cd();
    
    histo.SetLineColor(1);
    histo.SetLineWidth(2);
    histo.SetFillColor(5);
    histo.SetTitle("Histogram of random numbers fitted with Gaussian");
    histo.GetXaxis()->SetTitle("Random number");
    histo.GetYaxis()->SetTitle("Number of occurences");
    histo.Fit("gaus");
    histo.Draw("");
    canvas.Print("histogram.C");
    canvas.Print("histogram.png");
}

//I wasn't able to change the linewidth of the fit as with Python or last week with ROOT only. 
//It always gave me an error so decided not to include it on this exercise.
