import requests
import streamlit as st



def search_game(game_name):
    dataset = []

    link_steam = f"https://store.steampowered.com/api/storesearch/?term={game_name}&cc=pl"

    r = requests.get(link_steam)

    data = r.json()
    if data and data.get("items"):
        for item in data["items"]:
            if item.get("price"):
                game_data = {
                    "name": item.get("name"),
                    "price": item["price"]["final"] / 100,
                    "id": item.get("id"),
                    "tiny_img": item.get("tiny_image")
                }
                dataset.append(game_data)
    return dataset



def get_game_details(gameid):
    url = f"https://store.steampowered.com/api/appdetails?appids={gameid}"

    r = requests.get(url)

    data = r.json()

    game_id_str = str(gameid)

    if data and data.get(game_id_str) and data[game_id_str].get("success"):
        
        game_data = data[game_id_str]["data"]

        description = game_data.get("detailed_description")

        return description

