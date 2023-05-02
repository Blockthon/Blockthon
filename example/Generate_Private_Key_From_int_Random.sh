#!/bin/bash
source Blockthon.sh

z=0
while true
do
  d=$((19999999999999999 + RANDOM % 999999999999999999999999999999999999))
  key=$(PrivateKey $d)
  ((z++))
  echo -ne "Total: $z $key\r"
done
