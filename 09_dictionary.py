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


# lecimy po wszystkich serverach i pokazujemy co tam siedzi
for key, value in servers.items():
    print(
        f"{key} IP to {value['ip']} "
        f"dalej mamy OSystem ---> {value['os']} "
        f"i na koncu RAAAMECZKI RAMMMECZKI!: {value['ram']}"
    )

    # sprawdzamy czy ram w ogole jest bo python lubi sie zesrac jak nie ma
    print(value.get("ram", "RAM not specified"))


# Show all keys -> Server01, Server02 and Server03
for server in servers.keys():
    print(server)


# teraz pokazujemy wszystkie wartosci czyli cale dane serverow
for server in servers.values():
    print(server)


# user wybiera sobie server ktory chce zmienic
server = input("Which server do you want to update? ")

# tutaj user wpisuje ile chce ramu, bo czemu nie
new_ram = input("Enter new RAM: ")


# update servera czyli zmieniamy mu ram
servers[server].update({
    "ram": new_ram
})


# tutaj dla testu wywalamy ram z server01 xD
servers["server01"].pop("ram")


# jak nie ma statusu to mu go dodamy
servers["server01"].setdefault("status", "online")


# zobaczmy co sie teraz odjebalo ze slownikiem
print(servers)


# pokazujemy finalnie wszystkie servery
for key, value in servers.items():
    print(
        f"SERVER: {key}\n"
        f"IP: {value.get('ip', 'IP not specified')}\n"
        f"OS: {value.get('os', 'OS not specified')}\n"
        f"RAM: {value.get('ram', 'RAM not specified')}\n"
        f"STATUS: {value.get('status', 'STATUS not specified')}"
    )
    print("-------------------------")