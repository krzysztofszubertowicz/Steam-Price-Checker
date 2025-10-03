import tkinter as tk
import steam_scrapper as scrapper


def create_window(title, size):
    window = tk.Tk()
    window.title(title)
    window.geometry(size)
    return window

def handle_search_click():
    game_name = entry.get()
    scrapper.search_game(game_name)
    print(scrapper.dataset)


window = create_window("Steam_Scrapper", "320x200")
entry = tk.Entry(window)
entry.pack(pady = 10)
button = tk.Button(window, text="Search", command= handle_search_click)
button.pack()

window.mainloop()


