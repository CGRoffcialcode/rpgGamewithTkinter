# LATEST UPDATE



## List


##  Continue_game.py 
    def continue_game()

##### Responsible for looping through the enemies; enabling fight scenes. Reason for not in player_enemy_logic is because this is a early game loop

## enemy_character.py
    def character_selection
    def encounter_enemy
    def choose_character

##### Stores the data for the enemies, and players and their features. Also contains character selection because the python file has the data for the function


# player_enemy_logic.py
    def start_final_battle()
    def next_battle()
    def battle(player, enemy, text_area, attack_button)
    def enemy_attack(player, enemy, text_area)
    def attack(player, enemy, text_area)

##### Is responsible for most the battle logic, and main game logic as it is a rpg.



# powerup.py
    def power_up(player)

##### A basic example of a power up, (not used inside main.py, or any other functions) and wil be improved on.


# WORKAROUNDcontinue_game.py
    def returnE ()

##### A workaround for a circulation error, and helps Continue_game.py access the variable enemies_defeated.py.


# main.py
    def return_enemies_defeated()
    def start_game(selected_character)
  
##### The main file for the game running, and is the python file run to make the game work. Also contains return_enemies_defeated()