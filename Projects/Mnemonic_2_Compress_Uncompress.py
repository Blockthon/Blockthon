from Blockthon import Wallet, Check
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
    print(f"{red}+ {off}{green}Mnemonic  : {off}{mnemonic_string}")
    print(f"{red}+ {off}{green}PrivateKey: {off}{privatekey}")
    table = [
        [f"{red}Compressed Address{off}", compress_addr, f"{green}BALANCE:{cyan}{compress_bal}{off}"],
        [f"{red}Uncompressed Address{off}", uncompress_addr, f"{green}BALANCE:{cyan}{uncompress_bal}{off}"],
        [f"{cyan}CHECKED{off}", count, f"{red}FOUND:{off} {cyan}{found}{off}"]
    ]
    print(tabulate(table, tablefmt="grid"))
