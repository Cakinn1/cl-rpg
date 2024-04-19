import pytest
from project import welcome_to_game, open_inventory, create_player, get_valid_class_choice, Player, menu  
from unittest.mock import patch  

@patch('builtins.input', return_value="TestHero")  # Mock input to be "TestHero"
def test_welcome_to_game(mock_input):
    player_name = welcome_to_game()
    assert player_name == "TestHero"
    
@patch('builtins.input', return_value="TestHero")
def test_invalid_welcome_to_game(mock_input):
    player_name = welcome_to_game()
    assert player_name != "TestHero1"   

@patch("builtins.input", return_value="0")
def test_get_valid_class_choice(mock_input):
    choice = get_valid_class_choice()
    assert choice == "0"
    

