# Tic Tac Toe 2 Player Game - GUI Version

A graphical user interface implementation of the classic Tic Tac Toe game for two players using Python's tkinter library.

## How to Run

1. Make sure you have Python 3 installed on your system (tkinter comes built-in with Python).
2. Run the game using:
   ```bash
   python tic_tac_toe.py
   ```

## Game Features

- **Graphical Interface**: Clean, modern GUI with large clickable buttons
- **Two-Player Gameplay**: Alternating turns between Player X and Player O
- **Win Detection**: Automatically detects wins in all directions (rows, columns, diagonals)
- **Tie Detection**: Recognizes when the board is full with no winner
- **Game Status**: Real-time display of whose turn it is
- **New Game Button**: Easily restart the game without closing the application
- **Game Over Messages**: Pop-up dialogs announce the winner or tie
- **Input Validation**: Prevents clicking on already occupied squares

## GUI Layout

- **Title**: "Tic Tac Toe" at the top
- **Status Bar**: Shows current player's turn or game result
- **Game Board**: 3x3 grid of large buttons for placing X's and O's
- **Control Buttons**: "New Game" to restart and "Quit" to exit

## Game Rules

- Player X always goes first
- Players take turns clicking on empty squares
- First player to get 3 marks in a row (horizontally, vertically, or diagonally) wins
- If all 9 squares are filled without a winner, it's a tie
- Click "New Game" to start over

## Requirements

- Python 3.x (tkinter is included by default)
- No external dependencies required

## Troubleshooting

If you encounter issues:
- Ensure Python 3 is installed and in your PATH
- On some systems, tkinter might need to be installed separately (e.g., `sudo apt-get install python3-tk` on Ubuntu)
- The game window should appear automatically when you run the script

Enjoy playing Tic Tac Toe! 🎮