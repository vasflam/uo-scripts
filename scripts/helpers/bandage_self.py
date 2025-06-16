if Timer.Check('bandage'):
    Player.HeadMessage(46, "Bandage in Progress")
else:
    if Player.Hits < Player.HitsMax or Player.Poisoned:
        Player.HeadMessage(46, "Bandage self")
        Items.UseItemByID(0x0E21, -1)
        Target.WaitForTarget(2000)
        Target.TargetExecute(Player.Serial)
        Timer.Create('bandage', 3700, "Bandage complete")
    else:
        Player.HeadMessage(46, "Full HP")
