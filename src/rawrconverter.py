#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import template, utils
from utils.slpp import slpp as lua

if __name__ == '__main__':
    EG_data = utils.get_eg_data()

    # first 18 bytes are just the variable name that the EG table is loaded by, we don't need that.
    EG_data = lua.decode(EG_data[18:])
    specs = {}  # the character's number of points in each tree
    info = {}  # class and equipment
    for faction in EG_data['faction']:
        for userrealm in EG_data['faction'][faction]['users']:
            username = userrealm.split('-')[0]
            data = EG_data['faction']['Horde']['users'][userrealm]
            data = utils.egdata_to_json(data)
            if not data or 'talentTree1' not in data or data['level'] != 80 or 'equipment' not in data:
                continue
            class_token = data['classToken'].title()
            specs[username] = {1: data['talentTree1'], 2: data['talentTree2'], 3: data['talentTree3']}
            info[username] = {'equipment': data['equipment'], 'class': class_token}

    # We've parsed the EG file and gotten all our data. Time to interact with the end-user.
    print("Characters:")
    print(", ".join(sorted(specs)))
    print()
    while True:
        print("Type a character's name to create their xml, or 'q' to quit.")
        user = input().title()
        if user in specs or user == 'Q':
            break

    if user in specs:
        # gets us the index of the talent tree with the most points.
        # This could eventually be turned into trying to match the spec with a 'best guess' using
        # Rawr's built-in default specs.
        spec = max(specs[user], key=specs[user].get)
        class_name = info[user]['class']
        race = utils.DEFAULT_RACE[class_name]
        model = utils.MODELS[class_name][spec]

        # At this point we need to convert our wow ItemString from EG into Rawr XML.
        # We generate both the equipped gear, as well as the available gear/enchants for the optimizer.
        equipment = ""
        available = ""
        for index in info[user]['equipment']:
            _, id, enchant, gem1, gem2, gem3, _, _, _, _ = info[user]['equipment'][index].split(':')
            gem1 = utils.GEM_MAP[gem1]
            gem2 = utils.GEM_MAP[gem2]
            gem3 = utils.GEM_MAP[gem3]
            itemString = '.'.join([id, gem1, gem2, gem3, enchant])
            equipment += f"  <{utils.EQUIP_MAP[index]}>{itemString}</{utils.EQUIP_MAP[index]}>\n"
            available += f"  <AvailableItems>{id}</AvailableItems>\n"
        for enchant in utils.DEFAULT_ENCHANTS_AVAILABLE[class_name][spec]:
            available += f"  <AvailableItems>{enchant}</AvailableItems>\n"
        available = available[:-1]  # remove trailing newline
        equipment = equipment[:-1]  # remove trailing newline

        xml = template.template.format(model=model, race=race, class_name=class_name,
                                       equipment=equipment, name=user, available=available)

        with open(f"{user}.xml", 'w') as f:
            f.write(xml)
        print()
        print(f"Saved to '{user}.xml'.")
