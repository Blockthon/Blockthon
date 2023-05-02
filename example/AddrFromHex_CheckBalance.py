from Blockthon import PrivateKey, Addr_From_PrivateKey, Balance


z = 0
f = 0
while True:
    z += 1
    key = PrivateKey()
    caddr = Addr_From_PrivateKey(key, compress=True)
    uaddr = Addr_From_PrivateKey(key)
    cbal = Balance(caddr)
    ubal = Balance(uaddr)
    if cbal != '0' or ubal != '0':
        f += 1
        open("found.txt", "a").write(f"{caddr} : {cbal}\n{uaddr} : {ubal}\n{key}\n")
    else:
        print(f"[{z}] # Found:{f} > {caddr} : {cbal} # {uaddr} : {ubal}")
