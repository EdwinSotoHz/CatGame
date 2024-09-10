class Player:
    def __init__(self, symbol, name):
        self.name = name  # 'X' o 'O'
        self.symbol = symbol  # 'X' o 'O'
    
    def reset_player(self):  # Resetea atributos
        self.victory_count = 0