#!/bin/bash

echo "Dlugosc-slowa,Proby-do-kolizji" > coll.csv

for ((i=1; i<6;i++)); do
	x=$((10**i))
	for ((j=0; j<100; j++)); do
		echo -n "$x;" >> coll.csv
		python3 main.py coll "$x" | grep "ATTEMPT:" | awk '{print $2}' | paste -sd ";" - >> coll.csv
	done
done
