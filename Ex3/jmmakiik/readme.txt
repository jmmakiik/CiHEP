The following command may need to be written to the terminal to have everything working correctly:

export LD_LIBRARY_PATH=~/path/to/library 
(for example for me, path was ~/CiHEP/Ex3/jmmakiik)

This is for the programs and compilations to know where everything is. Without it, I wasn't able get anything out. You can use "echo $LD_LIBRARY_PATH" to see if the program/computer/compilation knows where the wanted files are.

The job file created should do everything needed (run the make file, give permissions to everything to use and run the test program using Testexe). All one has to do is write ./Test.job to run everything (if something goes wrong, check the description about path before).
