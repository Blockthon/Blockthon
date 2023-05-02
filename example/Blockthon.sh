#!/bin/bash

PrivateKey() {
    hexdump -n 32 -e '8/4 "%08X" 1 "\n"' /dev/random
}

PrivateKey_To_Dec() {
      printf "%064x" $1
}

PrivateKey_To_Bytes() {
    echo -n $1 | xxd -r -p
}

Bytes_To_Mnemonic() {
    mnemonic=$(python3 -c "from mnemonic import Mnemonic; print(Mnemonic('english').to_mnemonic('$1'))")
    echo $mnemonic
}

Bytes_To_PrivateKey() {
    echo -n $1 | xxd -p -c 1000
}

PrivateKey_To_Mnemonic() {
    Byte_String=$(PrivateKey_To_Bytes $1)
    mnemonic=$(python3 -c "from mnemonic import Mnemonic; print(Mnemonic('english').to_mnemonic('$Byte_String'))")
    echo $mnemonic
}

Bytes_To_WIF() {
    if [ "$2" = true ]; then
        wif=$(python3 -c "from bit import Key; from bit.format import bytes_to_wif; print(bytes_to_wif('$1', compressed=True))")
    else
        wif=$(python3 -c "from bit import Key; from bit.format import bytes_to_wif; print(bytes_to_wif('$1'))")
    fi
    echo $wif
}


Balance() {
    url="https://bitcoin.atomicwallet.io/api/v1/address/$1"
    request_send=$(curl -s $url)
    balance_response=$(echo $request_send | jq -r '.balance')
    echo "$balance_response/100000000" | bc -l
}

