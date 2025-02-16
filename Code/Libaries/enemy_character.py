import random
import tkinter as tk
from tkinter import messagebox
import main as m
import Libaries as lib
from Libaries import player_enemy_logic as ec_logic, enemy_character as ec, continue_game as cs, powerup
def choose_character():
    return {
        "Warrior": {"HP": 100, "Attack": 19, "Defense": 17, "SpecialPowerAttack": "Strength", "SpecialPowerDefense": "Strength", "SpecialPowerDefensePoint": 5, "SpecialPowerAttackPoint": 5 },
        "Mage": {"HP": 70, "Attack": 20, "Defense": 5, "SpecialPowerAttack": "Magic", "SpecialPowerDefense": "Magic", "SpecialPowerDefensePoint": 10, "SpecialPowerAttackPoint": 6},
        "Rouge": {"HP": 80, "Attack": 18, "Defense": 8, "SpecialPowerAttack": "Strength", "SpecialPowerDefense": "Strength", "SpecialPowerDefensePoint": 3, "SpecialPowerAttackPoint": 3},
        "Fire Mage": {"HP": 80, "Attack": 20, "Defense": 5, "SpecialPowerAttack": "Fire", "SpecialPowerDefense": "Fire", "SpecialPowerDefensePoint": 7,"SpecialPowerAttackPoint": 10}
    }

def encounter_enemy():
    return random.choice([
        {"name": "Goblin", "HP": 70, "Attack": 10, "Defense": 7, "SpecialPowerAttack": "Strength", "SpecialPowerDefense": "Strength", "SpecialPowerDefensePoint": 3, "SpecialPowerAttackPoint": 5},
        {"name": "Orc", "HP": 80, "Attack": 12, "Defense": 8,  "SpecialPowerAttack": "Magic", "SpecialPowerDefense": "Magic", "SpecialPowerDefensePoint": 5, "SpecialPowerAttackPoint": 5},
        {"name": "Dragon", "HP": 100, "Attack": 28, "Defense": 10, "SpecialPowerAttack": "Fire", "SpecialPowerDefense": "Fire", "SpecialPowerDefensePoint": 6, "SpecialPowerAttackPoint": 10},
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