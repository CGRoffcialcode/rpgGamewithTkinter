"""
    the code below and above is in development, and will be improved in the future
"""
import random
import tkinter as tk
from tkinter import messagebox
import main as m
import Libaries as lib
from Libaries import player_enemy_logic, enemy_character, continue_game, powerup

def create_power_up(player, enemy, text_area):
    power_up_type = enemy["SpecialPowerAttack"]
    power_up_point_HP = player["SpecialPowerAttackPoint"] - enemy["SpecialPowerDefensePoint"]
    power_up_point_Attack_Defense = 0

    if enemy["HP"] <= 80 and enemy["Defense"] <= 80:
        power_up_point_HP += enemy["HP"] + enemy["Defense"] + player["Attack"] + player["Defense"] - player["SpecialPowerAttackPoint"]
    elif enemy["HP"] >= 90 and enemy["Defense"] >= 90:
        power_up_point_HP += enemy["HP"] + enemy["Defense"] + player["Attack"] + player["Defense"]
        power_up_point_Attack_Defense += enemy["Attack"] + enemy["Defense"] + player["Attack"] + player["Defense"] - player["SpecialPowerAttackPoint"]

    power_up(power_up_type, power_up_point_HP, power_up_point_Attack_Defense, player, enemy, text_area)
    
    
def power_up(pw_type, pw_point_HP, pw_point_Attack_Defense, player, enemy, text_area):
    text_area.insert(tk.END, f"Discovered some loot! \nFound a {pw_type} power-up! \n")
    text_area.insert(tk.END, f"Your HP has increased by {pw_point_HP} \n")
    player["HP"] += pw_point_HP

    if enemy["HP"] > 100 or enemy["Attack"] > 20:
        text_area.insert(tk.END, f"Your Attack and Defense have increased by {pw_point_Attack_Defense} \n")
        player["Attack"] += pw_point_Attack_Defense
        player["Defense"] += pw_point_Attack_Defense
    else:
        text_area.insert(tk.END, f"Try fighting stronger enemies to increase your Attack and Defense! \n")
    