class Waypoint:
    def __init__(self, pos: tuple, dim: str, name: str, desc: str) -> "Waypoint":
        self.x, self.y, self.z = pos
        self.dim = dim
        self.desc = desc

