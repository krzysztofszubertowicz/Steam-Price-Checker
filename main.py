import requests

#enter the name of the game you wanna search
game_name = input("Podaj nazwe gry: ")


link_steam = f"https://store.steampowered.com/api/storesearch/?term={game_name}&cc=pl"

r = requests.get(link_steam)

data = r.json()

for item in data["items"]:
    print("nazwa: ", item["name"])
    print("Cena PLN: ", item["price"]["final"]/100)