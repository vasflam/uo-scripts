from vasflam.uoevo.lib.gathering.mining import gathering_smelt_ore, gathering_mine_tile

beetle = 0x43e7b11
beetleFood = 0x09F1
ingot_key = 0x45803A62

t = Target.PromptGroundTarget("Select tail", 46)
if t is None:
    exit(0)
gathering_smelt_ore(furnace=beetle, ingot_key=ingot_key)
while gathering_mine_tile(tile=t, furnace=beetle, ingot_key=ingot_key, timeout=10000):
    Misc.Pause(300)
gathering_smelt_ore(furnace=beetle, ingot_key=ingot_key)