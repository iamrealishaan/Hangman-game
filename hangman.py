import random

# Define a list of words to choose from
words = ["apple", "banana", "cherry", "orange", "pear"]

# Function to choose a random word from the list
def choose_word(words):
    return random.choice(words)

# Function to initialize the game board
def init_board(word):
    return ["_" for letter in word]

# Function to display the game board
def display_board(board):
    print(" ".join(board))

# Function to get the user's guess
def get_guess():
    return input("Guess a letter: ")

# Function to update the game board based on the user's guess
def update_board(word, board, guess):
    for i, letter in enumerate(word):
        if letter == guess:
            board[i] = letter

# Function to check if the user has won the game
def check_win(board):
    return "_" not in board

# Main game loop
word = choose_word(words)
board = init_board(word)
display_board(board)

guesses = []
max_guesses = 6

while len(guesses) < max_guesses:
    guess = get_guess()
    
    # Check if the guess has already been made
    if guess in guesses:
        print("You already guessed that letter!")
        continue
    
    # Add the guess to the list of guesses
    guesses.append(guess)
    
    # Update the game board based on the guess
    if guess in word:
        update_board(word, board, guess)
        display_board(board)
        if check_win(board):
            print("You win!")
            break
    else:
        print("Sorry, that letter is not in the word.")
    
    # Display the number of guesses remaining
    guesses_remaining = max_guesses - len(guesses)
    print(f"You have {guesses_remaining} guesses remaining.")
    
# If the user has used all their guesses and not solved the word, they lose
if not check_win(board):
    print(f"Sorry, you lose! The word was {word}.")
