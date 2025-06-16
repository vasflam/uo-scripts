while True:
    if Journal.Search('Your belt point'):
        Player.HeadMessage(48, "Got bet point")
        Journal.Clear()
    Misc.Pause(300)