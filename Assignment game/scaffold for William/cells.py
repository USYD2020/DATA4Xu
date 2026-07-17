class Air:
    def __init__(self):
        self.display = ' '


class Wall:
    def __init__(self):
        self.display = '*'


class Start:
    def __init__(self):
        self.display = 'X'


class End:
    def __init__(self):
        self.display = 'Y'


class Water:
    def __init__(self):
        self.display = 'W'


class Fire:
    def __init__(self):
        self.display = 'F'


class Teleport:
    def __init__(self, display):
        self.display = display
