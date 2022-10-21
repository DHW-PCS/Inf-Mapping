# Inf-Mapping

Waypoint set in DHW-Inf for different map mods

Waypoint set in different mods will be stored in different folders

## Inf Map `waypoint.json`

```json
{
    "waypoints": [
        {
            "name": "name",
            "x": 111,
            "y": 222,
            "z": 333,
            "dim": "overworld",
            "desc": "Description",
            "opts": {
                "xaerosmap": {
                    "opt1": "value1"
                },
                "journeymap": {
                    "opt1": "value1"
                }
            }
        }
    ]
}
```

## Supporting mods

- XaerosMinimap(recommended)
- JourneyMap
- VoxelMap(mod no longer updating)

## Naming convention

Make sure that the location of each waypoint is as accurate as possible, especially the y-coordinate, and that waypoints in the nether that are part of the nether traffic system have names ending in `-地狱交通`.

Feel free to add a variety of waypoints, but remember to keep each point meaningful

## How to use

### VoxelMap

Somethings...

### JourneyMap

Somethings...

### XaerosMinimap

Go to the corresponding folder and download the Multiplayer_domain" folder and move the file to your minecraft folder. If you don't have version isolation on, the path is usually "/.minecraft/XaeroWaypoints/". Otherwise, the path is generally "/.minecraft/versions/yourgameversion/XaeroWaypoints/".

In particular, note that you may need to change the domain name part of the folder name to accommodate your client. For example, if the domain name you used to join Inf was "example.exp", then you need to change the "domain" in the folder name to "example.exp".

## TODO

Add support for more than just python🤮
