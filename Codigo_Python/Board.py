class Board:
    def __init__(self, player):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]  # Lista bidimensional para guardar los simbolos
        self.current_player = player  # Jugador actual

    def place_symbol(self, x, y):
        if self.board[x][y] == ' ':  # Solo colocar símbolo si la casilla está vacía
            self.board[x][y] = self.current_player.symbol  # Agregar la casilla presionada con su simbolo
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
        return all(cell != ' ' for row in self.board for cell in row)

    def reset_board(self):
        """Reinicia todas las casillas del tablero a su estado original y restablece el turno."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
