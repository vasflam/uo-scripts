from vasflam.uoevo.lib.runebook import runebook_cast
runebook = 0x46916A0D
spots = [
    # trinsic 1
    [
        0x0149AB1F,
        0x0018421B,
        0x001863B0,
        0x0018638A,
        0x001863A0,
        0x001863B9,
        0x04399DA7,
        0x001857FC,
        0x046CADBF,
    ],
    [
        0x0019652F,
        0x0019642B,
        0x00196495,
        0x0019650D,
        0x001964C9,
        0x001964F5,
        0x001962F4,
        0x00118A6C,
        0x001962B1,
        0x0019627D,
    ],
    [
        0x002E2F53,
        0x002E2F21,
        0x002E2F38,
        0x002E2F26,
        0x002E2F25,
        0x002E2F12,
        0x002E2F20,
    ],
    # Brit tailors
    [
        0x00189E8C,
        0x0018429B,
        0x00184296,
        0x0018A14D,
        0x00184299,
        0x00184298
    ]
]

def dress():
    Dress.ChangeList('lrc')
    Dress.DressFStart()
    while Dress.DressStatus():
        Misc.Pause(500)
        
def undress():
    Dress.ChangeList('lrc')
    Dress.UnDressFStart()
    while Dress.UnDressStatus():
        Misc.Pause(500)
        
while True:
    for i, spot in enumerate(spots):
        dress()
        runebook_cast(runebook, i+1, 'Sacred Journey')
        Misc.Pause(2000)
        undress()
        # undress
        for npc in spot:
            obj = Mobiles.FindBySerial(npc)
            if Player.DistanceTo(obj) > 2:
                path = PathFinding.GetPath(obj.Position.X, obj.Position.Y, True)
                PathFinding.RunPath(path, 7000, False, True)
            Player.UseSkill('Begging')
            Target.WaitForTarget(3000)
            Target.TargetExecute(obj)
            Misc.Pause(14000)