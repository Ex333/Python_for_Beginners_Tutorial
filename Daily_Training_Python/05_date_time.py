from datetime import datetime


time = datetime.now()

print(f"Aktualna godzina: {time.strftime('%H:%M:%S')}")

hour = int(time.strftime('%H'))


if 5 <= hour < 9:
    print("🌅 Jest rano!")

elif 9 <= hour < 12:
    print("☀️ Jest przed południem!")

elif 12 <= hour < 18:
    print("🌞 Jest popołudnie!")

elif 18 <= hour < 22:
    print("🌆 Jest wieczór!")

else:
    print("🌙 Jest noc!")
