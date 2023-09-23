import ujson

with open("default.json", "r") as f:
    data = ujson.load(f)

client_jdata = ujson.dumps(data)
print("data", type(data))
print(data)
print("j data", type(client_jdata))
print(client_jdata)

print(data['10.1.1.254']['client_name'])
print(data['10.1.1.11']['DISKS'])

