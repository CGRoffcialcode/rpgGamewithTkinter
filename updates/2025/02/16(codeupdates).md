# LATEST UPDATE



## List


## Continue_game.py 
    def continue_game()

##### Responsible for looping through the enemies; enabling fight scenes. Reason for not in player_enemy_logic is because this is a early game loop

###### Changes: changed import from (WORKAROUNDcontinute_game as E) to (from Libaries import utils as E)

## enemy_character.py
    def character_selection
    def encounter_enemy
    def choose_character

##### Stores the data for the enemies, and players and their features. Also contains character selection because the python file has the data for the function

###### Changes: 
    Added (to def encounterEnemy() and def choose_character()):
    SpecialPowerAttack
    SpecialPowerDefense
    SpecialPowerDefensePoint
    SpecialPowerAttackPoint




# player_enemy_logic.py
    def start_final_battle()
    def next_battle()
    def battle(player, enemy, text_area, attack_button)
    def enemy_attack(player, enemy, text_area)
    def attack(player, enemy, text_area)

##### Is responsible for most the battle logic, and main game logic as it is a rpg.

###### Changes: 
    Added:
     from Libaries import player_enemy_logic as ec_logic, enemy_character as ec, continue_game as cs, powerup as pw
    
     if player["SpecialPowerAttack"] == enemy["SpecialPowerDefense"]:
     damage_to_enemy += max(0, player["SpecialPowerAttackPoint"] - enemy["SpecialPowerDefensePoint"])

     text_area.insert(tk.END, f"You hit {damage_to_enemy} damage to {enemy['name']}. ({max(0, enemy['HP'])} HP left) \n")

     if player["SpecialPowerAttack"] == enemy["SpecialPowerDefense"]:
     damage_to_player += max(0, enemy["SpecialPowerAttackPoint"] - player["SpecialPowerDefensePoint"])

     text_area insert(tk.END, f"{enemy['name']} deals {damage_to_player} damage to you. ({max(0, player['HP'])} HP left) \n")
     m.root.after(1000, pw.create_power_up(player, enemy, text_area))

    Removed:
     text_area.insert(tk.END, f"{enemy['name']} deals {damage_to_player} damage to you. ({player['HP']} Hp left) \n")

     text_area.insert(tk.END, f"You hit {damage_to_enemy} damage to {enemy['name']}. ({enemy['HP']} HP left) \n")

     from Libaries import player_enemy_logic as ec_logic, enemy_character as ec, continue_game as cs, powerup
     
        





# powerup.py
    def create_power_up()
    def power_up

##### A improved version of a power up, (used in functions now).

##### Changes:
    Added:
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
    


### WORKAROUNDcontinue_game.py
    (Deleted)


##### A workaround for a circulation error, and helps Continue_game.py access the variable enemies_defeated.py.

# Utils.py
   def returnE()

##### A workaround for a circulation error, and helps Continue_game.py access the variable enemies_defeated.py.

###### Changes:
     import main as m

     def returnE ():
       return m.return_enemies_defeated()


# main.py
    def return_enemies_defeated()
    def start_game(selected_character)
  
##### The main file for the game running, and is the python file run to make the game work. Also contains return_enemies_defeated()