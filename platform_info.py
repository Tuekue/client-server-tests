import platform
import psutil
import cpuinfo
import os


print(f"Architecture: {platform.architecture()}")
print(f"Network Name: {platform.node()}")
print(f"Operating Sysyem: {platform.platform()}")
print(f"Processor: {platform.processor()}")

my_cpuinfo = cpuinfo.get_cpu_info()
print(f"Full CPU Name: {my_cpuinfo['brand_raw']}")   # Dictionary 
print(f"Actual CPU speed: {my_cpuinfo['hz_actual_friendly']}")   # Dictionary 
print(f"CPU speed: {my_cpuinfo['hz_advertised_friendly']}")   # Dictionary 

mem = psutil.virtual_memory()
print(f"Total RAM : {mem.total / 1024 / 1024 / 1024:.2f} GB")
print(f"Used RAM: {mem.used / 1024 / 1024 / 1024:.2f} GB")
print(f"Free RAM: {mem.available / 1024 / 1024 / 1024:.2f} GB")
print(f"Used RAM %: {mem.percent}%")

THRESHOLD = 100 * 1024 * 1024  # 100MB
if mem.available <= THRESHOLD:
    print("warning")

if os.name != 'nt':
    print(f"Net Addrs: {psutil.net_if_addrs()}") 

'''
Limux altinda calisan diger faydali olabilecek psutil komutlari

    psutil.net_io_counters(pernic=False, nowrap=True)
    psutil.net_connections(kind='inet') //inet4, tcp4, udp4, unix, all
    psutil.net_if_addrs()

    for proc in psutil.process_iter(['pid', 'name', 'username']):
      print(proc.info)

p = psutil.Process()
with p.oneshot():
    print(f"1. {p.name()}")  # execute internal routine once collecting multiple info
    print(f"2. {p.cpu_times()}")  # return cached value
    print(f"3. {p.cpu_percent()}")  # return cached value
    print(f"4. {p.create_time()}")  # return cached value
    print(f"5. {p.ppid()}")  # return cached value
    print(f"6. {p.status()}")  # return cached value
    print(f"7. {p.memory_full_info()})
    print(f"8. {p.memory_info()})

'''

 