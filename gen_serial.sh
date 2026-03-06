#!/bin/bash
if [[ $1 != *.txt ]]; 
then
	echo "Wrong file format"
	exit 1
fi

for i in {1..20};
do
	python3 main.py bbs 15 >> $1
done
