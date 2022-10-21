from lib import Waypoint

# overworld: default_0
# nether: default_-1
# end: default_1

def load_str(raw_str: str, dim: str) -> Waypoint:
    raw_str = str(raw_str).strip()
    str_list = raw_str.split(":")
    str_list = list(map(lambda x: x.replace("§§", ":"), str_list))
    str_list.pop(0)  # "waypoint"
    name = str_list.pop(0)
    abbr = str_list.pop(0)
    x = round(float(str_list.pop(0)))
    y = round(float(str_list.pop(0)))
    z = round(float(str_list.pop(0)))
    color = str_list.pop(0)
    disabled = str_list.pop(0)
    type = str_list.pop(0)
    set = str_list.pop(0)
    rotate_on_tp = str_list.pop(0)
    tp_yaw = str_list.pop(0)
    global_ = str_list.pop(0)
    return Waypoint((x, y, z), dim, name)

def dump_str(waypoint: Waypoint) -> str:
    return f"waypoint:{Waypoint.name}:{Waypoint.name[0]}:{Waypoint.x}:{Waypoint.y}:{Waypoint.z}:1:false:0:gui.xaero_default:false:0:false"

HEADER = """#
#waypoint:name:initials:x:y:z:color:disabled:type:set:rotate_on_tp:tp_yaw:global
#"""