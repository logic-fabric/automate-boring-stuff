from inventory import stringify_inventory


def test_with_an_empty_inventory():
    inventory = dict()
    expected_string = """
INVENTORY
=========
------------------------
Total: 0 item and 0 coin
"""
    assert stringify_inventory(inventory) == expected_string

def test_stringify_an_empty_inventory():
    inventory = dict()
    expected_string = """
INVENTORY
=========
------------------------
Total: 0 item and 0 coin
"""
    assert stringify_inventory(inventory) == expected_string

def test_stringify_an_inventory_containing_only_one_item():
    inventory = {'arrow': 1}
    expected_string = """
INVENTORY
=========
1 arrow
------------------------
Total: 1 item and 0 coin
"""
    assert stringify_inventory(inventory) == expected_string

def test_stringify_an_inventory_containing_only_a_duplicated_item():
    inventory = {'arrow': 2}
    expected_string = """
INVENTORY
=========
2 arrows
-------------------------
Total: 2 items and 0 coin
"""
    assert stringify_inventory(inventory) == expected_string

def test_stringify_an_inventory_containing_only_one_coin():
    inventory = {'gold coin': 1}
    expected_string = """
INVENTORY
=========
1 gold coin
------------------------
Total: 0 item and 1 coin
"""
    assert stringify_inventory(inventory) == expected_string

def test_stringify_an_inventory_containing_only_two_identical_coins():
    inventory = {'gold coin': 2}
    expected_string = """
INVENTORY
=========
2 gold coins
-------------------------
Total: 0 item and 2 coins
"""
    assert stringify_inventory(inventory) == expected_string

def test_stringify_an_inventory_containing_only_one_item_and_one_coin():
    inventory = {'arrow': 1,'gold coin': 1}
    expected_string = """
INVENTORY
=========
1 arrow

1 gold coin
------------------------
Total: 1 item and 1 coin
"""
    assert stringify_inventory(inventory) == expected_string

def test_stringify_a_complex_inventory():
    inventory = {
        'arrow': 12,
        'gold coin': 14,
        'rope': 1,
        'torch': 5,
        'dagger': 1,
        'silver coin': 53,
        'platinum coin': 1,
    }
    expected_string = """
INVENTORY
=========
12 arrows
1 dagger
1 rope
5 torchs

14 gold coins
1 platinum coin
53 silver coins
----------------------------
Total: 19 items and 68 coins
"""
    assert stringify_inventory(inventory) == expected_string
