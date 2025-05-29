evo_key = 0x454A4BFD
reg_key = 0x450106CC

def unload_to_key(key):
    Misc.WaitForContext(key, 10000)
    Misc.ContextReply(key, 2)
    Gumps.WaitForGump(0xc0f93b2d, 10000)
    Gumps.CloseGump(0xc0f93b2d)

def find_corpses():
    f = Items.Filter()
    f.Enabled = True
    f.IsCorpse = True
    f.RangeMax = 2
    return Items.ApplyFilter(f)
    
def cut_leather():
    hides = Items.FindAllByID(0x1079, -1, Player.Backpack.Serial, 2)
    for hide in hides:
        Items.UseItemByID(0x0F9F, -1)
        Target.WaitForTarget(2000, True)
        Target.TargetExecute(hide)

corpses = find_corpses()
if len(corpses):
    Player.ChatSay("[claim -c")
    Target.WaitForTarget(2000, True)
    for corpse in corpses:
        Target.TargetExecute(corpse)
        Target.WaitForTarget(2000, True)
    Target.Cancel()
cut_leather()
unload_to_key(evo_key)
