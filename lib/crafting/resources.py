class ResourceColor:
    def __init__(self, name, color, button):
        self.name = name
        self.color = color
        self.button = button

    def equal(self, name):
        return name.lower() in self.name.lower()

    def __str__(self):
        return 'ResourceColor(name={}, color={}, button={})'.format(self.name, self.color, self.button)

class ResourceColors:
    def __init__(self, button: int, colors):
        self.button = button
        self.colors = colors

    def search(self, query):
        for c in self.colors:
            if isinstance(query, str) and query.lower() in c.name.lower():
                return c
            if isinstance(query, int) and query == c.color:
                return c

        return None

RESOURCE_COLORS = ResourceColors(7, [
    ResourceColor('default', 0, 6),

    # metal
    ResourceColor('Iron', 0, 6),
    ResourceColor('Dull Copper', 0x0973, 13),
    ResourceColor('Shadow Iron', 0x0966, 20),
    ResourceColor('Copper', 0x096d, 27),
    ResourceColor('Bronze', 0x0972, 34),
    ResourceColor('Gold', 0x08a5, 41),
    ResourceColor('Agapite', 0x0979, 48),
    ResourceColor('Verite', 0x089f, 55),
    ResourceColor('Valorite', 0x08ab, 62),
    ResourceColor('Blaze', 0x0489, 69),
    ResourceColor('Ice', 0x0480, 76),
    ResourceColor('Toxic', 0x04f8, 83),
    ResourceColor('Electrum', 0x04fe, 90),
    ResourceColor('Platinum', 0x0481, 97),

    # Wood
    ResourceColor('Board', 0, 6),
    ResourceColor('Pine', 0x0973, 13),
    ResourceColor('Ash', 0x096d, 27),
    ResourceColor('Mohogany', 0x0972, 34),
    ResourceColor('Yew', 0x08a5, 41),
    ResourceColor('Oak', 0x0979, 48),
    ResourceColor('Zircote', 0x089f, 55),
    ResourceColor('Ebony', 0x08ab, 62),
    ResourceColor('Bamboo', 0x0489, 69),
    ResourceColor('Heartwood', 0x0480, 76),
    ResourceColor('Bloodwood', 0x04f8, 83),
    ResourceColor('Frostwood', 0x04fe, 90),
])

TINKERING_RESOURCE_COLORS = ResourceColors(7, [
    ResourceColor('default', 0x0, 55),
    # metal
    ResourceColor('Verite', 0x089f, 6),
    ResourceColor('Valorite', 0x08ab, 13),
    ResourceColor('Blaze', 0x0489, 20),
    ResourceColor('Ice', 0x0480, 27),
    ResourceColor('Toxic', 0x04f8, 34),
    ResourceColor('Electrum', 0x04fe, 41),
    ResourceColor('Platinum', 0x0481, 48),
    ResourceColor('Iron', 0, 55),
    ResourceColor('Dull Copper', 0x0973, 62),
    ResourceColor('Shadow Iron', 0x0966, 69),
    ResourceColor('Copper', 0x096d, 76),
    ResourceColor('Bronze', 0x0972, 83),
    ResourceColor('Gold', 0x08a5, 90),
    ResourceColor('Agapite', 0x0979, 97),
])
