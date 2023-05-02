#!/bin/bash
# First install jq for json and bc for busybox 
source Blockthon.sh

filename='address.txt'

while read -r addr; do
  addr=$(echo $addr | tr -d '
')
  bal=$(Balance $addr)

  echo "Address: $addr : Balance: $bal"
done < "$filename"
