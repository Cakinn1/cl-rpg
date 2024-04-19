from Player import Player
from Battle import Battle
from Enemy import Enemy


player = Player()
enemy_1 = Enemy(attack=10, health=100, mana=40, defense=5, level=5, name="goblin")
battle = Battle(player, enemy_1)

def main():
    player.name = welcome_to_game()
    create_character = create_player(player)
    print(create_character)



def welcome_to_game():
    print("")
    print("##################################################################################")
    print("Welcome to Legends of Valor")
    print("This is a turn-based RPG adventure with resource-management survival elements!")
    print("Defeat enemies, gain XP, and level up your hero.")   
    print("##################################################################################")
    
    while True:
        print("")
        player_name = input("What is your hero's name? >  ") 
        if player_name:
            break
        else: 
            print("You must enter a name!")
        
    print(f"\nAre you ready to begin your quest, brave {player_name}?")
    input("Press enter to start game: ") 
    return player_name


def open_inventory ():
    print("")
    print(f"Health: {player.health}")
    print(f"Mana: {player.mana}")
    
    print("")
    if len(player.inventory) >= 1:
        for i in range(len(player.inventory)):
            print(f"[{i}]: {player.inventory[i]}")
            
        while True:
            try:
                index_value = int(input("Enter the index value to use potion: "))
                if index_value <= len(player.inventory):
                    player.use_potion(index_value)
                    print("")
                    break
                else:
                    print()
                    print(f"Index range must be between 0 and {len(player.inventory) - 1}")
                    print()
                    continue
            except ValueError:
                print("Must be a number")   
    else:
        print("No items in inventory")
        print("")
    menu()
    
    
def create_player(player):
    print("")
    check_player_name = input(f"Is your name {player.name}? (y/n): ")
    
    if check_player_name.lower() == "y" or check_player_name.lower() == "yes":
        print("")
        print(f"Welcome {player.name}")
        print("")
    elif check_player_name.lower() == "n" or check_player_name.lower() == "no":
        print("")
        player.name = input("Enter Name: ")
        
        
    class_choice = get_valid_class_choice()    
    if class_choice == "0":
        player.character_class = "mage"
    elif class_choice == "1":
        player.character_class = "warrior"
    print("")
    player.add_starter_abilities()
    print(player.view_stat)
    print("")

    print("lets start the adventure!")
    print("")
    menu()

def get_valid_class_choice():
    while True:
        print("")
        print("#############")
        print("[0]: Mage")
        print("[1]: Warrior")
        print("#############")
        print("")
        choice = input("Choose your class, Enter: 0 or 1: ")
        if choice in ['0', '1']:
            return choice
        else:
            print("Invalid choice. Please enter 0 or 1.")
        
    
def menu():
    print("###############")
    print("[0]: battle")
    print("[1]: inventory")
    print("[2]: stats")
    print("###############")
    print("")
    while True:
        select = input("Selection: ")
        if select.isdigit() and 0 <= int(select) <= 2:  # Combined condition
            if int(select) == 0:
                     #  reset goblin health
                enemy_1.health = 100
                while True:
                    battle_result = battle.run_battle()
                    if battle_result:
                        break   
                    menu()
            elif int(select) == 1:   
                open_inventory()             
            elif int(select) == 2:  
               print(player.view_stat) 
               print("")
            menu()    
            break  
        else:
            print("Choose number between 0 and 2")
            


if __name__ == "__main__":
    main()