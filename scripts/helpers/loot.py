key = 0x57ED1232

def unload_to_key(key):
    Misc.WaitForContext(key, 10000)
    Misc.ContextReply(key, 2)

def find_corpses():
    f = Items.Filter()
    f.Enabled = True
    f.IsCorpse = True
    f.RangeMax = 2
    f.CheckIgnoreObject = True
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
        got_target = Target.WaitForTarget(2000, True)
        if not got_target:
            print('ignore object')
            Misc.IgnoreObject(corpse)
            break
    Target.Cancel()
cut_leather()
unload_to_key(key)
