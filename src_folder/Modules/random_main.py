## Random Module

import random

def roll_dice():
    """Simulate rolling a 6-sided dice using the random module."""
    return random.randint(1, 6)

dice_roll = roll_dice()
print(f"You rolled a {dice_roll}")