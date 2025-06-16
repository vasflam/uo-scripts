from vasflam.lib.enemy import enemy_get_closest

old_enemy = False
enemy_serial = Misc.ReadSharedValue("last_enemy")
if enemy_serial:
    enemy = Mobiles.FindBySerial(enemy_serial)
    old_enemy = True
    if not enemy:
        old_enemy = False
        enemy = enemy_get_closest()
else:
    enemy = enemy_get_closest()
    if enemy:
        Misc.SetSharedValue("last_enemy", enemy.Serial)
    
if enemy:
    Spells.Cast("Lightning Strike")
    if not old_enemy:
        Player.InvokeVirtue("Honor")
        Target.WaitForTarget(3000, True)
        Target.TargetExecute(enemy)
    Player.WeaponPrimarySA()
    Player.Attack(enemy)
    
    
    