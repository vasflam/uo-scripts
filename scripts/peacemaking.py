while True:
    Player.UseSkill('peacemaking')
    Target.WaitForTarget(3000)
    if Journal.Search('What instrument'):
        inst = Items.FindByID(0x0E9D, -1, Player.Backpack.Serial, 2)
        if inst:
            Target.TargetExecute(inst)
            Target.WaitForTarget(3000)
        else:
            Target.Cancel()
            break
    Target.TargetExecute(Player.Serial)
    Misc.Pause(6300)