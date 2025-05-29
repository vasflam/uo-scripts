GUMP_ID_RUNEBOOK = 0x8f3b5a22

def runebook_cast(runebook, runeNumber, spell = 'Recall'):
    baseNum = 1
    if spell == 'Sacred Journey':
        baseNum = 3
    elif spell == 'Gate Travel':
        baseNum = 2
    gumpButton = 4 + baseNum + (runeNumber-1) * 6

    x = Player.Position.X
    y = Player.Position.Y

    Items.UseItem(runebook)
    Gumps.WaitForGump(GUMP_ID_RUNEBOOK, 10000)
    Gumps.SendAction(GUMP_ID_RUNEBOOK, gumpButton)
    Misc.Pause(300)

    while Player.Position.X == x and Player.Position.Y == y:
        Misc.Pause(400)
    Misc.Pause(500)
