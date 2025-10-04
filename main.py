import steam_scrapper as scrap
import ui 
import export_data
import streamlit as st
import pandas as pd


game_name = st.text_input("Enter the name of the game you want to search for:")
if game_name:
    result = scrap.search_game(game_name)
    ui.show_results(result)
    df = pd.DataFrame(result)
    st.dataframe(df)
    export = df.to_csv()
    ui.show_export_button(export)

