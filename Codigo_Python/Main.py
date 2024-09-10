import tkinter as tk
from Board import Board
from Player import Player
from ButtonManager import ButtonManager

class Main:
    def __init__(self):
        # Inicializar jugadores y el tablero
        self.player1 = Player('X', 'Jugador 1')
        self.player2 = Player('O', 'Jugador 2')
        self.board = Board(self.player1)
        self.btnManager = ButtonManager()

        # Crear ventana
        self.root = tk.Tk()
        self.root.title("Gato")
        self.root.resizable(False, False)

        # (Para abrir la ventana al centro)
        x = (self.root.winfo_screenwidth() - 320) // 2
        y = (self.root.winfo_screenheight() - 400) // 2
        self.root.geometry(f'{320}x{400}+{x}+{y}')

        # Etiqueta superior
        self.label = tk.Label(self.root, text="Etiqueta superior", font=('Arial', 18))
        self.label.pack(pady=5, padx=5)

        # Frame
        self.mainFrame = tk.Frame(self.root)
        self.mainFrame.pack(pady=20, padx=30)

        # Crear botones
        self.buttons = {}
        self.create_buttons()

        # Botón de reset
        self.buttonReset = tk.Button(self.mainFrame, text='De Nuevo', width=5, height=1, font=('Arial', 18), command=self.reset)
        self.buttonReset.grid(row=3, column=1, padx=1, pady=1)
        self.btnManager.disable_button(self.buttonReset)

        # Iniciar el bucle de eventos
        self.root.mainloop()

    def create_buttons(self):
        """Crea y coloca los botones del tablero en la interfaz."""
        self.buttons['1_1'] = tk.Button(self.mainFrame, text='', width=3, height=2, font=('Arial', 30), command=lambda: self.update_board(self.buttons['1_1'], 0, 0))
        self.buttons['1_1'].grid(row=0, column=0, padx=1, pady=1)
        self.buttons['1_2'] = tk.Button(self.mainFrame, text='', width=3, height=2, font=('Arial', 30), command=lambda: self.update_board(self.buttons['1_2'], 0, 1))
        self.buttons['1_2'].grid(row=0, column=1, padx=1, pady=1)
        self.buttons['1_3'] = tk.Button(self.mainFrame, text='', width=3, height=2, font=('Arial', 30), command=lambda: self.update_board(self.buttons['1_3'], 0, 2))
        self.buttons['1_3'].grid(row=0, column=2, padx=1, pady=1)
        self.buttons['2_1'] = tk.Button(self.mainFrame, text='', width=3, height=2, font=('Arial', 30), command=lambda: self.update_board(self.buttons['2_1'], 1, 0))
        self.buttons['2_1'].grid(row=1, column=0, padx=1, pady=1)
        self.buttons['2_2'] = tk.Button(self.mainFrame, text='', width=3, height=2, font=('Arial', 30), command=lambda: self.update_board(self.buttons['2_2'], 1, 1))
        self.buttons['2_2'].grid(row=1, column=1, padx=1, pady=1)
        self.buttons['2_3'] = tk.Button(self.mainFrame, text='', width=3, height=2, font=('Arial', 30), command=lambda: self.update_board(self.buttons['2_3'], 1, 2))
        self.buttons['2_3'].grid(row=1, column=2, padx=1, pady=1)
        self.buttons['3_1'] = tk.Button(self.mainFrame, text='', width=3, height=2, font=('Arial', 30), command=lambda: self.update_board(self.buttons['3_1'], 2, 0))
        self.buttons['3_1'].grid(row=2, column=0, padx=1, pady=1)
        self.buttons['3_2'] = tk.Button(self.mainFrame, text='', width=3, height=2, font=('Arial', 30), command=lambda: self.update_board(self.buttons['3_2'], 2, 1))
        self.buttons['3_2'].grid(row=2, column=1, padx=1, pady=1)
        self.buttons['3_3'] = tk.Button(self.mainFrame, text='', width=3, height=2, font=('Arial', 30), command=lambda: self.update_board(self.buttons['3_3'], 2, 2))
        self.buttons['3_3'].grid(row=2, column=2, padx=1, pady=1)

    def reset(self):
        """Resetea el juego."""
        self.btnManager.update_button(self.label, ' ')
        self.btnManager.reset_buttons(self.buttons)
        self.btnManager.disable_button(self.buttonReset)
        self.player1 = Player('X', 'Jugador X')
        self.player2 = Player('O', 'Jugador O')
        self.board = Board(self.player1)
        self.board.reset_board()

    def update_board(self, button, x, y):
        """Actualiza el tablero y verifica el estado del juego cuando se presiona un botón."""
        if self.board.board[x][y] == ' ':
            self.board.place_symbol(x, y)
            self.btnManager.update_button(button, self.board.current_player.symbol)
            self.btnManager.disable_button(button)

            if self.board.check_winner():
                self.btnManager.disable_all_buttons(self.buttons)
                self.btnManager.update_button(self.label, f'{self.board.current_player.name} Gana!')
                self.btnManager.enable_button(self.buttonReset)
            elif self.board.is_board_full():
                self.btnManager.update_button(self.label, '¡Empate!')
                self.btnManager.enable_button(self.buttonReset)

            # Cambiar el turno al siguiente jugador
            self.board.current_player = self.player2 if self.board.current_player == self.player1 else self.player1


# Inicializar la aplicación
if __name__ == "__main__":
    Main()
