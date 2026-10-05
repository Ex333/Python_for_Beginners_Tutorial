servers = {
    "server01": {
        "ip": "192.168.1.10",
        "os": "Linux",
        "ram": "32GB"
    },
    "server02": {
        "ip": "192.168.1.20",
        "os": "Linux",
        "ram": "64GB"
    },
    "server03": {
        "ip": "10.0.0.5",
        "os": "Windows",
        "ram": "16GB"
    }
}

for key, value in servers.items():
    print(f"{key}    IP to {value['ip']} dalej mamy OSystem ---> {value['os']} i na koncu RAAAMECZKI RAMMMECZKI!: {value['ram']}")
    print(value.get("ram", "RAM not specified"))

for server in servers.keys():
    print(server)