from vasflam.uoevo.lib.crafting.common import CraftingGump
from vasflam.uoevo.lib.crafting.resources import RESOURCE_COLORS, TINKERING_RESOURCE_COLORS
from vasflam.uoevo.lib.crafting.tinkering import TINKERING_CONFIG

item_to_make = 0x00
max_skill = 100
crafting = CraftingGump(TINKERING_CONFIG)
while Player.GetSkillValue('Tinkering') < max_skill:
    crafting.craft('ruby ring', 0x108A, TINKERING_RESOURCE_COLORS.search('iron'), 1)
    Misc.Pause(100)
    Misc.WaitForContext(0x001843ED, 10000)
    Misc.ContextReply(0x001843ED, 2)
    Misc.Pause(100)