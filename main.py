from Character import Character
# player values
player_name = None
player = None
def battle():
    test_goblin = Character(5, 8, 2, attack=10, character_class="Enemy", defense=4)
    
    while test_goblin.health > 0 or player.health > 0:
        # add maybe some logic here to choose what attack you want to do?
        # and have the goblin pick a random move out of 4 moves to attack?
        # maybe add crit chance too
        
        # both player and goblin attacks each other
        player.attack_user(test_goblin)
        test_goblin.attack_user(player)
        print(player.view_stats)
        
        if player.health <= 0:
            print("Player has lost!")
            break
        elif test_goblin.health <= 0:
            print("Goblin has lost!")
            player.gain_xp(test_goblin.level * 2)
            break
        
        ...
    game_over()



def game_over():
    print("Game is over!")
    play_game =  input("Play again? (y/n): ")
    if play_game.lower() == "y" or play_game.lower() == "yes":
        main()
        print("")
        print("")


    

def main():
    welcome_to_game()
    ...

def create_player():
    global player_name, player
    player = Character()
    print('Create your character')
    print("")
    
    # adjust players name
    check_player_name = input(f"Is your name {player_name}? (y/n): ")
    
    if check_player_name.lower() == "y" or check_player_name.lower() == "yes":
        ...
    elif check_player_name.lower() == "n" or check_player_name.lower() == "no":
        player_name = input("Enter Name: ")
        
        
    default_settings = input(f"Would you like to start with default settings? (y/n): ")
    choose_class = input("Choose your class, [Warrior or Mage]: ")
    if default_settings.lower() == 'y' or default_settings.lower() == "yes":
        player.strength = 12
        player.dexterity = 12
        player.health = 50
        player.attack = 20
        player.character_class = choose_class
        player.defense = 10
        print(player.view_stats)
    else:
        #continue asking their stats?
        ...
        
    print('')
    print("lets start the adventure!")
    print('')
    battle()




def welcome_to_game():
    global player_name
    print("################################")
    print("Welcome to Legends of Valor")
    print("This is a turn-based RPG adventure!")
    print("Defeat enemies, gain XP, and level up your hero.")   
    print("What is your hero's name?")
    player_name = input("> ") 
    print("Are you ready to begin your quest, brave", player_name + "?")
    print("Press enter to start game.")
    print("################################")
    create_player()


if __name__ == "__main__":
    main()