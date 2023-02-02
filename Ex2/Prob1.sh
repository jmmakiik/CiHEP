#!/bin/bash

for i in {1..10}
do
	~/CiHEP/Ex2/Prob1 $i > hello_${i}
	echo "Run $i complete"
done

wait
echo "All runs completed and files generated"
