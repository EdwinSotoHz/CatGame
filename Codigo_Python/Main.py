import tkinter as tk
from Board import Board
from Player import Player
from ButtonManager import ButtonManager

# Inicializar jugadores y el tablero
player1 = Player('X', 'Jugador 1')
player2 = Player('O', 'Jugador 2')
board = Board(player1)
btnManager = ButtonManager()

def reset():
    """Resetea el juego."""
    btnManager.update_button(label, ' ')
    btnManager.reset_buttons(buttons)
    global player1, player2, board
    player1 = Player('X', 'Jugador 1')
    player2 = Player('O', 'Jugador 2')
    board = Board(player1)
    board.reset_board()

def update_board(button, x, y): 
    """Actualiza el tablero y verifica el estado del juego cuando se presiona un botón."""
    if board.board[x][y] == ' ' and not board.is_board_full():
        board.place_symbol(x, y)
        btnManager.update_button(button, board.current_player.symbol)
        btnManager.disable_button(button)
        
        if board.check_winner():
            btnManager.disable_all_buttons(buttons)
            btnManager.update_button(label, f'{board.current_player.symbol} Gana!')
        elif board.is_board_full():
            btnManager.update_button(label, '¡Empate!')

        # Cambiar el turno al siguiente jugador
        board.current_player = player2 if board.current_player == player1 else player1

############################## INTERFAZ ##############################

# Crear ventana
root = tk.Tk()
root.title("Gato")
root.resizable(False, False)

# (Para abrir la ventana al centro)
x = (root.winfo_screenwidth() - 320) // 2
y = (root.winfo_screenheight() - 400) // 2
root.geometry(f'{320}x{400}+{x}+{y}')

# Etiqueta superior
label = tk.Label(root, text="Etiqueta superior", font=('Arial', 18))
label.pack(pady=5, padx=5)

# Frame
mainFrame = tk.Frame(root)
mainFrame.pack(pady=20, padx=30)

# Crear botones 
buttons = {} # los metodos llevan x = ?, y = ?
buttons['1_1'] = tk.Button(mainFrame, text='1', width=3, height=2, font=('Arial', 30), command=lambda: update_board(buttons['1_1'], 0, 0))
buttons['1_1'].grid(row=0, column=0, padx=1, pady=1)
buttons['1_2'] = tk.Button(mainFrame, text='2', width=3, height=2, font=('Arial', 30), command=lambda: update_board(buttons['1_2'], 0, 1))
buttons['1_2'].grid(row=0, column=1, padx=1, pady=1)
buttons['1_3'] = tk.Button(mainFrame, text='3', width=3, height=2, font=('Arial', 30), command=lambda: update_board(buttons['1_3'], 0, 2))
buttons['1_3'].grid(row=0, column=2, padx=1, pady=1)
buttons['2_1'] = tk.Button(mainFrame, text='4', width=3, height=2, font=('Arial', 30), command=lambda: update_board(buttons['2_1'], 1, 0))
buttons['2_1'].grid(row=1, column=0, padx=1, pady=1)
buttons['2_2'] = tk.Button(mainFrame, text='5', width=3, height=2, font=('Arial', 30), command=lambda: update_board(buttons['2_2'], 1, 1))
buttons['2_2'].grid(row=1, column=1, padx=1, pady=1)
buttons['2_3'] = tk.Button(mainFrame, text='6', width=3, height=2, font=('Arial', 30), command=lambda: update_board(buttons['2_3'], 1, 2))
buttons['2_3'].grid(row=1, column=2, padx=1, pady=1)
buttons['3_1'] = tk.Button(mainFrame, text='7', width=3, height=2, font=('Arial', 30), command=lambda: update_board(buttons['3_1'], 2, 0))
buttons['3_1'].grid(row=2, column=0, padx=1, pady=1)
buttons['3_2'] = tk.Button(mainFrame, text='8', width=3, height=2, font=('Arial', 30), command=lambda: update_board(buttons['3_2'], 2, 1))
buttons['3_2'].grid(row=2, column=1, padx=1, pady=1)
buttons['3_3'] = tk.Button(mainFrame, text='9', width=3, height=2, font=('Arial', 30), command=lambda: update_board(buttons['3_3'], 2, 2))
buttons['3_3'].grid(row=2, column=2, padx=1, pady=1)

# Botón de reset
buttonReset = tk.Button(mainFrame, text='Reset', width=5, height=1, font=('Arial', 18), command=reset)
buttonReset.grid(row=3, column=1, padx=1, pady=1)

# Iniciar el bucle de eventos
root.mainloop()
