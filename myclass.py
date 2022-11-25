class Ship:
    def __init__(self, y, x, size, name):
        self.y = y
        self.x = x
        self.size = size
        self.name = name

    def __str__(self):
        return f'{self.y, self.x, self.size}'
