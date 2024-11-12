## Except Block

def safe_input():
    """Prompt user for input and handle potential value errors."""
    try:
        number = int(input("Enter a number: "))
        print(f"You entered: {number}")
    except ValueError:
        print("Error: Please enter a valid integer.")

safe_input()