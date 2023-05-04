# //////////////////////////////////////////////////
# // Github : github.com/Pymmdrza                 //
# // official Page : https://github.com/Blockthon //
# //////////////////////////////////////////////////

from Blockthon import PrivateKey, Addr_From_PrivateKey, Balance

# import address from text file : address.txt

filename = 'address.txt'
# open and read address file
richFile = [i.strip() for i in open(filename).readlines()]
# Count for total checking
count = 0
for check in range(len(richFile)):
    count += 1
    addr = richFile[check]
    bal = Balance(address=addr)
    print(count, addr, bal)
