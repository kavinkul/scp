from typing import Dict, List

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, components, launch_subprocess, Type
from .Items import SCPItem, SCPItemData, get_items_by_category, item_table
from .Locations import SCPLocation, location_table, full_location_table
from .Options import scp_option_groups, SuperCatPlanetOptions
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

    option_groups = scp_option_groups

class SuperCatPlanetWorld(World):
    """
    Super Cat Planet
    """
    game = "Super Cat Planet"
    web = SuperCatPlanetWebWorld()
    #option_definitions = scp_options
    options_dataclass = SuperCatPlanetOptions
    options: SuperCatPlanetOptions

    extra_walls_table: Dict[str, str]
    junk_pool: Dict[str, int]
    topology_present = True
    # web = RLWeb()

    item_name_to_id = {name: data.address for name, data in item_table.items()}
    location_name_to_id = {name: data.address for name, data in full_location_table.items()}

    def generate_early(self):

        if(self.options.ending_required.value == 1):
            self.options.include_final_stage.value = 1
        if(self.options.cat_hunt_enabled.value == 1):
            self.options.cat_rando.value = 1
        if(self.options.include_final_stage.value == 1):
            self.options.strange_cat_rando.value = 1
        
        self.extra_walls_table = create_extra_walls(self)


    #def get_setting(self, name: str):
    #    return getattr(self.multiworld, name)[self.player]

    def fill_slot_data(self) -> dict:
        #slot_data_dict = {option_name: self.get_setting(option_name).value for option_name in scp_options}
        slot_data_dict = self.options.as_dict("cat_rando", "local_cats", "strange_cat_rando", "extra_walls", "hidden_costume_rando", "ending_required",
                                               "include_final_stage", "cat_hunt_enabled", "cat_hunt_target", "easy_wind", "death_link", "death_link_amnesty",
                                               "costume_weight", "ogmo_trap", "darkness_trap", "crow_trap", casing="snake")
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
        self.junk_pool = self.create_junk_pool()

        filler = self.random.choices(*zip(*self.junk_pool.items()), k=total_locations - len(item_pool))
        item_pool += [self.create_item(name) for name in filler]

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choices([filler for filler in self.junk_pool.keys()], list(self.junk_pool.values), k=1)[0]

    def create_item(self, name: str) -> SCPItem:
        data = item_table[name]
        return SCPItem(name, data.classification, data.address, self.player)

    def create_extra_walls(self):
        return create_extra_walls(self)

    def create_junk_pool(self) -> Dict[str, int]:
        junk_pool: Dict[str, int] = {}
        junk_pool = {
            "Costume": self.options.costume_weight.value,
            "Ogmo Trap": self.options.ogmo_trap.value,
            "Darkness Trap": self.options.darkness_trap.value,
            "Crow Trap": self.options.crow_trap.value,
        }
        return junk_pool

    def set_rules(self):
        set_rules(self, self.extra_walls_table)

    def create_regions(self):
        create_regions(self)