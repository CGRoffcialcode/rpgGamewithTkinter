import random
import tkinter as tk
from tkinter import messagebox
import main as m
import Libaries as lib
from Libaries import player_enemy_logic as ec_logic, enemy_character as ec, continue_game as cs, powerup
def choose_character():
    return {
        "Warrior": {"HP": 100, "Attack": 15, "Defense": 10},
        "Mage": {"HP": 70, "Attack": 20, "Defense": 5},
        "Rouge": {"HP": 80, "Attack": 18, "Defense": 8}
    }

def encounter_enemy():
    return random.choice([
        {"name": "Goblin", "HP": 70, "Attack": 10, "Defense": 7},
        {"name": "Orc", "HP": 80, "Attack": 12, "Defense": 8},
        {"name": "Dragon", "HP": 120, "Attack": 20, "Defense": 12}
    ])


def character_selection():
    def select_character(character):
        selection_window.destroy()
        m.start_game(character)
    
    selection_window = tk.Tk()
    selection_window.title("Character Selection")
    selection_window.configure(bg="black")

    tk.Label(selection_window, text="Choose your character:", font=("Arial", 12), fg="gold", bg="black").pack()

    for char in choose_character().keys():
        tk.Button(selection_window, text=char, command=lambda c=char: select_character(c), bg="blue", fg="white").pack()
    
    selection_window.mainloop()