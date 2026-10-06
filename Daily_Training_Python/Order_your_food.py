from art import text2art

orders = []

print(text2art("ORDER YOUR FOOD"))


def show_menu():
       print("="*40)
       print("          MAIN MENU")
       print("="*40)
       print("1. New order")
       print("2. Show orders")
       print("3. Calculate total")
       print("4. Send confirmation")
       print("0. Exit")
       print("="*40)


def new_order(name):
       order = input(f"{name}, gimme ur order: ")
       orders.append({
              "name": name,
              "order": order
       })


def show_orders():
       print()
       print("========== YOUR ORDERS ==========")

       if orders:
              for order in orders:
                     print(f"- {order['name']} -> {order['order']}")
       else:
              print("No orders yet.")

       print("="*30)
       input("Press ENTER to return to menu...")


while True:
       show_menu()
       choice = input("Choose your option: ")

       if choice == "1" or choice.lower() == "new order":

              name = input("What's your name? ")
              new_order(name)

       elif choice == "2" or choice.lower() == "show orders":
              show_orders()

       elif choice == "3" or choice.lower() == "calculate total":
              pass

       elif choice == "4" or choice.lower() == "send confirmation":
              pass

       elif choice == "0" or choice.lower() == "exit":
              print("Goodbye!")
              break

       else:
              print("Invalid value")