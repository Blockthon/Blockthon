# Blockthon

Blockthon is a Python library for generating and manipulating various cryptographic elements related to blockchain, such as private keys, addresses, mnemonics, and more.

## Installation

To use Blockthon, you can install it via pip:

```shell
pip install Blockthon
```
on linux use `pip3`:
```shell
sudo apt-get update&&sudo apt-get upgrade -y
sudo apt-get install -y autoconf automake build-essential libffi-dev libtool pkg-config python3-dev
# after installing run cammand 
pip3 install blockthon
```

## Usage

Here are some examples of how to use the functions provided by Blockthon:

- **Generating a random private key**: This example demonstrates how to generate a random private key using the `getPrivateKey()` function from the `Wallet` class.

- **Generating a random mnemonic**: This example showcases how to generate a random mnemonic using the `getMnemonics()` function from the `Wallet` class.

- **Generating random bytes (seed)**: This example illustrates how to generate random bytes (seed) using the `getSeed()` function from the `Wallet` class.

- **Generating a random binary number**: This example shows how to generate a random binary number using the `getBinary()` function from the `Wallet` class.

- **Converting a private key from hex to binary**: This example demonstrates how to convert a private key from hexadecimal to binary format using the `PrivateKey_To_Binary()` function from the `Wallet` class.

- **Converting a private key from hex to bytes (seed)**: This example showcases how to convert a private key from hexadecimal to bytes (seed) using the `PrivateKey_To_Bytes()` function from the `Wallet` class.

- **Converting a private key from hex to decimal number**: This example illustrates how to convert a private key from hexadecimal to decimal number using the `PrivateKey_To_Dec()` function from the `Wallet` class.

- **Converting a private key from hex to mnemonic**: This example shows how to convert a private key from hexadecimal to mnemonic using the `PrivateKey_To_Mnemonic()` function from the `Wallet` class.

- **Converting a private key from hex to RIPEMD160**: This example demonstrates how to convert a private key from hexadecimal to RIPEMD160 format using the `PrivateKey_To_RIPEMD160()` function from the `Wallet` class.

- **Converting a private key from hex to address**: This example showcases how to convert a private key from hexadecimal to address format using the `PrivateKey_To_Address()` function from the `Wallet` class.

- **Converting a private key from hex to compressed Bitcoin address**: This example illustrates how to convert a private key from hexadecimal to compressed Bitcoin address format using the `PrivateKey_To_Compress_Addr()` function from the `Wallet` class.

- **Converting a private key from hex to uncompressed Bitcoin address**: This example shows how to convert a private key from hexadecimal to uncompressed Bitcoin address format using the `PrivateKey_To_UnCompress_Addr()` function from the `Wallet` class.

- **Converting a private key to a public key**: This example demonstrates how to convert a private key to a public key using the `PrivateKey_To_PublicKey()` function from the `Wallet` class.

- **Converting a private key to P2PKH Bitcoin address**: This example showcases how to convert a private key to a P2PKH (Pay-to-Public-Key-Hash) Bitcoin address using the `PrivateKey_P2PKH_Addr()` function from the `Wallet` class.

- **Converting a private key to P2SH Bitcoin address**: This example illustrates how to convert a private key to a P2SH (Pay-to-Script-Hash) Bitcoin address using the `PrivateKey_P2SH_Addr()` function from the `Wallet` class.

- **Converting a private key to P2WPKH Bitcoin address**: This example shows how to convert a private key to a P2WPKH (Pay-to-Witness-Public-Key-Hash) Bitcoin address using the `PrivateKey_P2WPKH_Addr()` function from the `Wallet` class.

- **Converting a private key to P2WSH Bitcoin address**: This example demonstrates how to convert a private key to a P2WSH (Pay-to-Witness-Script-Hash) Bitcoin address using the `PrivateKey_P2WSH_Addr()` function from the `Wallet` class.

- **Converting a private key to P2SH-P2WPKH Bitcoin address**: This example showcases how to convert a private key to a P2SH-P2WPKH (Pay-to-Script-Hash-Pay-to-Witness-Public-Key-Hash) Bitcoin address using the `PrivateKey_P2SH_P2WPKH_Addr()` function from the `Wallet` class.

- **Converting a mnemonic to a private key**: This example illustrates how to convert a mnemonic to a private key using the `Mnemonic_To_PrivateKey()` function from the `Wallet` class.

- **Converting a mnemonic to seed**: This example shows how to convert a mnemonic to seed using the `Mnemonic_To_Seed()` function from the `Wallet` class.

- **Converting a mnemonic to binary**: This example demonstrates how to convert a mnemonic to binary using the `Mnemonic_To_Binary()` function from the `Wallet` class.

- **Converting a mnemonic to a decimal number**: This example showcases how to convert a mnemonic to a decimal number using the `Mnemonic_To_Dec()` function from the `Wallet` class.

- **Converting a mnemonic to RIPEMD160**: This example illustrates how to convert a mnemonic to RIPEMD160 format using the `Mnemonic_To_RIPEMD160()` function from the `Wallet` class.

- **Converting a mnemonic to an address**: This example shows how to convert a mnemonic to an address using the `Mnemonic_To_Address()` function from the `Wallet` class.

- **Converting a mnemonic to compressed Bitcoin address**: This example demonstrates how to convert a mnemonic to a compressed Bitcoin address using the `Mnemonic_To_Compress_Addr()` function from the `Wallet` class.

- **Converting a mnemonic to uncompressed Bitcoin address**: This example showcases how to convert a mnemonic to an uncompressed Bitcoin address using the `Mnemonic_To_UnCompress_Addr()` function from the `Wallet` class.

These are just a few examples of the functionalities provided by Blockthon. You can explore the library and its documentation to discover more options and customize them according to your specific needs.
