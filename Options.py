from typing import Dict
from dataclasses import dataclass

from Options import Visibility, Choice, Range, NamedRange, Option, Toggle, DeathLink, DefaultOnToggle, OptionSet, PerGameCommonOptions, OptionGroup

#class SplitJumps(Toggle):
#   """Starts the player with only one of the three jump heights."""
#   display_name = "Split Jumps"
#   default = False

class CatsRandomized(Toggle):
    """Includes Cats into randomization."""
    display_name = "Randomize Cats"
    default = True

class LocalCats(NamedRange):
    """
    Forces some percent of Cat items to be found inside of your slot.
    Reduces flooding in the multiworld.
    """
    visibility = Visibility.none
    display_name = "Local Cat Percentage"
    range_start = 0
    range_end = 100
    special_range_names = {
        "off": -1,
        "weak": 50,
        "strong": 75,
        "all": 100
    }

    default = -1
    

class StrangeCatsRandomized(Toggle):
    """Includes Strange Cats into randomization."""
    display_name = "Randomize Strange Cats"
    default = True

class ExtraWalls(Toggle):
    """Adds button walls between areas to break up progression. Highly recommended."""
    display_name = "Extra Button Walls"
    default = True

class HiddenCostumesRandomized(Toggle):
    """Includes Hidden Costume locations as checks."""
    display_name = "Hidden Costumes"
    default = False

class EndingRequired(Choice):
    """Chooses which ending is required to goal."""
    display_name = "Goal Ending"
    option_crows = 0
    option_final_boss = 1
    default = 0

class FinalStage(Toggle):
    """
    Includes checks found in the final stage.
    Automatically enabled if goal is set to True Ending.
    Automatically enables strange cat randomization.
    """
    display_name = "Include Final Stage"
    default = False

class CatHuntEnabled(Toggle):
    """
    Enables Cat Hunt.
    Cat Hunt requires you to already have the required number of cats when performing your goal ending.
    If you reach your ending before reaching this number, you will need to reach it again after receiving enough cats.
    Automatically enables cat randomization.
    """
    display_name = "Cat Hunt"
    default = False

class CatHuntTarget(Range):
    """Required Cats to goal with Cat Hunt."""
    display_name = "Cat Hunt Target"
    range_start = 1
    range_end = 170
    default = 150

class EasyWind(Toggle):
    """Significantly reduces the strength of the wind for two cat locations in Ice Caves."""
    display_name = "Weaker Wind"
    default = False

class DeathLinkAmnesty(Range):
    """Number of deaths required per activation of death link."""
    display_name = "Death Link Amnesty"
    range_start = 1
    range_end = 20
    default = 1

#item weights

class CostumeWeight(Range):
    """Weight of costume filler in the item pool."""
    display_name = "Costume Weight"
    range_start = 1
    range_end = 100
    default = 10

class OgmoTrap(Range):
    """Weight of ogmo traps in the item pool."""
    display_name = "Ogmo Trap Weight"
    range_start = 0
    range_end = 100
    default = 1

class DarknessTrap(Range):
    """Weight of darkness traps in the item pool."""
    display_name = "Darkness Trap Weight"
    range_start = 0
    range_end = 100
    default = 1

class CrowTrap(Range):
    """Weight of crow traps in the item pool."""
    display_name = "Crow Trap Weight"
    range_start = 0
    range_end = 100
    default = 1

"""
scp_options: Dict[str, type(Option)] = {
    # split jump move rando
    "cat_rando": CatsRandomized,
    "local_cats": LocalCats,
    "strange_cat_rando": StrangeCatsRandomized,
    "extra_walls": ExtraWalls,
    "hidden_costume_rando": HiddenCostumesRandomized,
    "ending_required": EndingRequired,
    "include_final_stage": FinalStage,
    "cat_hunt_enabled": CatHuntEnabled,
    "cat_hunt_target": CatHuntTarget,
    "easy_wind": EasyWind,
    "death_link": DeathLink,
    "death_link_amnesty": DeathLinkAmnesty,
    "costume_weight": CostumeWeight,
    "ogmo_trap": OgmoTrap,
    "darkness_trap": DarknessTrap,
    "crow_trap": CrowTrap,
    
}
"""
scp_option_groups = [
    OptionGroup("Filler Weights", [
        CostumeWeight,
        OgmoTrap,
        DarknessTrap,
        CrowTrap
    ]),
]

@dataclass
class SuperCatPlanetOptions(PerGameCommonOptions):
    # split jump move rando
    cat_rando: CatsRandomized
    local_cats: LocalCats
    strange_cat_rando: StrangeCatsRandomized
    extra_walls: ExtraWalls
    hidden_costume_rando: HiddenCostumesRandomized
    ending_required: EndingRequired
    include_final_stage: FinalStage
    cat_hunt_enabled: CatHuntEnabled
    cat_hunt_target: CatHuntTarget
    easy_wind: EasyWind
    death_link: DeathLink
    death_link_amnesty: DeathLinkAmnesty
    costume_weight: CostumeWeight
    ogmo_trap: OgmoTrap
    darkness_trap: DarknessTrap
    crow_trap: CrowTrap
