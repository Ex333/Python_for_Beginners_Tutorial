
from datetime import datetime
orders = {}
time = datetime.now()
time = time.strftime("%d.%m.%Y--%H:%M:%S")

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

def order_food():
      name = input("Podaj swoje imie:   ")
      order = input("Podaj swoje zamówienie:   ")
      quantity = input("Podaj ilość:   ")

      orders[name] = {
            "order": order,
            "quantity": quantity,
            "datetime": time
      }


def show_orders():
    for name, order in orders.items():
        print(f"User: {name}")
        print(f"Order: {order['order']}")
        print(f"Quantity: {order['quantity']}")
        print(f"Ordered at:  {order['datetime']}")
        print("-" * 20)




while True:
    show_menu()
    choice = input("Podaj swów wybór")

    if choice.lower() == "1" or choice.lower() == "order food":
          order_food()
    elif choice.lower() == "2" or choice.lower() == "show orders":
          show_orders()
          input("Press Enter to continue!")
    else:
          print("I D K ")
          break
