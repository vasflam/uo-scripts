import time
from uoevo.lib.gathering import GUMP_ID_INGOT_KEY

TYPE_SHOVEL = 0x0F39
TYPE_ORES = [0x19B7, 0x19B8, 0x19B9, 0x19BA]
nextMessages = ['loose', 'fail to find', 'put', 'extract', 'must wait', 'worn']
stopMessages = ['no metal', 'far away', 'be seen', "can't mine"]

def gathering_get_shovel():
    shovel = Items.FindByID(TYPE_SHOVEL, -1, Player.Backpack.Serial, True)
    return shovel if shovel else None

def gathering_stack_ore():
    ores = []
    for t in TYPE_ORES:
        ores.extend(Items.FindAllByID(t, -1, Player.Backpack.Serial, 0))

    colored = {}
    # get colors
    for ore in ores:
        clr = ore.Color
        if clr not in colored:
            colored[clr] = []
        colored[clr].append(ore)
        
    for v in colored.values():
        if len(v) > 1:
            stack = v[0]
            piles = v[1:]
            for pile in piles:
                Items.UseItem(pile)
                Target.WaitForTarget(2000)
                Target.TargetExecute(stack)
                Misc.Pause(200)
    
def gathering_smelt_ore(furnace = None, ingot_key = None, force = False):
    if Player.Weight+30 >= Player.MaxWeight or force:
        gathering_stack_ore()
        if furnace is None:
            return
        for t in TYPE_ORES:
            ores = Items.FindAllByID(t, -1, Player.Backpack.Serial, 0)
            for ore in ores:
                if ore.Graphics == TYPE_ORES[0] and ore.Amount == 1:
                    continue
                Items.UseItem(ore)
                Target.WaitForTarget(3000)
                Target.TargetExecute(furnace)
                Misc.Pause(200)
        gathering_unload_ore(ingot_key)
    
def gathering_unload_ore(ingotKey):
    if ingotKey is not None:
        Misc.WaitForContext(ingotKey, 10000)
        Misc.ContextReply(ingotKey, 2)
        Gumps.WaitForGump(GUMP_ID_INGOT_KEY, 5000)
        Gumps.CloseGump(GUMP_ID_INGOT_KEY)
                    
# mine - mine a tile
def gathering_mine_tile(tile = None, furnace = None, ingot_key = None, timeout=5000):
    gathering_smelt_ore(furnace, ingot_key)
    shovel = gathering_get_shovel()
    if not shovel:
        Player.HeadMessage(33, 'No shovel')
        return False
    Journal.Clear()
    Items.UseItem(shovel)
    Target.WaitForTarget(2000)
    if tile is None:
        Target.TargetExecuteRelative(Player.Serial, 0)
    else:
        Target.TargetExecute(tile.X, tile.Y, tile.Z)
    Misc.Pause(500)
    start = int(time.time()) * 1000
    while True:
        if any(Journal.Search(phrase) for phrase in stopMessages):
            return False
        if any(Journal.Search(phrase) for phrase in nextMessages):
            return True
        if int(time.time())*1000 - start > timeout:
            return True
        Misc.Pause(300)
