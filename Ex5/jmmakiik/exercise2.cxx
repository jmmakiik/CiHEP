void exercise2(){

    TFile* ffile = TFile::Open("exercise1.root");
    TTree* readtree = (TTree*)ffile->Get("MyTree");    

    Float_t variable;
    TBranch* branch = readtree->GetBranch("Random_Gaussian_numbers");
    branch->SetAddress(&variable);
    
    TH1F* histo = new TH1F("Histogram","",100,-5,5);
    histo->SetStats(0);

    for(size_t i = 0; i < readtree->GetEntries(); ++i){
      readtree->GetEvent(i);
      histo->Fill(variable);
    }
    
    TCanvas* canvas = new TCanvas("exercise2","",500,500);
    canvas->cd();
    
    TF1 *gaus = new TF1("gaus","gaus",-5,5);
    gaus->SetLineWidth(4);
    
    histo->SetLineColor(1);
    histo->SetLineWidth(2);
    histo->SetFillColor(5);
    histo->SetTitle("Histogram of random numbers fitted with Gaussian");
    histo->GetXaxis()->SetTitle("Random number");
    histo->GetYaxis()->SetTitle("Number of occurences");
    histo->Fit(gaus);
    histo->Draw("");
    canvas->Print("histogram.C");
}
