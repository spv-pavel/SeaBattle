class Ship:
    def __init__(self, y, x, size):
        self.y = y
        self.x = x
        self.size = size

    def __str__(self):
        return f'{self.y, self.x, self.size}'
