class Piece:
    def __init__(self, color, is_king=False):
        self.color = color
        self.is_king = is_king
    
    def __repr__(self):
        king_str = "King" if self.is_king else "Piece"
        return f"{self.color} {king_str}"
