class Waypoint:
    def __init__(self, pos: tuple, dim: str, name: str, desc: str, *args, **kwargs) -> "Waypoint":
        """
        DO NOT USE args PLZZZZZZZ
        kwargs is used to save different map options
        """
        self.x, self.y, self.z = pos
        self.dim = dim
        self.desc = desc
        self.opts = kwargs

