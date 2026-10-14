
"""
rps.py

Redistributed and modified with permission from the
EECS Department at The University of Michigan, Ann Arbor

Name: Cameron Bailey

CS 104: Project 2
FALL 2026

Description: This program lets two players play Rock, Paper,
Scissors for three rounds and announces the winner.
"""

# Constants
COURSE_NAME = "CS 104"
MAX_ROUNDS = 3

ROCK = "r"
PAPER = "p"
SCISSORS = "s"
DEFAULT_MOVE = ROCK

PLAYER_1 = 1
PLAYER_2 = 2
DEFAULT_NAME_1 = "Rocky"
DEFAULT_NAME_2 = "Creed"

DRAW = 0

ERROR_NAME = 1
ERROR_MOVE = 2

PLAY_RPS = 1
PLAY_RPSLS = 2
QUIT_CHOICE = 3


def rps():
    """Runs the whole game."""
    print_initial_header()

    p1_name = get_name(PLAYER_1)
    p2_name = get_name(PLAYER_2)

    choice = get_menu_choice()

    while choice != QUIT_CHOICE:
        winner = do_game(p1_name, p2_name, choice)
        if choice == PLAY_RPS:
            announce_winner(winner)
        choice = get_menu_choice()

    print_closer()


def get_name(player_number):
    """Gets a player's name."""
    name = input(f"Player {player_number}, enter your name: ")

    if name.strip() == "":
        print_error_message(ERROR_NAME)
        if player_number == PLAYER_1:
            return DEFAULT_NAME_1
        return DEFAULT_NAME_2

    return name


def get_menu_choice():
    """Gets a valid menu choice."""
    while True:
        print_menu()
        choice = input("Choice --> ")

        if choice in ("1", "2", "3"):
            return int(choice)

        print("Invalid menu choice")


def is_move_good(move):
    """Checks if a move is valid."""
    return move.lower() in (ROCK, PAPER, SCISSORS)


def get_move(player_name):
    """Gets a player's move."""
    move = input(f"{player_name}, enter your move: ")

    if not is_move_good(move):
        print_error_message(ERROR_MOVE)
        return DEFAULT_MOVE

    return move


def is_round_winner(move, opponent_move):
    """Checks if a player won the round."""
    move = move.lower()
    opponent_move = opponent_move.lower()

    return (
        (move == ROCK and opponent_move == SCISSORS)
        or (move == PAPER and opponent_move == ROCK)
        or (move == SCISSORS and opponent_move == PAPER)
    )


def announce_round_winner(winner_name):
    """Prints the winner of a round."""
    if winner_name == "":
        print("This round is a draw!")
    else:
        print(f"{winner_name} wins the round!")


def do_round(p1_name, p2_name):
    """Plays one round and returns the winner."""
    move1 = get_move(p1_name)
    move2 = get_move(p2_name)

    if move1.lower() == move2.lower():
        return DRAW

    if is_round_winner(move1, move2):
        return PLAYER_1

    return PLAYER_2


def announce_winner(winner_name):
    """Prints the winner of the game."""
    if winner_name == "":
        print("No winner!")
    else:
        print(f"Congratulations {winner_name}!")
        print(f"You won {COURSE_NAME} Rock, Paper, Scissors!")


def do_game(p1_name, p2_name, game_type):
    """Plays three rounds and returns the game winner."""
    if game_type == PLAY_RPSLS:
        print("Under Construction")
        return ""

    p1_score = 0
    p2_score = 0

    for round_number in range(MAX_ROUNDS):
        winner = do_round(p1_name, p2_name)

        if winner == PLAYER_1:
            p1_score += 1
            announce_round_winner(p1_name)
        elif winner == PLAYER_2:
            p2_score += 1
            announce_round_winner(p2_name)
        else:
            announce_round_winner("")

    if p1_score > p2_score:
        return p1_name
    elif p2_score > p1_score:
        return p2_name

    return ""




def print_initial_header():
    """Prints a pretty header to introduce the user to the game."""
    print("----------------------------------------")
    print("                CS 104")
    print("          Rock, Paper, Scissors")
    print("----------------------------------------")


def print_menu():
    """Prints the menu options (not the prompt)."""
    print()
    print("Menu Options")
    print("------------")
    print("1) Play rock, paper, scissors")
    print("2) Play rock, paper, scissors, lizard, spock")
    print("3) Quit")
    print()


def print_error_message(error_number):
    """Prints the error for ERROR_NAME or ERROR_MOVE."""
    if error_number == ERROR_NAME:
        print()
        print("ERROR: Illegal name given, using default")
        print()
    elif error_number == ERROR_MOVE:
        print()
        print("ERROR: Illegal move given, using default")
    else:
        print("This should never print!")


def print_closer():
    """Prints out the final greeting for the program."""
    print()
    print("----------------------------------------")
    print("           Thanks for playing")
    print("          Rock, Paper, Scissors!")
    print("----------------------------------------")
