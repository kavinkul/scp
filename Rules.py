from typing import Dict
from BaseClasses import CollectionState, MultiWorld
from .Regions import connect_regions
from .Options import SuperCatPlanetOptions, scp_options
import random



def set_rules(multiworld: MultiWorld, player: int, extra_walls_table: Dict[str, str]):

    multiworld.get_location("Green Switch", player).access_rule = lambda state: state.has("Red Switch", player, 1) or state.has("Orange Switch", player, 1) or state.has("Blue Switch", player, 1) or state.has("Yellow Switch", player, 1)
    
    if getattr(multiworld.worlds[player].options, "include_final_stage"):
        multiworld.get_location("Strange Cat [Final - Not Much Longer Now]", player).access_rule = lambda state: state.has("Pastry Basket", player, 1)
        multiworld.get_location("Star", player).access_rule = lambda state: state.has("Pastry Basket", player, 1)

    connect_regions(multiworld, player, "Menu", "Village", None)
    
    connect_regions(multiworld, player, "Village", "Jungle", lambda state: wall_rule(state, multiworld, player, extra_walls_table, "Village_Jungle"), twoway=True)
    connect_regions(multiworld, player, "Village", "Canyon", lambda state: wall_rule(state, multiworld, player, extra_walls_table, "Village_Canyon"), twoway=True)

    connect_regions(multiworld, player, "Canyon", "Void", lambda state: state.has("Orange Switch", player, 1))
    connect_regions(multiworld, player, "Canyon", "Flowers", lambda state: state.has("Orange Switch", player, 1), twoway=True)

    connect_regions(multiworld, player, "Jungle", "Lava Caves", lambda state: wall_rule(state, multiworld, player, extra_walls_table, "Jungle_Lava"), twoway=True)
    connect_regions(multiworld, player, "Jungle", "Flowers", lambda state: wall_rule(state, multiworld, player, extra_walls_table, "Jungle_Flowers"), twoway=True)
    connect_regions(multiworld, player, "Jungle", "Factory", lambda state: wall_rule(state, multiworld, player, extra_walls_table, "Jungle_Factory"), twoway=True)

    connect_regions(multiworld, player, "Mushrooms_outside", "Mushrooms", lambda state: wall_rule(state, multiworld, player, extra_walls_table, "Lava_Mushrooms"), twoway=True)
    connect_regions(multiworld, player, "Mushrooms", "Final", lambda state: state.count("Strange Cat", player) >= 16)

    connect_regions(multiworld, player, "Factory", "Mushrooms_outside", None)
    connect_regions(multiworld, player, "Mushrooms_outside", "Factory", lambda state: state.has("Purple Switch", player, 1) and state.has("Blue Switch", player, 1))
    
    connect_regions(multiworld, player, "Mushrooms_outside", "Lava Caves", None)
    connect_regions(multiworld, player, "Lava Caves", "Mushrooms_outside", lambda state: state.has("Purple Switch", player, 1))
    connect_regions(multiworld, player, "Lava Caves", "Crows_intro", lambda state: wall_rule(state, multiworld, player, extra_walls_table, "Lava_Ice"), twoway=True)

    connect_regions(multiworld, player, "Ice Caves", "Flowers", lambda state: wall_rule(state, multiworld, player, extra_walls_table, "Flowers_Ice"), twoway=True)
    connect_regions(multiworld, player, "Ice Caves", "Crows_intro", lambda state: wall_rule(state, multiworld, player, extra_walls_table, "Lava_Ice"), twoway=True)

    connect_regions(multiworld, player, "Crows_intro", "Crows", lambda state: (((state.has("Left Yellow Switch", player, 1) and \
        state.has("Right Yellow Switch", player, 1)) or \
        state.has("White Switch", player, 1)) and \
        state.has("Red Switch", player, 1) and \
        state.has("Orange Switch", player, 1) and \
        state.has("Blue Switch", player, 1)), twoway=True)

    connect_regions(multiworld, player, "Crows", "Warp Room", None)

    connect_regions(multiworld, player, "Void", "Ice Caves", None)



    multiworld.completion_condition[player] = lambda state: goal_rule(state, player, multiworld)

    #goal = getattr(multiworld.worlds[player].options, "ending_required")
    #if(goal == 0):
    #    multiworld.completion_condition[player] = lambda state: state.can_reach("Crows", 'Region', player)
    #else:
    #    multiworld.completion_condition[player] = lambda state: state.can_reach("Star", 'Location', player)
    #
    #if(getattr(multiworld.worlds[player].options, "cat_hunt_enabled")):
    #    multiworld.completion_condition[player] = lambda state: state.has("Cat", getattr(multiworld.worlds[player].options, "cat_hunt_target"))

def create_extra_walls(multiworld: MultiWorld, player: int) -> Dict[str, str]:

    reg_links = ["Village_Jungle", "Village_Canyon", "Jungle_Lava", "Jungle_Flowers", "Jungle_Factory", "Factory_Lava", "Lava_Mushrooms", "Lava_Ice", "Flowers_Ice"]
    switches = ["Red Switch", "Orange Switch", "Yellow Switch", "Blue Switch", "White Switch", "Purple Switch"]
    next3 = [random.choice(switches) for _ in range(3)]
    switches = switches + next3
    random.shuffle(switches)

    walls = {key: value for key, value in (zip(reg_links, switches))}
    print(walls)
    return walls

def wall_rule(state: CollectionState, multiworld: MultiWorld, player: int, walls: Dict[str, str], regs: str) -> bool:
    if(not getattr(multiworld.worlds[player].options, "extra_walls")):
        return True
    
    switch = walls[regs]
    can_pass = False
    if(switch == "Yellow Switch"):
        if(state.has("Left Yellow Switch", player, 1) and state.has("Right Yellow Switch", player, 1)):
            can_pass = True
    elif state.has(switch, player, 1):
        can_pass = True
    return can_pass
    

def goal_rule(state: CollectionState, player: int, multiworld: MultiWorld) -> bool:
    can_goal = True
    goal = getattr(multiworld.worlds[player].options, "ending_required")
    cats = getattr(multiworld.worlds[player].options, "cat_hunt_target")
    
    if(goal == 0):
        can_goal = state.can_reach("Crows", 'Region', player)
    else:
        can_goal = state.can_reach("Star", 'Location', player)
    
    if(not getattr(multiworld.worlds[player].options, "cat_hunt_enabled")):
        cats = 0
    if(cats > 0 and state.has("Cat", player, ) < cats):
        can_goal = False
    
    return can_goal