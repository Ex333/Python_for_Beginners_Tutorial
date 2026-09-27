servers = [
    "web01",
    "db01",
    "web02",
    "backup01",
    "web03",
    "db02",
    "monitoring01"
]

for index, server in enumerate(servers):
    if server.startswith("web"):
        print(index, server)

print("*" * 8)

for server in servers:
    if "01" in server:
        print(server)


print("*" * 8)

counter_db = 0
counter_web = 0
another_counter = 0 

for server in servers:
    if "web" in server:
        counter_web +=1
    elif "db" in server:
        counter_db +=1
    else:
        another_counter +=1
print(f"Web serverów mamy: {counter_web} \n Db Serverów mamy: {counter_db} \n Innych serverów mamy: {another_counter}")

print("*" * 8)


web_servers = []

for server in servers:
    if server.startswith("web"):
        web_servers.append(server)

print(web_servers)

print("**" * 8)

server_names = []

for server in servers:
    server_names.append(server.upper())

print(server_names)

print("**" * 8)

for index, server in enumerate(servers, start=1):
    if server.startswith('web'):
        print(f'{index}, {server}')
        