import random
import tkinter as tk
from tkinter import messagebox
import main as m
import Libaries as lib
from Libaries import player_enemy_logic, enemy_character, continue_game, powerup

def power_up(player):
    player["HP"] += 20
    player["Attack"] += 5