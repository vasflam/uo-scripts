PET_LOYALTY_WONDERFUL = 'Wonderful Happy'
PET_LOYALTY_EXTREME = 'Extreme Happy'
PET_LOYALTY_VERY = 'Very Happy'

PET_LOYALTY_LEVELS = [
    PET_LOYALTY_WONDERFUL,
    PET_LOYALTY_EXTREME,
    PET_LOYALTY_VERY,
]

def pet_mount(pet):
    if Player.Mount is None:
        Mobiles.UseMobile(pet)

def pet_unmount():
    if Player.Mount is not None:
        Mobiles.UseMobile(Player.Serial)


def pet_toggle_mount():
    mount = Misc.ReadSharedValue("mount")
    if mount <= 0:
        mount = Target.PromptTarget("Select your mount")
        if mount is None or mount <= 0:
            return
        Misc.SetSharedValue("mount", mount)

    if Player.Mount is not None:
        Mobiles.UseMobile(Player.Serial)
    else:
        mobile = Mobiles.FindBySerial(mount)
        if not mobile:
            Misc.SetSharedValue("mount", -1)
            return

        Mobiles.UseMobile(mount)

def pet_get_loyalty(pet, timeout = 5000):
    Mobiles.WaitForProps(pet, timeout)
    props = Mobiles.GetPropStringList(pet)
    for prop in props:
        if "Loyalty" in prop:
            a, b = [part.strip() for part in prop.split(':')]
            return b
    return None

def pet_loyalty_lower_than(pet, loyalty):
    pet_loyalty = pet_get_loyalty(pet)
    indexed = {value: index for index, value in enumerate(PET_LOYALTY_LEVELS)}
    if loyalty in indexed:
        p = indexed[pet_loyalty]
        n = indexed[loyalty]
        if p > n:
            return True
    return False

def pet_feed(pet, food_graphic):
    Player.HeadMessage(46, str(Player.DistanceTo(pet)))
    distance = Player.DistanceTo(pet)
    if 0 <= distance <= 2:
        food = Items.FindAllByID(food_graphic, 0, Player.Backpack.Serial, 2)
        if len(food) > 0:
            Items.Move(food[0], pet, 1)
            Misc.Pause(200)
