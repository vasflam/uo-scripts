from vasflam.uoevo.lib.captcha import GumpData, GUMP_ID

while True:
    if Gumps.HasGump(GUMP_ID):
        gd = Gumps.GetGumpData(GUMP_ID)
        gd = GumpData(gd.gumpLayout, gd.gumpText)
        button = gd.solve()
        if button:
            Gumps.SendAction(GUMP_ID, button)

    Misc.Pause(400)