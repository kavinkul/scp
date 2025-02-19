from typing import Dict
from dataclasses import dataclass

from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionSet, PerGameCommonOptions

#class SplitJumps(Toggle):
#   """Starts the player with only one of the three jump heights."""
#   display_name = "Split Jumps"
#   default = False

class CatsRandomized(Toggle):
    """Includes Cats into randomization."""
    display_name = "Randomize Cats"
    default = True

class LocalCats(Range):
    """
    Forces some percent of Cat items to be found inside of your slot.
    Recommended to reduce flooding in the multiworld.
    """
    display_name = "Local Cat Percentage"
    range_start = 0
    range_end = 100
    default = 80

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
    "death_link": DeathLink,
}
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
    death_link: DeathLink
