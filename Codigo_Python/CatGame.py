import tkinter as tk

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

class Board:
    def __init__(self, player):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.current_player = player

    def place_symbol(self, x, y):
        self.board[x][y] = self.current_player.symbol
        print(self.board)

    def check_winner(self):
        # Comprobar filas
        for row in self.board:
            if all(cell == self.current_player.symbol for cell in row):
                return True
        # Comprobar columnas
        for col in range(3):
            if all(self.board[row][col] == self.current_player.symbol for row in range(3)):
                return True
        # Comprobar diagonales
        if all(self.board[i][i] == self.current_player.symbol for i in range(3)):
            return True
        if all(self.board[i][2 - i] == self.current_player.symbol for i in range(3)):
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

class ButtonManager:
    def update_button(self, button, symbol):
        button.config(text=symbol)

    def disable_button(self, button):
        button.config(state=tk.DISABLED)

    def enable_button(self, button):
        button.config(state=tk.NORMAL)

class Main(ButtonManager):
    def __init__(self):
        self.player1 = Player('X', 'Jugador X')
        self.player2 = Player('O', 'Jugador O')
        self.board = Board(self.player1)
        self.buttons = {}
        self.label = None
        self.buttonReset = None

    def update_board(self, button, x, y):
        self.board.place_symbol(x, y)
        self.update_button(button, self.board.current_player.symbol)
        self.disable_button(button)

        if self.board.check_winner():
            for button in self.buttons.values():
                self.disable_button(button)
            self.update_button(self.label, f'{self.board.current_player.symbol} Gana!')
            self.enable_button(self.buttonReset)
        elif self.board.is_board_full():
            self.update_button(self.label, '¡Empate!')
            self.enable_button(self.buttonReset)
        
        self.board.current_player = self.player2 if (self.board.current_player == self.player1)  else self.player1

    def reset(self):
        self.update_button(self.label, ' ')
        for button in self.buttons.values():
            self.enable_button(button)
            self.update_button(button, ' ')
        self.disable_button(self.buttonReset)
        self.board = Board(self.player1)
    
    def play(self):
        root = tk.Tk()
        root.title("Gato")

        self.label = tk.Label(root, text=" ", font=('Arial', 18))
        self.label.pack(pady=5, padx=5)

        mainFrame = tk.Frame(root)
        mainFrame.pack(pady=20, padx=30)

        self.buttons['1_1'] = tk.Button(mainFrame, text=' ', width=3, height=1, font=('Arial', 30), command=lambda: self.update_board(self.buttons['1_1'], 0, 0))
        self.buttons['1_1'].grid(row=0, column=0)
        self.buttons['1_2'] = tk.Button(mainFrame, text=' ', width=3, height=1, font=('Arial', 30), command=lambda: self.update_board(self.buttons['1_2'], 0, 1))
        self.buttons['1_2'].grid(row=0, column=1)
        self.buttons['1_3'] = tk.Button(mainFrame, text=' ', width=3, height=1, font=('Arial', 30), command=lambda: self.update_board(self.buttons['1_3'], 0, 2))
        self.buttons['1_3'].grid(row=0, column=2)
        self.buttons['2_1'] = tk.Button(mainFrame, text=' ', width=3, height=1, font=('Arial', 30), command=lambda: self.update_board(self.buttons['2_1'], 1, 0))
        self.buttons['2_1'].grid(row=1, column=0)
        self.buttons['2_2'] = tk.Button(mainFrame, text=' ', width=3, height=1, font=('Arial', 30), command=lambda: self.update_board(self.buttons['2_2'], 1, 1))
        self.buttons['2_2'].grid(row=1, column=1)
        self.buttons['2_3'] = tk.Button(mainFrame, text=' ', width=3, height=1, font=('Arial', 30), command=lambda: self.update_board(self.buttons['2_3'], 1, 2))
        self.buttons['2_3'].grid(row=1, column=2)
        self.buttons['3_1'] = tk.Button(mainFrame, text=' ', width=3, height=1, font=('Arial', 30), command=lambda: self.update_board(self.buttons['3_1'], 2, 0))
        self.buttons['3_1'].grid(row=2, column=0)
        self.buttons['3_2'] = tk.Button(mainFrame, text=' ', width=3, height=1, font=('Arial', 30), command=lambda: self.update_board(self.buttons['3_2'], 2, 1))
        self.buttons['3_2'].grid(row=2, column=1)
        self.buttons['3_3'] = tk.Button(mainFrame, text=' ', width=3, height=1, font=('Arial', 30), command=lambda: self.update_board(self.buttons['3_3'], 2, 2))
        self.buttons['3_3'].grid(row=2, column=2)

        self.buttonReset = tk.Button(mainFrame, text='De Nuevo', font=('Arial', 18), command=self.reset)
        self.buttonReset.grid(row=3, column=0, columnspan=3)
        self.disable_button(self.buttonReset)

        self.board = Board(self.player1)
        root.mainloop()

game = Main()
game.play()
