from inventory import add_loot_to_inventory


COMPLEX_INVENTORY = {
    'arrow': 12,
    'gold coin': 14,
    'rope': 1,
    'torch': 5,
    'dagger': 1,
    'silver coin': 53,
    'platinum coin': 1,
}


def test_add_nothing_to_inventory():
    inventory = dict(COMPLEX_INVENTORY)
    loot = []
    assert add_loot_to_inventory(inventory, loot) == COMPLEX_INVENTORY

def test_add_a_new_kind_of_stuff_to_inventory():
    inventory = dict(COMPLEX_INVENTORY)
    loot = ['new stuff']

    new_inventory = dict(COMPLEX_INVENTORY)
    new_inventory['new stuff'] = 1

    assert add_loot_to_inventory(inventory, loot) == new_inventory

def test_add_two_identical_new_stuff():
    inventory = dict(COMPLEX_INVENTORY)
    loot = ['new stuff', 'new stuff']

    new_inventory = dict(COMPLEX_INVENTORY)
    new_inventory['new stuff'] = 2

    assert add_loot_to_inventory(inventory, loot) == new_inventory

def test_add_existing_kind_of_stuff():
    inventory = dict(COMPLEX_INVENTORY)
    loot = ['arrow']

    new_inventory = dict(COMPLEX_INVENTORY)
    new_inventory['arrow'] += 1

    assert add_loot_to_inventory(inventory, loot) == new_inventory
