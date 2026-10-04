server = {}

while True:

    print("\n=========================")
    print("      SERVER MANAGER")
    print("=========================")
    print("1. Add server")
    print("2. Show servers")
    print("3. Exit")
    print("=========================")

    choice = input("Choose: ")

    # =========================
    # ADD SERVER
    # =========================
    if choice == "1":

        # SERVER NAME
        while True:
            name = input("Server name: ")

            if not name:
                print("Name cannot be empty!")

            elif len(name) > 15:
                print("Name cannot be longer than 15 characters!")

            else:
                break

        # IP ADDRESS
        while True:
            ip_address = input("IP address: ")

            parts = ip_address.split(".")

            if len(parts) != 4:
                print("Invalid IP address!")

            else:
                valid_ip = True

                for part in parts:

                    if not part.isdigit():
                        valid_ip = False
                        break

                    if int(part) < 0 or int(part) > 255:
                        valid_ip = False
                        break

                if valid_ip:
                    break

                print("Invalid IP address!")

        # OPERATING SYSTEM
        while True:
            o_system = input("Operating system (Linux/Windows): ").lower()

            if o_system == "linux":
                o_system = "Linux"
                break

            elif o_system == "windows":
                o_system = "Windows"
                break

            else:
                print("Choose only Linux or Windows!")

        # SSH PORT
        while True:
            ssh_port = input("SSH port: ")

            if not ssh_port.isdigit():
                print("Port must be a number!")

            else:
                ssh_port = int(ssh_port)

                if 1 <= ssh_port <= 65535:
                    break

                print("Port must be between 1 and 65535!")

        # SAVE SERVER
        server[name] = {
            "ip": ip_address,
            "os": o_system,
            "ssh_port": ssh_port
        }

        print(f"\nServer '{name}' added successfully!")

    # =========================
    # SHOW SERVERS
    # =========================
    elif choice == "2":

        if not server:
            print("\nNo servers found.")

        else:
            print("\n========== SERVERS ==========")

            for name, data in server.items():

                print(f"\nServer: {name}")
                print(f"  IP:       {data['ip']}")
                print(f"  OS:       {data['os']}")
                print(f"  SSH port: {data['ssh_port']}")

            print("\n=============================")

    # =========================
    # EXIT
    # =========================
    elif choice == "3":

        print("Goodbye!")
        break

    else:
        print("Invalid choice!")