import random
import tkinter as tk
from tkinter import messagebox
import main as m
import Libaries as lib
from Libaries import player_enemy_logic as ec_logic, enemy_character as ec, continue_game as cs, powerup
def attack(player, enemy, text_area):
    damage_to_enemy = max(0, player["Attack"] - enemy["Defense"])
    enemy["HP"] -= damage_to_enemy
    text_area.insert(tk.END, f"You hit {damage_to_enemy} damage to {enemy['name']}. ({enemy['HP']} HP left) \n")
    return enemy["HP"] > 0 


def enemy_attack(player, enemy, text_area):
    damage_to_player = max(0, enemy["Attack"] - player["Defense"])
    player["HP"] -= damage_to_player 
    text_area.insert(tk.END, f"{enemy['name']} deals {damage_to_player} damage to you. ({player['HP']} Hp left) \n")
    return player["HP"] > 0

def battle(player, enemy, text_area, attack_button):
    def player_turn():
        if attack(player, enemy, text_area):
            if not enemy_attack(player, enemy, text_area):
                messagebox.showinfo("Game Over", "You have been defeated. Game over!")
                m.root.quit()
            elif not attack(player, enemy, text_area):
                text_area.insert(tk.END, f"You have defeated {enemy['name']}! \n")
                attack_button.config(state=tk.DISABLED)
                m.root.after(1000, cs.continue_game)
            elif enemy_attack(player, enemy, text_area):
                attack_button.config(state=tk.NORMAL)
                attack_button.config(command=player_turn)

    attack_button.config(command=player_turn)


def next_battle():
    global current_enemy
    current_enemy = ec.encounter_enemy()
    m.text_area.insert(tk.END, f"A wild {current_enemy['name']} appears!  \n")
    m.attack_button.config(state=tk.NORMAL)
    battle(m.player, current_enemy, m.text_area, m.attack_button)


def start_final_battle():
    global final_boss
    current_enemy = final_boss()
    m.text_area.insert(tk.END, f"The final battle begins against the Dark Lord! \n")
    m.attack_button.config(state=tk.NORMAL)
    battle(m.player, current_enemy, m.text_area, m.attack_button)