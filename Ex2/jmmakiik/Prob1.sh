#!/bin/bash

for i in {1..10}
do
	~/CiHEP/Ex2/jmmakiik/Prob1 $i > hellosh_${i} #Path has to be changed depending on where the files are (removing/replacing /CiHEP part for example)

	echo "Run $i complete"
done

wait
echo "All runs completed and files generated"
