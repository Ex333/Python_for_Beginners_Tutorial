products = ["laptop", "mouse", "keyboard", "monitor", "mouse", "laptop"]

for i in range(len(products)):

    if products[i] == "laptop":
        print(f"LAPTOP is an expensive thing. It is located at position {i}: additionally, I can tell you that this is: {products[i]}")

    elif products[i] == "mouse":
        print(f"Mouse - accessory located at position {i}")

    elif products[i].lower() == "keyboard":
        print("This is a keyboard, buddy!")

    else:
        print("Error, nothing, null, zero, nada!")

for i in products:
    print(i)

laptop_counter = 0
mouse_counter = 0
keyboard_counter = 0
monitor_counter = 0

for i in products:

    if i == "laptop":
        laptop_counter += 1

    elif i == "mouse":
        mouse_counter = +1

    elif i == "keyboard":
        keyboard_counter += 1

    elif i == "monitor":
        monitor_counter += 1

print(f"Laptops: {laptop_counter}\n"
      f"Mice: {mouse_counter}\n"
      f"Keyboards: {keyboard_counter}\n"
      f"Monitors: {monitor_counter}")