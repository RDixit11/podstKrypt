#!/bin/bash

echo "Dlugosc-slowa;procent-zmienionych-bitow" > sac.csv

for ((i=1; i<6;i++)); do
	x=$((10**i))
	for ((j=0;j<100;j++)); do
		echo -n "$x;" >> sac.csv
		python3 main.py sac $x | grep "BITS CHANGED:" | awk '{print $3}' | paste -sd ";" - >> sac.csv
	done
done
