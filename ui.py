import steam_scrapper as scrapper
import streamlit as st
def show_results(result):
    st.write("Search results:")
    for item in result:
        st.write(item["name"],item["price"],"zł")
        st.image(item["tiny_img"])
        with st.expander("Show more details..."):
            st.markdown(scrapper.get_game_details(item["id"]),unsafe_allow_html=True)

def show_export_button(export):
    st.download_button(data=export,mime="text/csv",label="Download CSV",file_name="csv_export")