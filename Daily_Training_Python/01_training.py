servers = ["web-01", "web-02", "db-01", "backup-01"]

cpus = [45, 91, 72, 20]

rams = [60, 82, 95, 30]

statuses = ["online", "online", "online", "offline"]

# for index,  server in enumerate(servers, start=1):
#     print(index, server)

for index, server in enumerate(servers, start=1):
   print(f"{index}  --  SERVER: {server} -- ma CPU: {cpus[index - 1]}% oraz RAM  {rams[index - 1]}% oraz status to: {statuses[index - 1]}")


lista1 = [1,2,3,4,5,6,7,88,2]
lista2 =lista1[:]

print(lista2)

lista2.append(15)

print("*"*8)

print(lista1)
print(lista2)

print(id(lista1))
print(id(lista2))


for server, cpu, ram, status in zip(servers,cpus, rams, statuses):
   print(server, cpu, ram, status)