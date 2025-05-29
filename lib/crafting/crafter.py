from vasflam.uoevo.lib.crafting.blacksmithing import BS_CONFIG
from vasflam.uoevo.lib.crafting.bod import BOD
from vasflam.uoevo.lib.crafting.common import CraftingGump

BOD_TYPES = {
    # BS
    0x044e: CraftingGump(BS_CONFIG)
}

def run_crafter():
    t = Target.PromptTarget('Select BOD type', 48)
    if t:
        obj = Items.FindBySerial(t)
        color = obj.Color
        if color in BOD_TYPES:
            craft_gump = BOD_TYPES[color]
            bods = Items.FindAllByID(0x2258, color, Player.Backpack.Serial, 0, True)
            for b in bods:
                bod = BOD(b)
                if bod.filled():
                    print("Skip BOD. " + str(bod))
                    continue
                craft_gump.craft_bod(bod)

                # Fill bod
                bod.fill()