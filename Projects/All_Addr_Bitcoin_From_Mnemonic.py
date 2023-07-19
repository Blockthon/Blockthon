from Blockthon import Wallet, Check, Bitcoin
from tabulate import tabulate
from colorthon import Colors
# ===================
red = Colors.RED
green = Colors.GREEN
cyan = Colors.CYAN
off = Colors.RESET
# ===================
count = 0
found = 0
while True:
    count += 1
    # Generate Mnemonic with word 12 without a repeat
    mnemonic_string = Wallet.getMnemonic(12)
    # convert mnwmonic to bytes (seed)
    seed = Wallet.Mnemonic_To_Bytes(mnemonic_string)
    # convert bytes (seed) to private key (hex)
    privatekey = seed.hex()
    # connvert Bytes (seed) to compressed address
    compress_addr = Wallet.Bytes_To_Address(seed, compress=True)
    # check value balance compressed address
    compress_bal = Check.Btc_Balance(compress_addr)
    # convert bytes to uncompressed address
    uncompress_addr = Wallet.Bytes_To_Address(seed)
    # check value balance uncompressed address
    uncompress_bal = Check.Btc_Balance(uncompress_addr)
    # generated P2sh Address from private key Hex
    p2sh_addr = Bitcoin.Address_From_PrivateKey(privatekey, 'P2SH')
    # Check value Balance From P2SH Address
    p2sh_bal = Check.Btc_Balance(p2sh_addr)
    # generated P2wsh Address from private key Hex
    p2wsh_addr = Bitcoin.Address_From_PrivateKey(privatekey, 'P2WSH')
    # Check value Balance From P2WSH Address
    p2wsh_bal = Check.Btc_Balance(p2wsh_addr)
    # generated P2WPKH Address from private key Hex
    p2wpkh_addr = Bitcoin.Address_From_PrivateKey(privatekey, 'P2WPKH')
    # Check value Balance From P2WPKH Address
    p2wpkh_bal = Check.Btc_Balance(p2wpkh_addr)
    print(f"{red}+ {off}{green}Mnemonic  : {off}{mnemonic_string}")
    print(f"{red}+ {off}{green}PrivateKey: {off}{privatekey}")
    table = [
        [f"{red}Compressed Address{off}", compress_addr, f"{green}BALANCE:{cyan}{compress_bal}{off}"],
        [f"{red}Uncompressed Address{off}", uncompress_addr, f"{green}BALANCE:{cyan}{uncompress_bal}{off}"],
        [f"{red}P2SH Address{off}", p2sh_addr, f"{green}BALANCE:{cyan}{p2sh_bal}{off}"],
        [f"{red}P2WSH Address{off}", p2wsh_addr, f"{green}BALANCE:{cyan}{p2wsh_bal}{off}"],
        [f"{red}P2WPKH Address{off}", p2wpkh_addr, f"{green}BALANCE:{cyan}{p2wpkh_bal}{off}"],
        [f"{cyan}CHECKED{off}", count, f"{red}FOUND:{off} {cyan}{found}{off}"]
    ]
    print(tabulate(table, tablefmt="grid"))
