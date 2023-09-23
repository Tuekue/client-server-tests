import ujson

with open("default.json", "r") as f:
    data = ujson.load(f)

client_jdata = ujson.dumps(data)
print("data", type(data))
print(data)
print("j data", type(client_jdata))
print(client_jdata)

print(data['gsu']['IP'])
print(data['gsu']['DISKS']['sda3'])
print(data['opcon-17']['DISKS'])

