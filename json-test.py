import json

data = {
    "client_name" : "test",
    "CPU" : 0,
    "GW" : "NA",
    "RAM" : 0,
    "DISK": 0
}

class Client_Info:
    def __init__(self, client_name, CPU, MEM, RAM, DISK):
        self.client_name = client_name
        self.CPU = CPU
        self.MEM = MEM
        self.RAM = RAM
        self.DISK = DISK
    
    def toJson(self):
        '''
        Serialize the object custom object
        '''
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


c1 = Client_Info("opcon_1", 23, 56, 56, 3)
c2 = Client_Info("opcon_2", 18, 89, 24, 13)

clients = []
clients.append(json.loads(c1.toJson()))
clients.append(json.loads(c2.toJson()))

json_data = json.dumps(clients)
print(repr(json_data))
print(type(json_data))
print(json.loads(c1.toJson()))



'''

client_jdata = json.dumps(data)
client_data = json.loads(client_jdata)
print("data")
print(type(data))
print("j data")
print(type(client_jdata))
print("c data")
print(type(client_data))

print(client_data['client_name'])
'''


