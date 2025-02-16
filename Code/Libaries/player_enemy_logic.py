import random
import tkinter as tk
from tkinter import messagebox
import main as m
import Libaries as lib
from Libaries import player_enemy_logic as ec_logic, enemy_character as ec, continue_game as cs, powerup as pw

def attack(player, enemy, text_area):
    damage_to_enemy = max(0, player["Attack"] - enemy["Defense"])
    if player["SpecialPowerAttack"] == enemy["SpecialPowerDefense"]:
        damage_to_enemy += max(0, player["SpecialPowerAttackPoint"] - enemy["SpecialPowerDefensePoint"])
    enemy["HP"] -= damage_to_enemy
    text_area.insert(tk.END, f"You hit {damage_to_enemy} damage to {enemy['name']}. ({max(0, enemy['HP'])} HP left) \n")
    return enemy["HP"] > 0 

def enemy_attack(player, enemy, text_area):
    damage_to_player = max(0, enemy["Attack"] - player["Defense"])
    if player["SpecialPowerAttack"] == enemy["SpecialPowerDefense"]:
        damage_to_player += max(0, enemy["SpecialPowerAttackPoint"] - player["SpecialPowerDefensePoint"])
    player["HP"] -= damage_to_player 
    text_area.insert(tk.END, f"{enemy['name']} deals {damage_to_player} damage to you. ({max(0, player['HP'])} HP left) \n")
    return player["HP"] > 0

def battle(player, enemy, text_area, attack_button):
    def player_turn():
        if attack(player, enemy, text_area):
            if not enemy_attack(player, enemy, text_area):
                messagebox.showinfo("Game Over", "You have been defeated. Game over!")
                m.root.quit()
            else: 
                attack_button.config(state=tk.NORMAL)
                attack_button.config(command=player_turn)
        else:   
            text_area.insert(tk.END, f"You have defeated {enemy['name']}! \n")
            m.root.after(1000, pw.create_power_up(player, enemy, text_area))
            attack_button.config(state=tk.DISABLED)
            m.root.after(1000, cs.continue_game)
                
            
                

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