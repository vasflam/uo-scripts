if Timer.Check("consecrate"):
    Timer.Create("consecrate", 6000)
    Player.Cast('Consecrate Weapon')
    
def cast(spell, duration):
    if Timer.Check(spell):
        return False
    else:
        Journal.Clear("recovered")
        Spells.Cast(spell)
        Misc.Pause(300)
        if Journal.Search("recovered"):
            return False
        Timer.Create(spell, duration, spell + " off")
        return True

def chivalry():
    if cast('Consecrate Weapon', 6000):
        return
    if cast('Divine Fury', 20000):
        return

#Spells.Cast('Evasion')
#Spells.Cast('Momentum Strike')
Player.WeaponPrimarySA()        
chivalry()