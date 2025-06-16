from vasflam.uoevo.lib.crafting import BOD_GUMP_ID


class BOD:
    def __init__(self, serial: int, crafting_config, source_bag=None):
        self.serial = serial
        self.source_bag = Player.Backpack.Serial if source_bag is None else source_bag
        self.gump_id = crafting_config.bod_gump_id if crafting_config.bod_gump_id else BOD_GUMP_ID

        Items.UseItem(serial)
        Gumps.WaitForGump(self.gump_id, 13000)
        gd = Gumps.GetGumpData(self.gump_id)
        text = gd.gumpText
        self.item_name = text[4].strip()
        _, item = crafting_config.search_item(self.item_name)
        self.exceptional = 'All items must be exceptional.' in text
        self.amount = int(gd.gumpData[0])
        self.item_graphic = item.graphic if item and item.graphic else int(gd.gumpData[1])
        self.amount_finished = int(gd.gumpData[2])
        self.material = crafting_config.resources.search('default')
        self.fulfilled = self.amount == self.amount_finished
        # fulfilled gump don't have information about resource
        if len(gd.gumpData) > 3 and not self.fulfilled:
            query = gd.gumpData[3].split('with')[1].strip().split(' ')[0].strip()
            print(query)
            self.material = crafting_config.resources.search(query)
        Gumps.CloseGump(self.gump_id)

    def fill(self):
        if self.filled():
            return

        iterations = 0
        while not self.filled() or iterations > 20:
            items = Items.FindAllByID(self.item_graphic, self.material.color, self.source_bag, 0, True)
            iterations += 1
            if len(items):
                Items.UseItem(self.serial)
                Gumps.WaitForGump(self.gump_id, 13000)
                for item in items:
                    if self.exceptional and not ('Exceptional' in item.Name or int(Items.GetPropValue(item, 'Exceptional'))):
                        continue
                    Gumps.SendAction(self.gump_id, 2)
                    Gumps.WaitForGump(self.gump_id, 13000)
                    Target.WaitForTarget(13000)
                    Target.TargetExecute(item)
                    Misc.Pause(30)
                    self.amount_finished += 1
                    if self.filled():
                        break
                Misc.Pause(400)
                Gumps.SendAction(self.gump_id, 1)
                Target.ClearLastandQueue()
            else:
                return

    def filled(self):
        return self.amount_finished >= self.amount

    def __str__(self):
        return 'Bod {} {}[{}, {}] {}/{}'.format(
            'exceptional' if self.exceptional else '',
            self.item_name,
            self.item_graphic,
            self.material.name,
            self.amount_finished,
            self.amount
        )
