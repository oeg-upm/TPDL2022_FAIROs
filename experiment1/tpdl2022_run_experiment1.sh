#!/bin/bash
for i in $(ls -d $1); do 
	echo ${i%%/}
	file="$(basename -- $i)"
	parameters='-ro '${i%%/}' -o results/experiment1/FAIR_validation_'$file'_mode0.json -m true -a 0'
    	python3 $2 $parameters 
	parameters='-ro '${i%%/}' -o results/experiment1/FAIR_validation_'$file'_mode1.json -m true -a 1'
	python3 $2 $parameters
done
