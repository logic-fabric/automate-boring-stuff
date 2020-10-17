"""Implement a function that takes an inventory as a dictionary and display it like this:

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

if given inventory = {
    'arrow': 12,
    'gold coin': 14,
    'rope': 1,
    'torch': 5,
    'dagger': 1,
    'silver coin': 53,
    'platinum coin': 1,
}
"""


def stringify_inventory(inventory):
    equipment = [
        (item, inventory[item]) for item in inventory 
        if not item.endswith(" coin")
    ]
    equipment.sort()
    wealth = [
        (item, inventory[item]) for item in inventory if 
        item.endswith(" coin")
    ]
    wealth.sort()

    items = 0
    str_equipment = ""

    for item in equipment:
        stuff, quantity = item
        items += quantity
        if quantity > 1:
            stuff += "s"
        str_equipment += f"{quantity} {stuff}\n"

    coins = 0
    str_wealth = ""

    for item in wealth:
        coin_type, quantity = item
        coins += quantity
        if quantity > 1:
            coin_type += "s"
        str_wealth += f"{quantity} {coin_type}\n"

    if str_equipment and str_wealth:
        str_inventory = str_equipment + "\n" + str_wealth
    else:
        str_inventory = str_equipment + str_wealth

    plural_item = "s" if items > 1 else ""
    plural_coin = "s" if coins > 1 else ""
    summary = f"Total: {items} item{plural_item} and {coins} coin{plural_coin}"

    return f"""
INVENTORY
=========
{str_inventory}{'-' * len(summary)}
{summary}
"""


if __name__ == "__main__":
    inventory = {
        'arrow': 12,
        'gold coin': 14,
        'rope': 1,
        'torch': 5,
        'diamond': 3,
        'platinum coin': 1,
        'magic wand': 3,
        'copper coin': 89,
        'dagger': 1,
        'silver coin': 53
    }
    print(stringify_inventory(inventory))
