from BaseClasses import CollectionState, MultiWorld
from .Regions import connect_regions
from .Options import SuperCatPlanetOptions, scp_options

def set_rules(multiworld: MultiWorld, player: int):

    multiworld.get_location("Green Switch", player).access_rule = lambda state: state.has("Red Switch", player, 1) or state.has("Orange Switch", player, 1) or state.has("Blue Switch", player, 1) or state.has("Yellow Switch", player, 1)

    multiworld.get_location("Strange Cat [Final - Not Much Longer Now]", player).access_rule = lambda state: state.has("Pastry Basket", player, 1)
    multiworld.get_location("Star", player).access_rule = lambda state: state.has("Pastry Basket", player, 1)

    connect_regions(multiworld, player, "Menu", "Village", None)
    
    connect_regions(multiworld, player, "Village", "Jungle", None)
    connect_regions(multiworld, player, "Village", "Canyon", None)

    connect_regions(multiworld, player, "Canyon", "Void", lambda state: state.has("Orange Switch", player, 1))
    connect_regions(multiworld, player, "Canyon", "Flowers", lambda state: state.has("Orange Switch", player, 1))

    connect_regions(multiworld, player, "Jungle", "Lava Caves", None)
    connect_regions(multiworld, player, "Jungle", "Flowers", None)
    connect_regions(multiworld, player, "Jungle", "Factory", None)

    connect_regions(multiworld, player, "Mushrooms", "Final", lambda state: state.count("Strange Cat", player) >= 16)

    connect_regions(multiworld, player, "Factory", "Lava Caves", None)
    connect_regions(multiworld, player, "Factory", "Mushrooms", None)

    connect_regions(multiworld, player, "Lava Caves", "Ice Caves", None)
    connect_regions(multiworld, player, "Lava Caves", "Crows", lambda state: (state.has("Yellow Switch", player, 1) or state.has("White Switch", player, 1)) and state.has("Red Switch", player, 1) and state.has("Orange Switch", player, 1) and state.has("Blue Switch", player, 1))

    connect_regions(multiworld, player, "Ice Caves", "Flowers", None)
    connect_regions(multiworld, player, "Ice Caves", "Crows", lambda state: (state.has("Yellow Switch", player, 1) or state.has("White Switch", player, 1)) and state.has("Red Switch", player, 1) and state.has("Orange Switch", player, 1) and state.has("Blue Switch", player, 1))

    connect_regions(multiworld, player, "Crows", "Warp Room", None)

    connect_regions(multiworld, player, "Void", "Ice Caves", None)



    goal = getattr(multiworld.worlds[player].options, "ending_required")
    if(goal == 0):
        multiworld.completion_condition[player] = lambda state: state.can_reach("Crows", 'Region', player)
    else:
        multiworld.completion_condition[player] = lambda state: state.can_reach("Star", 'Location', player)
    
    if(getattr(multiworld.worlds[player].options, "cat_hunt_enabled")):
        multiworld.completion_condition[player] = lambda state: state.has("Cat", getattr(multiworld.worlds[player].options, "cat_hunt_target"))