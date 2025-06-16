from vasflam.lib.items_a import find_item_in_backpack

leash_graphic = 0x1374
items = find_item_in_backpack(leash_graphic, -1, 1)
if items and len(items):
    Items.UseItem(items[0])
else:
    Player.HeadMessage(48, "No Leashes")