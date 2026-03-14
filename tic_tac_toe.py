#!/usr/bin/env python3
"""
GAME Tic Tac Toe 2 Player Game - GUI Version
A graphical user interface implementation of the classic Tic Tac Toe game for two players.
"""

import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Game state
        self.board = [' '] * 9
        self.current_player = 'X'
        self.game_over = False
        
        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Title label
        self.title_label = tk.Label(self.root, text="Tic Tac Toe", font=('Arial', 24, 'bold'))
        self.title_label.pack(pady=20)
        
        # Status label
        self.status_label = tk.Label(self.root, text="Player X's turn", font=('Arial', 14))
        self.status_label.pack(pady=10)
        
        # Game board frame
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(pady=20)
        
        # Create 3x3 grid of buttons
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.board_frame,
                    text=' ',
                    font=('Arial', 20, 'bold'),
                    width=6,
                    height=3,
                    command=lambda row=i, col=j: self.make_move(row * 3 + col)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)
        
        # Control buttons frame
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(pady=20)
        
        # Restart button
        self.restart_button = tk.Button(
            self.control_frame,
            text="New Game",
            font=('Arial', 12),
            command=self.restart_game
        )
        self.restart_button.pack(side=tk.LEFT, padx=10)
        
        # Quit button
        self.quit_button = tk.Button(
            self.control_frame,
            text="Quit",
            font=('Arial', 12),
            command=self.root.quit
        )
        self.quit_button.pack(side=tk.LEFT, padx=10)
    
    def make_move(self, position):
        if self.game_over or self.board[position] != ' ':
            return
        
        # Make the move
        self.board[position] = self.current_player
        self.buttons[position].config(text=self.current_player)
        
        # Check for winner
        winner = self.check_winner()
        if winner:
            self.status_label.config(text=f"Player {winner} wins!")
            self.game_over = True
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            return
        
        # Check for tie
        if self.is_board_full():
            self.status_label.config(text="It's a tie!")
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a tie!")
            return
        
        # Switch players
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.status_label.config(text=f"Player {self.current_player}'s turn")
    
    def check_winner(self):
        """Check if there's a winner and return the winning symbol or None."""
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                return self.board[i]
        
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return self.board[i]
        
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return self.board[2]
        
        return None
    
    def is_board_full(self):
        """Check if the board is full (tie game)."""
        return ' ' not in self.board
    
    def restart_game(self):
        """Reset the game to start over."""
        self.board = [' '] * 9
        self.current_player = 'X'
        self.game_over = False
        
        for button in self.buttons:
            button.config(text=' ')
        
        self.status_label.config(text="Player X's turn")

def main():
    """Main function to start the GUI application."""
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()