from vasflam.uoevo.lib.crafting import CRAFTING_GUMP_ID
from vasflam.uoevo.lib.crafting.bod import BOD
from vasflam.uoevo.lib.crafting.resources import RESOURCE_COLORS


class CraftingGump:
    def __init__(self, crafting_config):
        self.crafting_config = crafting_config

    def craft(self, item_name, item_graphic, material, amount, exceptional = False):
        section, craft_item = self.crafting_config.search_item(item_name)
        if craft_item is None:
            print('Failed to find item with name ' + item_name)
            return

        # Use tool
        tool = Items.FindByID(self.crafting_config.tool_graphic, 0, Player.Backpack.Serial, 2)
        if tool is None:
            raise 'No crafting tool'

        Items.UseItem(tool)
        Gumps.WaitForGump(CRAFTING_GUMP_ID, 13000)
        if not Gumps.HasGump(CRAFTING_GUMP_ID):
            raise 'Something went wrong while waiting for crafting gump'

        # Choose material
        Gumps.SendAction(CRAFTING_GUMP_ID, RESOURCE_COLORS.button)
        Gumps.WaitForGump(CRAFTING_GUMP_ID, 13000)
        Gumps.SendAction(CRAFTING_GUMP_ID, material.button)
        Gumps.WaitForGump(CRAFTING_GUMP_ID, 13000)

        # Choose section
        Gumps.SendAction(CRAFTING_GUMP_ID, section.button)
        Gumps.WaitForGump(CRAFTING_GUMP_ID, 13000)

        first = True
        counter = 1
        print('Creating {}[{}]x{}'.format(item_name, material.name, amount))
        while counter < amount:
            items = Items.FindAllByID(item_graphic, material.color, Player.Backpack.Serial, 0, True)
            if exceptional:
                new_counter = 0
                for item in items:
                    Items.WaitForProps(item, 7000)
                    if 'Exceptional' in item.Name or int(Items.GetPropValue(item, 'Exceptional')):
                        new_counter += 1
                counter = new_counter
            else:
                counter = len(items)
            print(counter)

            if counter >= amount:
                return

            if first:
                # Create First Item
                Gumps.SendAction(CRAFTING_GUMP_ID, craft_item.button)
                Gumps.WaitForGump(CRAFTING_GUMP_ID, 13000)
                first = False

            Gumps.SendAction(CRAFTING_GUMP_ID, 21)
            Gumps.WaitForGump(CRAFTING_GUMP_ID, 13000)

            # Check resources
            lines = Gumps.GetLineList(CRAFTING_GUMP_ID)
            no_resources = False
            for line in lines:
                if 'do not have' in line:
                    no_resources = True
            if no_resources:
                print('\tDo not have resources for this BOD')
                break

        Misc.Pause(500)
        Gumps.CloseGump(CRAFTING_GUMP_ID)
        print('Complete {}[{}]x{}'.format(item_name, material.name, amount))

    def craft_bod(self, bod: BOD):
        amount = bod.amount - bod.amount_finished
        if amount == 0:
            return True
        self.craft(bod.item_name, bod.item_graphic, bod.material, amount, bod.exceptional)


class CraftingItem:
    def __init__(self, name, button, graphic = None):
        self.name = name
        self.graphic = graphic
        self.button = button

class CraftingSection:
    def __init__(self, name, button, items):
        self.name = name
        self.button = button
        self.items = items

    def select(self):
        if Gumps.GumpExists(CRAFTING_GUMP_ID):
            Gumps.SendAction(CRAFTING_GUMP_ID, self.button)
            Gumps.WaitForGump(CRAFTING_GUMP_ID, 3000)
            return True
        return False

    def search_item(self, query):
        for item in self.items:
            if isinstance(query, str) and query.lower() in item.name.lower():
                return item
            if isinstance(query, int) and query == item.graphic:
                return item

        return None


class CraftingConfig:
    def __init__(self, bod_color, tool_graphic, sections, resources):
        self.bod_color = bod_color
        self.sections = sections
        self.resources = resources
        self.tool_graphic = tool_graphic

    def search_item(self, name):
        for section in self.sections:
            item = section.search_item(name)
            if item:
                return section, item

        return None, None
