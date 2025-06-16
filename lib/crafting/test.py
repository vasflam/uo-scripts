from vasflam.uoevo.lib.crafting import CRAFTING_GUMP_ID


def scan_gump(start_text, start_button):
    gd = Gumps.GetGumpData(CRAFTING_GUMP_ID)
    print(dir(gd))
    print(gd.stringList)
    if gd:
        started = False
        for line in gd.gumpText:
            if 'page' in line.lower():
                continue
            if start_text.lower() in line.lower():
                started = True
            #print(line)
            if started:
                print("CraftingItem('{}', {}),".format(line.strip(), start_button))
                start_button += 7

def scan_gump_custom(start_text, start_button):
    gd = Gumps.GetGumpData(CRAFTING_GUMP_ID)
    if gd:
        started = False
        for line in gd.stringList:
            if 'PAGE' in line:
                continue
            if 'LAST TEN' in line:
                continue
            if start_text.lower() in line.lower():
                started = True
            #print(line)
            if started:
                print("CraftingItem('{}', {}),".format(line.strip(), start_button))
                start_button += 7
