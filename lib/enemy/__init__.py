from System.Collections.Generic import List
from System import Int32
from System import Byte

WW_WEAPONS = {
    0x0F4B: 'secondary',
    0x13FB: 'primary',
}

def enemy_find_list(range = 10):
    f = Mobiles.Filter()
    f.Enabled = True
    f.Notorieties = List[Byte](bytes([3, 4, 5, 6]))
    f.RangeMax = range
    return Mobiles.ApplyFilter(f)

def enemy_get_closest(max_range = 10):
    enemies = enemy_find_list(max_range)
    if len(enemies) == 0:
        return None
    return min(enemies, key=lambda e: Player.DistanceTo(e))
    #return min(enemies, key=lambda e: abs(e.Position.X-Player.Position.X) + abs(e.Position.Y-Player.Position.Y))

def enemy_attack_closest(max_range = 10, ability=None, text_delay=800):
    closest = enemy_get_closest(max_range)
    if closest is None:
        Player.HeadMessage(46, "No enemies near")
        return None

    if ability is not None:
        if ability == 'primary':
            Player.WeaponPrimarySA()
        else:
            Player.WeaponSecondarySA()

    Player.Attack(closest)
    Mobiles.Message(closest, 88, "[Attack target]", text_delay)

def enemy_attack_with_ww():
    ability = None
    weapon = Player.GetItemOnLayer('LeftHand')
    if weapon is not None and weapon.ItemID in WW_WEAPONS and not Player.HasSpecial:
        ability = 'primary' if WW_WEAPONS[weapon.ItemID] == 'primary' else 'secondary'

    enemy_attack_closest(max_range=2, ability=ability)
