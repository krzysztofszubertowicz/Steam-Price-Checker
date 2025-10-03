import requests


dataset = {}
def search_game(game_name):

    link_steam = f"https://store.steampowered.com/api/storesearch/?term={game_name}&cc=pl"

    r = requests.get(link_steam)

    data = r.json()
    if data and data.get("items"):
        for item in data["items"]:
            if item.get("price"):
                game_name = item.get("name")
                price = item["price"]["final"]/100
                dataset[game_name] = price
    return dataset



