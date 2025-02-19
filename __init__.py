from typing import Dict, List

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, components, launch_subprocess, Type
from .Items import SCPItem, SCPItemData, get_items_by_category, item_table
from .Locations import SCPLocation, location_table, full_location_table
from .Options import scp_options, SuperCatPlanetOptions
from .Regions import create_regions
from .Rules import set_rules, create_extra_walls, goal_rule, wall_rule
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
    option_dataclass = SuperCatPlanetOptions
    options: SuperCatPlanetOptions
    extra_walls_table: Dict[str, str]
    topology_present = True
    # web = RLWeb()

    item_name_to_id = {name: data.address for name, data in item_table.items()}
    location_name_to_id = {name: data.address for name, data in full_location_table.items()}

    def generate_early(self):
        self.extra_walls_table = create_extra_walls(self.multiworld, self.player)

    def make_walls(self):
        return create_extra_walls(self.multiworld, self.player)

    def get_setting(self, name: str):
        return getattr(self.multiworld, name)[self.player]

    def fill_slot_data(self) -> dict:
        slot_data_dict = {option_name: self.get_setting(option_name).value for option_name in scp_options}
        slot_data_dict["extra_walls_table"] = self.extra_walls_table
        return slot_data_dict

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
            
            # Add items to the pool if their category is enabled by settings
            if (data.category == "Cats" and self.options.cat_rando.value):
                if(not self.options.include_final_stage.value):
                    quantity -= 1
                item_pool += [self.create_item(name) for _ in range(0, quantity)]

            if (data.category == "Strange Cats" and self.options.strange_cat_rando.value):
                if(not self.options.include_final_stage.value):
                    quantity -= 1
                item_pool += [self.create_item(name) for _ in range(0, quantity)]

            if (name == "Pastry Basket" and self.options.include_final_stage.value):
                item_pool += [self.create_item(name) for _ in range(0, quantity)]

            # Add items in universal categories to the pool
            if (data.category == "Switches"):
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

    def create_extra_walls(self):
        return create_extra_walls(self.multiworld, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.player, self.extra_walls_table)

    def create_regions(self):
        create_regions(self.multiworld, self.player)