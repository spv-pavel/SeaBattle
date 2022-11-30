class Ship:
    def __init__(self, y, x, size, hits=0, condition='whole'):
        self.y = y
        self.x = x
        self.size = size
        self.hits = hits
        self.condition = condition

    def __str__(self):
        return f'{self.y, self.x, self.size, self.hits, self.condition}'
