from System.Collections.Generic import List
from System import String


def fishing():
    Journal.Clear()
    Items.UseItem(0x5133D03B)
    Target.WaitForTarget(5000)
    p = Player.Position
    Target.TargetExecute(p.X+2, p.Y, p.Z)
    #Target.TargetExecuteRelative(Player.Serial, 0)
    while True:
        t = Journal.WaitJournal(List[String](['pull', 'fish a while', 'no fish', 'must wait', 'biting here']), 15000)
        if t == 'biting here':
            return False
        return True

while fishing():
    Misc.Pause(300)
