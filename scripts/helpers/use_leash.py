leash = Items.FindAllByID(0x1374, -1, Player.Backpack.Serial, 2)
if len(leash):
    Items.UseItem(leash[0])