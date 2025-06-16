from vasflam.uoevo.lib.gathering.mining import gathering_mine_tile, gathering_smelt_ore, gathering_unload_ore
from vasflam.uoevo.lib.pets import pet_feed, pet_mount, pet_unmount
from vasflam.uoevo.lib.runebook import runebook_cast
from vasflam.uoevo.lib.gathering.spots import CAVE_POINTS_COVETOUS_1, CAVE_POINTS_COMPASSION, CAVE_POINTS_BRITAIN_1, \
    CAVE_POINTS_COVETOUS_3, CAVE_POINTS_COVETOUS_2

beetle = 0x486945BF
beetleFood = 0x09F1
ingot_key = 0x45803A62
runebook = 0x46917676

caves = [
    CAVE_POINTS_COVETOUS_1,
    CAVE_POINTS_COVETOUS_2,
    CAVE_POINTS_COVETOUS_3,
    CAVE_POINTS_COMPASSION,
    CAVE_POINTS_BRITAIN_1,
]



pet_feed(beetle, beetleFood)
for i, points in enumerate(caves):
    pet_mount(beetle)
    runebook_cast(runebook, i+1, 'Sacred Journey')
    Misc.Pause(2000)
    pet_unmount()
    for point in points:
        path = PathFinding.GetPath(point[0], point[1], True)
        PathFinding.RunPath(path, 7000, False, True)

        while gathering_mine_tile(furnace=beetle, ingot_key=ingot_key):
            gathering_smelt_ore(beetle)
            Misc.Pause(200)
        gathering_unload_ore(ingotKey=ingot_key)
    gathering_unload_ore(ingotKey=ingot_key)
#for i in range(-2, 2):
#    for j in range(-2, 2):
#        while mine(i,j):
#            smeltBeetle()
#            Pause(200)
