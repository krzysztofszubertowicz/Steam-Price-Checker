import steam_scrapper as scrapper
import streamlit as st

game_name = st.text_input("Enter the name of the game you want to search for:")
if game_name:
    st.write("Search results:")
    result = scrapper.search_game(game_name)
    for item in result:
        st.write(item["name"],item["price"])