from xmlrpc.client import Boolean


class Waypoint:
    def __init__(self, pos: tuple, dim: str, name: str, desc: str = "", *args, **kwargs) -> "Waypoint":
        """
        DO NOT USE args PLZZZZZZZ
        kwargs is used to save different map options
        """
        self.x, self.y, self.z = pos
        self.name = name
        self.pos = pos
        self.dim = dim
        self.desc = desc
        for tkn in ["opts", "x", "y", "z"]:
            try:
                del kwargs[tkn]
            except:
                pass
        self.opts = kwargs

    def is_same_point(self, waypoint) -> Boolean:
        return self.pos == waypoint.pos

    @property
    def loc(self):
        """Location"""
        return f"{self.dim}: {self.x}, {self.y}, {self.z}"


def join_list(wplist1: list, wplist2: list) -> list:
    wpdict = {}
    wplist1.extend(wplist2)
    for waypoint in wplist1:
        waypoint = Waypoint(**waypoint)
        if waypoint.loc not in wpdict:
            wpdict[waypoint.loc] = waypoint
        elif waypoint.name == wpdict[waypoint.loc].name and waypoint.desc == wpdict[waypoint.loc].desc:
            # FORCED merge
            opts = wpdict[waypoint.loc].opts
            for opt in waypoint.opts:
                opts[opt] = waypoint.opts[opt]
        else:
            print(
                f"Conflict at joining waypoints <{waypoint.name}> and <{wpdict[waypoint.loc].name}>")
    return list(wpdict.values())
