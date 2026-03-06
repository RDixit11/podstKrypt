#!/bin/bash
if [[ $1 != *.txt ]]; 
then
	echo "Wrong file format"
	exit 1
fi

for i in {1..20000};
do
	python3 main.py bbs 15 >> $1
	echo "generating series: $i/20000" 
done
