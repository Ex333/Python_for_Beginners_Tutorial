from art import text2art


print(text2art("ORDER YOUR FOOD"))


def show_menu():
    print("==============================")
    print("          MAIN MENU")
    print("==============================")
    print("1. New order")
    print("2. Show orders")
    print("3. Calculate total")
    print("4. Send confirmation")
    print("0. Exit")
    print("==============================")


show_menu()