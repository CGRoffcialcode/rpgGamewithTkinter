import random
import tkinter as tk
from tkinter import messagebox
import Libaries as lib
from Libaries import player_enemy_logic as ec_logic, enemy_character as ec, continue_game as cs, powerup



def start_game(selected_character):
    global root, text_area, attack_button, player, enemies_defeated
    root = tk.Tk()
    root.title("Fantasy RPG Battle")
    root.configure(bg="Black")

    tk.Label(root, text="Fantasy RPG Battle", font=("Arial", 16), fg="gold", bg="black").pack()
    text_area = tk.Text(root, height=20, width=50, bg="darkgrey", fg="white")
    text_area.pack()
    attack_button = tk.Button(root, text="Attack", bg="red", fg="white")
    attack_button.pack()

    player = ec.choose_character() [selected_character]
    enemies_defeated = 0

    ec_logic.next_battle()

    root.mainloop()

def return_enemies_defeated():
    return enemies_defeated


if __name__ == "__main__":
    ec.character_selection()

