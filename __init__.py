from typing import Dict, List

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, components, launch_subprocess, Type
from .Items import SCPItem, SCPItemData, get_items_by_category, item_table
from .Locations import SCPLocation, location_table, full_location_table
from .Options import scp_options
from .Regions import create_regions
from .Rules import set_rules
import random


class SuperCatPlanetWebWorld(WebWorld):
    theme = "ice"
    
    '''
    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to setting up Super Cat Planet.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["lone"]
    )

    tutorials = [setup_en]
    '''

class SuperCatPlanetWorld(World):
    """
    Super Cat Planet
    """
    game = "Super Cat Planet"
    web = SuperCatPlanetWebWorld()
    option_definitions = scp_options
    topology_present = True
    # web = RLWeb()

    

    item_name_to_id = {name: data.address for name, data in item_table.items()}
    location_name_to_id = {name: data.address for name, data in full_location_table.items()}

    def get_setting(self, name: str):
        return getattr(self.multiworld, name)[self.player]

    def fill_slot_data(self) -> dict:
        return {option_name: self.get_setting(option_name).value for option_name in scp_options}

    def create_items(self):
        item_pool: List[SCPItem] = []
        character_list = []
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        number_placed_item = 0
        
        for name, data in item_table.items():
            quantity = data.max_quantity

            # Categories to be ignored, they will be added in a later stage.
            if data.category == "Junk":
                continue
            if data.category == "Traps":
                continue

            item_pool += [self.create_item(name) for _ in range(0, quantity)]

        # Fill any empty locations with filler items.
        while len(item_pool) + number_placed_item < total_locations:
            item_pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        fillers = get_items_by_category("Junk") | get_items_by_category("Traps")
        weights = [data.weight for data in fillers.values()]
        return self.multiworld.random.choices([filler for filler in fillers.keys()], weights, k=1)[0]

    def create_item(self, name: str) -> SCPItem:
        data = item_table[name]
        return SCPItem(name, data.classification, data.address, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.player)

    def create_regions(self):
        create_regions(self.multiworld, self.player)