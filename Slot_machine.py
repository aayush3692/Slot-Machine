import random

# Constants for the game
MAX_LINES = 3  # Maximum number of lines a player can bet on
MAX_BET = 100  # Maximum amount a player can bet per line
MIN_BET = 1    # Minimum amount a player can bet per line

ROWS = 3  # Number of rows in the slot machine
COLS = 3  # Number of columns in the slot machine

# Symbol configuration: the number of each symbol per reel
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 4
}

# Payout values for each symbol
symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    """
    Check the slot machine results to calculate the winnings.

    Args:
    - columns: List of lists representing the slot machine columns.
    - lines: Number of lines the player has bet on.
    - bet: Amount of money bet per line.
    - values: Dictionary of symbol values for calculating winnings.

    Returns:
    - Tuple containing total winnings and the winning lines.
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            # If all symbols in the line match, calculate the winnings
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    """
    Simulate a spin of the slot machine.

    Args:
    - rows: Number of rows in the slot machine.
    - cols: Number of columns in the slot machine.
    - symbols: Dictionary of symbols and their counts.

    Returns:
    - List of lists representing the random arrangement of symbols in each column.
    """
    all_symbols = []
    # Create a list of all symbols based on their counts
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
        
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)  # Select a random symbol
            current_symbols.remove(value)  # Remove the selected symbol to avoid repeats in the column
            column.append(value)
            
        columns.append(column)    
        
    return columns

def print_slot_machine(columns):
    """
    Print the current state of the slot machine.

    Args:
    - columns: List of lists representing the slot machine columns.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
                
        print()

def deposit():
    """
    Prompt the player to deposit money into the game.

    Returns:
    - The amount deposited by the player.
    """
    while True:
        try:
            amount = int(input("Enter amount: $"))
            if amount > 0:
                break
            else:
                print("Amount should be greater than zero")
                
        except ValueError:
            pass
        
    return amount

def get_numbers_of_lines():
    """
    Prompt the player to select the number of lines to bet on.

    Returns:
    - The number of lines selected by the player.
    """
    while True:
        lines = input("Enter number of lines(1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter within the range")
        else:
            print("Please enter a valid number!")
    return lines

def get_bet():
    """
    Prompt the player to enter the bet amount per line.

    Returns:
    - The bet amount entered by the player.
    """
    while True:
        bet = input("Enter the amount you want to bet on a line: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount should be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid number!")
    return bet

def spin(balance):
    """
    Handle a single spin of the slot machine.

    Args:
    - balance: Current balance of the player.

    Returns:
    - Net gain or loss from the spin.
    """
    lines = get_numbers_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"Your total balance is {balance}. Not enough Amount.")
        else:
            break    
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is {total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winning, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winning}.")
    print(f"You won on lines: ", *winning_lines)
    return winning - total_bet

def main():
    """
    Main function to run the slot machine game.
    """
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        answer = input("Press enter to play (q to quit). ")
        if answer == 'q':
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")

if __name__ == "__main__":
    main()
