GUMP_ID = 0xec59e0f2
BOOK_ID = 0x2259
BOOK_COLOR = 0x04b4

# add button - 200-201-202
# remove button - 100-101-102


def read_book():
    book = Items.FindByID(BOOK_ID, BOOK_COLOR, Player.Backpack.Serial, 2)
    if not book:
        return False

    if not Gumps.HasGump():
        Items.UseItem(book)
        Gumps.WaitForGump(GUMP_ID, 7000)
    gd = Gumps.GetGumpData(GUMP_ID)
    if gd:
        print(dir(gd))
        print(gd.gumpStrings)
        print(gd.stringList)