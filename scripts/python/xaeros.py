import json
from lib import *
import os

# overworld: dim%0
# nether: default_-1
# end: default_1
dims = {
    "overworld": "dim%0",
    "nether": "dim%-1",
    "end": "dim%1"
}
HEADER = """#
#waypoint:name:initials:x:y:z:color:disabled:type:set:rotate_on_tp:tp_yaw:global
#
"""
dir = os.path.dirname(__file__)


def load_str(raw_str: str, dim: str) -> Waypoint:
    """
    Load a waypoint from Xaeros string
    """
    raw_str = str(raw_str).strip()
    str_list = raw_str.split(":")
    str_list = list(map(lambda x: x.replace("§§", ":"), str_list))
    str_list.pop(0)  # "waypoint"
    name = str_list.pop(0)
    abbr = str_list.pop(0)
    try:
        x = round(float(str_list.pop(0)))
    except:
        x = 0
    try:
        y = round(float(str_list.pop(0)))
    except:
        y = 0
    try:
        z = round(float(str_list.pop(0)))
    except:
        z = 0
    xaeros_opt = {}
    xaeros_opt["color"] = str_list.pop(0)
    xaeros_opt["disabled"] = str_list.pop(0)
    xaeros_opt["type"] = str_list.pop(0)
    xaeros_opt["set"] = str_list.pop(0)
    xaeros_opt["rotate_on_tp"] = str_list.pop(0)
    xaeros_opt["tp_yaw"] = str_list.pop(0)
    xaeros_opt["global"] = str_list.pop(0)
    return Waypoint(pos=(x, y, z), dim=dim, name=name, xaeros_opt=xaeros_opt)


def dump_str(waypoint: Waypoint) -> str:
    """
    Dump a Waypoint Object into Xaeros string
    """
    xaeros_opt = {
        "color": "1",
        "disabled": "false",
        "type": "0",
        "set": "gui.xaero_default",
        "rotate_on_tp": "false",
        "tp_yaw": "0",
        "global": "false"
    }
    if "xaeros_opt" in waypoint.opts:
        for opt in waypoint.opts["xaeros_opt"]:
            xaeros_opt[opt] = waypoint.opts["xaeros_opt"][opt]
    return f"waypoint:{waypoint.name}:{waypoint.name[0]}:{waypoint.x}:{waypoint.y}:{waypoint.z}:{xaeros_opt['color']}:{xaeros_opt['disabled']}:{xaeros_opt['type']}:{xaeros_opt['set']}:{xaeros_opt['rotate_on_tp']}:{xaeros_opt['tp_yaw']}:{xaeros_opt['global']}"


def read_all() -> dict:
    """
    Read from `data/data.json` and Xaeros file in the same directory as `__file__`
    """
    wplist = []
    with open(os.path.join(dir, "..", "..", "data", "data.json"), "r") as f:
        data = json.loads(f.read())
    for dim in dims:
        if os.path.isdir(os.path.join(dir, dims[dim])):
            with open(os.path.join(dir, dims[dim], "mw$default_1.txt"), "r") as f:
                raw_list = f.read().split(HEADER)[-1].strip().split("\n")
            wplist.extend(map(lambda x: load_str(x, dim).__dict__, raw_list))
    data["waypoints"] = list(
        map(lambda x: x.__dict__, join_list(data["waypoints"], wplist)))
    return data


def write_all(data: dict):
    """
    Write the `data` as the Xaeros format in the `__file__` directory
    """
    wpdict = {
        "overworld": [],
        "nether": [],
        "end": []
    }
    for waypoint in data["waypoints"]:
        wpdict[waypoint["dim"]].append(waypoint)
    build_dir = os.path.join(dir, "..", "..", "build", "Xaerosmap")
    if not os.path.exists(build_dir):
        os.mkdir(build_dir)
    for dim in dims:
        if len(wpdict[dim]) > 0:
            if not os.path.exists(os.path.join(build_dir, dims[dim])):
                os.mkdir(os.path.join(build_dir, dims[dim]))
            with open(os.path.join(build_dir, dims[dim], "mw$default_1.txt"), "w") as f:
                f.write(
                    HEADER + "\n".join(map(lambda x: dump_str(Waypoint(**x)), wpdict[dim])) + "\n")
