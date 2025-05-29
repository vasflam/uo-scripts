from uoevo.lib.crafting import BOD_GUMP_ID
from uoevo.lib.crafting.resources import RESOURCE_COLORS


class BOD:
    def __init__(self, serial: int):
        self.serial = serial

        Items.UseItem(serial)
        Gumps.WaitForGump(BOD_GUMP_ID, 13000)
        gd = Gumps.GetGumpData(BOD_GUMP_ID)
        text = gd.gumpText
        self.item_name = text[4].strip()
        self.exceptional = 'All items must be exceptional.' in text
        self.amount = int(gd.gumpData[0])
        self.item_graphic = int(gd.gumpData[1])
        self.amount_finished = int(gd.gumpData[2])
        self.material = RESOURCE_COLORS.search('iron')
        self.fulfilled = self.amount == self.amount_finished
        # fulfilled gump don't have information about resource
        if len(gd.gumpData) > 3 and not self.fulfilled:
            query = gd.gumpData[3].split('with')[1].strip().split(' ')[0].strip()
            self.material = RESOURCE_COLORS.search(query)
        Gumps.CloseGump(BOD_GUMP_ID)

    def fill(self):
        if self.filled():
            return

        items = Items.FindAllByID(self.item_graphic, self.material.color, Player.Backpack.Serial, 0, True)
        if len(items):
            Items.UseItem(self.serial)
            Gumps.WaitForGump(BOD_GUMP_ID, 13000)
            for item in items:
                if self.exceptional and not ('Exceptional' in item.Name or int(Items.GetPropValue(item, 'Exceptional'))):
                    continue
                Gumps.SendAction(BOD_GUMP_ID, 2)
                Gumps.WaitForGump(BOD_GUMP_ID, 13000)
                Target.WaitForTarget(13000)
                Target.TargetExecute(item)
                Misc.Pause(30)
                self.amount_finished += 1
                if self.filled():
                    break
            Misc.Pause(400)
            Gumps.SendAction(BOD_GUMP_ID, 1)
            Target.ClearLastandQueue()

    def filled(self):
        return self.amount_finished >= self.amount

    def __str__(self):
        return 'Bod {}{}[{}] {}/{}'.format(
            'exceptional' if self.exceptional else '',
            self.item_name,
            self.material.name,
            self.amount_finished,
            self.amount
        )
