from datetime import datetime

time = datetime.now()


name = input("Podaj swoje Imię:")

print(f"Użytkowniku {name}  jest godzina: {time.strftime("%H:%M:%S")}")

hour = int(time.strftime("%H"))


if 5 <= hour < 12:
    print("🌅 Dzień dobry! Jest poranek.")
elif 12 <= hour < 18:
    print("☀️ Jest popołudnie.")
elif 18 <= hour < 22:
    print("🌆 Jest wieczór.")
else:
    print("🌙 Jest noc.")

print(f"Aktualna godzina: {time.strftime('%H:%M:%S')}")