from System.Collections.Generic import List
from System import String
from vasflam.uoevo.lib.pets import pet_feed
import math


bandages_id = 0x0E21
pet_serial = 0x047FF331

def get_pack_backpack(pack_serial):
    pet = Mobiles.FindBySerial(pet_serial)
    if pet:
        return pet.Backpack

def get_weight():
    weight = int(math.ceil(Player.GetSkillValue("Stealing")))
    return weight

def get_bandages(container_serial):
    items = Items.FindAllByID(bandages_id, 0 ,container_serial, 2)
    if len(items):
        return items[0]
        
def check_animal_bandages(backpack_serial):
    weight = get_weight()
    bandages = get_bandages(backpack_serial)
    delta = weight - bandages.Amount if bandages else 0
    if delta >= 0:
        delta = weight if delta == 0 else delta
        player_bandages = get_bandages(Player.Backpack.Serial)
        Items.Move(player_bandages, backpack_serial, delta)
        Misc.Pause(300)
    else:
        Items.Move(bandages, Player.Backpack.Serial, abs(delta))
        Misc.Pause(300)
    return get_bandages(backpack_serial)

def bushido():
    Misc.Pause(600)
    axe = 0x46F359FB
    Player.EquipItem(axe)
    Spells.Cast('Evasion')
    Misc.Pause(800)
    Player.UnEquipItemByLayer('RightHand', 3000)
        
def steal(item):
    if item:
        Player.UseSkill("Stealing")
        Target.WaitForTarget(3000)
        Target.TargetExecute(item)        
        msg = Journal.WaitJournal(List[String](['success', 'fail']), 5000)
        bushido()
        Misc.Pause(8400)
        
    

def start():
    pack_backpack = get_pack_backpack(pet_serial)
    if not pack_backpack:
        return
    while True:
        if not Timer.Check("petfeed"):
            pet_feed(pet_serial, 0x09D0)
            Timer.Create("petfeed", 30 * 60 * 1000)
        to_steal = check_animal_bandages(pack_backpack.Serial)
        steal(to_steal)
    Misc.Pause(300)

start()