import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg='black')  # Set the background color to black
        self.current_player = 'X'

        self.buttons = [[None, None, None] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text="", width=10, height=2, font=('Helvetica', 36, 'bold'), bg='black')
                self.buttons[i][j].grid(row=i, column=j)
                self.buttons[i][j].config(command=lambda row=i, col=j: self.make_move(row, col))

    def make_move(self, row, col):
        if self.buttons[row][col]['text'] == "" and not self.check_winner():
            self.buttons[row][col]['text'] = self.current_player
            self.buttons[row][col]['state'] = 'disabled'
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != "":
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != "":
                return True

        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True

        return False

    def is_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == "":
                    return False
        return True

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""
                self.buttons[i][j]['state'] = 'active'
        self.current_player = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
