#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import template
from slpp import slpp as lua

WOW_INSTALL = "/mnt/hdd/Games/WoW 3.3.5"

MODELS = {
    'Warrior': {1: 'DPSWarr', 2: 'DPSWarr', 3: 'ProtWarr'},
    'DeathKnight': {1: 'TankDK', 2: 'DPSDK', 3: 'DPSDK'},
    'Druid': {2: 'Bear', 3: 'Tree', 1: 'Moonkin'},
    'Mage': {1: 'Mage', 2: 'Mage', 3: 'Mage'},
    'Warlock': {1: 'Warlock', 2: 'Warlock', 3: 'Warlock', },
    'Priest': {1: 'HealPriest', 2: 'HealPriest', 3: 'ShadowPriest'},
    'Hunter': {1: 'Hunter', 2: 'Hunter', 3: 'Hunter', },
    'Paladin': {1: 'Healadin', 2: 'ProtPaladin', 3: 'Retribution'},
    'Rogue': {1: 'Rogue', 2: 'Rogue', 3: 'Rogue', },
    'Shaman': {1: 'Elemental', 2: 'Enhance', 3: 'RestoSham'},
}

DEFAULT_RACE = {
    'Warrior': 'Orc',
    'DeathKnight': 'Orc',
    'Druid': 'Tauren',
    'Mage': 'BloodElf',
    'Warlock': 'BloodElf',
    'Priest': 'Undead',
    'Hunter': 'Orc',
    'Paladin': 'BloodElf',
    'Rogue': 'Undead',
    'Shaman': 'Tauren',
}

DEFAULT_ENCHANTS = {
    'Hunter': {
        1: [-53832, -13817, -33808, -41099, -83845, -93222, -113823, -163827, -153833, -193608, -123826,
            -122658, -120983, -123232, -121597],
        2: [-53832, -13817, -33808, -41099, -83845, -93222, -113823, -163827, -153833, -193608, -123826,
            -122658, -120983, -123232, -121597],
        3: [-53832, -13817, -33808, -41099, -83845, -93222, -113823, -163827, -153833, -193608, -123826,
            -122658, -120983, -123232, -121597],
    },
    'Warrior': {
        1: [-13817, -33808, -41099, -83845, -91603, -113823, -123826, -122658, -121597, -122939, -153789],
        2: [-13817, -33808, -41099, -83845, -91603, -113823, -123826, -122658, -121597, -122939, -153789],
        3: [-13818, -33811, -33852, -43294, -41951, -51953, -53297, -83850, -93330, -93253,
            -113822, -121075, -123232, -153869, -152673, -181952, -181071, -183849],
    },
    'DeathKnight': {
        1: [],
        2: [],
        3: [],
    },
    'Druid': {
        1: [],
        2: [],
        3: [],
    },
    'Mage': {
        1: [],
        2: [],
        3: [],
    },
    'Warlock': {
        1: [],
        2: [],
        3: [],
    },
    'Priest': {
        1: [],
        2: [],
        3: [],
    },
    'Paladin': {
        1: [],
        2: [],
        3: [],
    },
    'Rogue': {
        1: [],
        2: [],
        3: [],
    },
    'Shaman': {
        1: [],
        2: [],
        3: [],
    },
}

EQUIP_MAP = {
    1: 'Head',
    2: 'Neck',
    3: 'Shoulders',
    15: 'Back',
    4: 'Shirt',
    5: 'Chest',
    9: 'Wrist',
    10: 'Hands',
    6: 'Waist',
    7: 'Legs',
    8: 'Feet',
    11: 'Finger1',
    12: 'Finger2',
    13: 'Trinket1',
    14: 'Trinket2',
    16: 'MainHand',
    17: 'OffHand',
    18: 'Ranged',
}

EG_file = "WTF/Account/EXECUTIVE10/SavedVariables/ElitistGroup.lua"

if os.path.isfile('.wowpath'):
    with open('.wowpath') as f:
        wow_path = f.read()
else:
    while True:
        print("Please give the path to your WoW install:")
        wow_path = input()
        if os.path.isfile(os.path.join(wow_path, EG_file)):
            with open('.wowpath', 'w') as f:
                f.write(wow_path)
            break

with open(os.path.join(wow_path, EG_file)) as f:
    EG_data = f.read()

# first 17 bytes are a label
EG_data = lua.decode(EG_data[17:].replace(';', ''))
specs = {}  # the character's number of points in each tree
info = {}  # class and equipment
for userrealm in EG_data['faction']['Horde']['users']:
    username = userrealm.split('-')[0]
    data = EG_data['faction']['Horde']['users'][userrealm]
    data = lua.decode(data)
    if not data or 'talentTree1' not in data or data['level'] != 80 or 'equipment' not in data:
        continue
    main_spec = f"{data['talentTree1']}/{data['talentTree2']}/{data['talentTree3']}"
    class_token = data['classToken'].title()
    specs[username] = {1: data['talentTree1'], 2: data['talentTree2'], 3: data['talentTree3']}
    info[username] = {'equipment': data['equipment'], 'class': class_token}

print("Characters:")
print(", ".join(sorted(specs)))
print()
while True:
    print("Type a character's name to create their xml, or 'q' to quit.")
    user = input().title()
    if user in specs or user == 'Q':
        break

if user in specs:
    spec = max(specs[user], key=specs[user].get)
    class_name = info[user]['class']
    race = DEFAULT_RACE[class_name]
    model = MODELS[class_name][spec]
    equipment = ""
    available = ""
    for index in info[user]['equipment']:
        _, id, enchant, gem1, gem2, gem3, _, _, _, _ = info[user]['equipment'][index].split(':')
        itemString = '.'.join([id, gem1, gem2, gem3, enchant])
        equipment += f"  <{EQUIP_MAP[index]}>{itemString}</{EQUIP_MAP[index]}>\n"
        available += f"  <AvailableItems>{id}<AvailableItems>\n"
    for enchant in DEFAULT_ENCHANTS[class_name][spec]:
        available += f"  <AvailableItems>{enchant}<AvailableItems>\n"
    available = available[:-1]  # remove trailing newline
    equipment = equipment[:-1]  # remove trailing newline
    xml = template.template.format(model=model, race=race, class_name=class_name,
                                   equipment=equipment, name=user, available=available)

    with open(f"{user}.xml", 'w') as f:
        f.write(xml)
    print()
    print(f"Saved to '{user}.xml'.")
