import random
import tkinter as tk
from tkinter import messagebox
import main as m
import Libaries as lib
from Libaries import player_enemy_logic as ec_logic, enemy_character as ec, continue_game as cs, powerup
from Libaries import utils as E
def continue_game():
    global enemies_defeated
    enemies_defeated = E.returnE()
    enemies_defeated += 1
    if enemies_defeated < 3:
        ec_logic.next_battle()
    else:
        m.text_area.insert(tk.END, "A magical door appears, leading to the final battle! \n ")
        m.root.after(2000, lib.start_final_battle)
