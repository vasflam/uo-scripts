from vasflam.lib.logging import debug
from vasflam.uoevo.lib.crafting.blacksmithing import BS_CONFIG, BS_BOD_COLOR
from vasflam.uoevo.lib.crafting.bod import BOD
from vasflam.uoevo.lib.crafting.common import CraftingGump
from vasflam.uoevo.lib.crafting.tailoring import TAILORING_BOD_COLOR, TAILORING_CONFIG
from vasflam.uoevo.lib.crafting.tinkering import TINKERING_BOD_COLOR, TINKERING_CONFIG

BOD_TYPES = {
    # BS
    BS_BOD_COLOR: CraftingGump(BS_CONFIG),
    TAILORING_BOD_COLOR: CraftingGump(TAILORING_CONFIG),
    TINKERING_BOD_COLOR: CraftingGump(TINKERING_CONFIG),
}

def run_crafter(source_bag=None):
    source_bag = Player.Backpack.Serial if source_bag is None else source_bag
    t = Target.PromptTarget('Select BOD type', 48)
    if t:
        obj = Items.FindBySerial(t)
        color = obj.Color
        if color in BOD_TYPES:
            craft_gump = BOD_TYPES[color]
            bods = Items.FindAllByID(0x2258, color, Player.Backpack.Serial, 0, True)
            for b in bods:
                if int(Items.GetPropValue(b, 'Large Bulk Order')):
                    debug('Skip large BOD')
                    continue
                bod = BOD(b, craft_gump.crafting_config, source_bag=source_bag)
                if bod.filled():
                    print("Skip BOD. " + str(bod))
                    continue
                print(bod)
                craft_gump.craft_bod(bod, source_bag=source_bag)

                # Fill bod
                bod.fill()
        else:
            print('Unknown BOD type')