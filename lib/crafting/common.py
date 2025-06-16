from vasflam.lib.logging import debug
from vasflam.uoevo.lib.crafting import CRAFTING_GUMP_ID
from vasflam.uoevo.lib.crafting.bod import BOD
from vasflam.uoevo.lib.crafting.resources import RESOURCE_COLORS


class CraftingGump:
    def __init__(self, crafting_config):
        self.crafting_config = crafting_config

    def count_items(self, graphic, color, exceptional, source_bag=None):
        source_bag = Player.Backpack.Serial if source_bag is None else source_bag
        items = Items.FindAllByID(graphic, color, source_bag, 0, True)
        amount = 0
        if exceptional:
            for item in items:
                Items.WaitForProps(item, 7000)
                if 'Exceptional' in item.Name or int(Items.GetPropValue(item, 'Exceptional')):
                    amount += item.Amount
                else:
                    # recycle it
                    if self.crafting_config.recycle_fn is not None:
                        self.crafting_config.recycle_fn(item)
        else:
            amount += sum(i.Amount for i in items)

        debug('found items: {} with total amount of {}'.format(len(items), amount))
        return amount

    def check_no_resources(self):
        # Check resources
        lines = Gumps.GetLineList(CRAFTING_GUMP_ID)
        no_resources = False
        for line in lines:
            if 'do not have' in line.lower():
                return True
        return False

    def craft(self, item_name, item_graphic, material, amount, exceptional=False, source_bag=None):
        section, craft_item = self.crafting_config.search_item(item_name)
        if craft_item is None:
            print('Failed to find item with name ' + item_name)
            return

        # Use tool
        tool = Items.FindByID(self.crafting_config.tool_graphic, 0, Player.Backpack.Serial, 2)
        if tool is None:
            raise BaseException('No crafting tool')

        Items.UseItem(tool)
        Gumps.WaitForGump(CRAFTING_GUMP_ID, 13000)
        if not Gumps.HasGump(CRAFTING_GUMP_ID):
            raise 'Something went wrong while waiting for crafting gump'

        # Choose material
        debug('Select colors, button: {}'.format(RESOURCE_COLORS.button))
        Gumps.SendAction(CRAFTING_GUMP_ID, RESOURCE_COLORS.button)
        Gumps.WaitForGump(CRAFTING_GUMP_ID, 13000)
        debug('Select color, button: {}'.format(material.button))
        Gumps.SendAction(CRAFTING_GUMP_ID, material.button)
        Gumps.WaitForGump(CRAFTING_GUMP_ID, 13000)

        # Choose section
        debug('select section {}, button {}'.format(section.name, section.button))
        Gumps.SendAction(CRAFTING_GUMP_ID, section.button)
        Gumps.WaitForGump(CRAFTING_GUMP_ID, 13000)

        first = True
        counter = 0
        print('Creating {}[{}]x{}'.format(item_name, material.name, amount))
        debug('counter={}, amount={}'.format(counter, amount))
        while self.count_items(item_graphic, material.color, exceptional, source_bag) < amount:
            if first:
                debug('creating first item with button {}'.format(craft_item.button))
                # Create First Item
                Gumps.SendAction(CRAFTING_GUMP_ID, craft_item.button)
                Gumps.WaitForGump(CRAFTING_GUMP_ID, 13000)
                Misc.Pause(300)
                first = False
                if self.check_no_resources():
                    debug('failed to create first item, no resources')
                    break

            debug('creating item with make last button {}'.format(21))
            Gumps.SendAction(CRAFTING_GUMP_ID, 21)
            Gumps.WaitForGump(CRAFTING_GUMP_ID, 13000)
            Misc.Pause(200)

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

    def craft_bod(self, bod: BOD, source_bag=None):
        amount = bod.amount - bod.amount_finished
        if amount == 0:
            return True
        self.craft(bod.item_name, bod.item_graphic, bod.material, amount, bod.exceptional, source_bag=source_bag)


class CraftingItem:
    def __init__(self, name, button, graphic = None):
        self.name = name.strip()
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
            #if isinstance(query, str) and query.lower() in item.name.lower():
            if isinstance(query, str) and query.lower() == item.name.lower():
                    return item
            if isinstance(query, int) and query == item.graphic:
                return item

        return None


class CraftingConfig:
    def __init__(self, bod_color, tool_graphic, sections, resources, recycle_fn=None, bod_gump_id=None):
        self.bod_color = bod_color
        self.sections = sections
        self.resources = resources
        self.tool_graphic = tool_graphic
        self.recycle_fn = recycle_fn
        self.bod_gump_id = bod_gump_id

    def search_item(self, name):
        for section in self.sections:
            item = section.search_item(name)
            if item:
                return section, item

        return None, None
