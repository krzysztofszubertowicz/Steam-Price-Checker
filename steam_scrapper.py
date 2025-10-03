import requests


dataset = {}
def search_game(game_name):

    link_steam = f"https://store.steampowered.com/api/storesearch/?term={game_name}&cc=pl"

    r = requests.get(link_steam)

    data = r.json()
    for item in data["items"]:
        dataset[item["name"]] = item["price"]["final"]/100
        
    return dataset



