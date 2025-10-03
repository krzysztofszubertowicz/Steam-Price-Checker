import requests
import streamlit as st


@st.cache_data
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



