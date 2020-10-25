from inventory import add_loot_to_inventory, stringify_inventory


COMPLEX_INVENTORY = {
    'arrow': 12,
    'gold coin': 14,
    'rope': 1,
    'torch': 5,
    'dagger': 1,
    'silver coin': 53,
    'platinum coin': 1,
}


def test_add_new_to_stuf_then_stringify_inventory():
    inventory = dict(COMPLEX_INVENTORY)
    loot = ['new stuff', 'arrow', 'gold coin']

    new_inventory = dict(COMPLEX_INVENTORY)
    new_inventory['new stuff'] = 1
    new_inventory['arrow'] += 1
    new_inventory['gold coin'] += 1

    assert add_loot_to_inventory(inventory, loot) == new_inventory

    expected_string = """
INVENTORY
=========
13 arrows
1 dagger
1 new stuff
1 rope
5 torchs

15 gold coins
1 platinum coin
53 silver coins
----------------------------
Total: 21 items and 69 coins
"""
    assert stringify_inventory(inventory) == expected_string