t = Target.PromptTarget("Select item to add", 48)
if t:
    item = Items.FindBySerial(t)
    if item is not None:
        items = Items.FindAllByID(item.ItemID, 0, Player.Backpack.Serial, 0)
        print(type(items))
        for item in items:
            Gumps.SendAction(0xbfad58cd, 200)
            Target.WaitForTarget(10000, True)
            Target.TargetExecute(item)
            Gumps.WaitForGump(0xbfad58cd, 10000)

