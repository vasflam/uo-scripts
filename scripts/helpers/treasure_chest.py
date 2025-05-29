lockpicks_type = 0x14FC

data_file = './treasure_trash_items.json'

def load_trash_items():
    items = {}
    with open(data_file, 'rb') as f:
        for line in f:
            decoded = line.decode('ascii').strip()
            k,v = decoded.split(':')
            items[int(k, 16)] = v

    return items

def save_trash_items(data):
    with open(data_file, 'w') as f:
        for k,v in data.items():
            s = "{id}:{name}\n".format(id=hex(k), name=v)
            f.write(s)

def create_trash_list():
    items = load_trash_items()
    while True:
        item_serial = Target.PromptTarget("Select Item to hide", 56)
        if item_serial > 0:
            item = Items.FindBySerial(item_serial)
            items[item.ItemID] = item.Name
            Items.Hide(item)
        else:
            break
    save_trash_items(items)

def open_chest(chest):
    while True:
        Journal.Clear()
        if Items.BackpackCount(lockpicks_type, -1) < 1:
            return False
        Items.UseItemByID(lockpicks_type, -1)
        Target.WaitForTarget(3000)
        Target.TargetExecute(chest)
        while True:
            if Journal.Search('unable to pick'):
                break
            if Journal.Search('yield') or Journal.Search('to be locked'):
                return True

def hide_items(chest, hide_list):
    Items.WaitForContents(chest, 3000)
    Misc.Pause(300)
    content = chest.Contains
    hidden = 0
    for item in content:
        if item.ItemID in hide_list:
            Items.Hide(item)
            hidden += 1
            
    if len(content) > hidden:
        return True
    

chest_serial = Target.PromptTarget("Select treasure chest", 48)
if chest_serial:
    chest = Items.FindBySerial(chest_serial)
    if chest and 'Treasure' in chest.Name:
        opened = open_chest(chest)
        if opened:
            Items.UseItem(chest)
            Items.WaitForContents(chest, 3000)
            hide_list = load_trash_items()
            hide_items(chest, hide_list)
            create_trash_list()