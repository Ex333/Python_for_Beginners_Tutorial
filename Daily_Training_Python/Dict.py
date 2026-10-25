servers = {
    "server1": "online",
    "server2": "offline",
    "server3": "offline",
    "server4": "online"
}

nowy_status = "maintenance"
counter = 0

for nazwa, status in servers.items():
    if status.lower() == "offline":
        servers[nazwa] = nowy_status
        counter +=1
    else:
        print(f"reszta serverow jest ok...")


print(f"zmieniono status {counter} serverów na {nowy_status}")
print(servers)
