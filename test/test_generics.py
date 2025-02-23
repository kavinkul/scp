from . import SuperCatPlanetTestBase

class TestGenerics(SuperCatPlanetTestBase):
    options = {
        "cat_rando": True,
        "local_cats": False,
        "strange_cat_rando": True,
        "extra_walls": True,
        "hidden_costume_rando": False,
        "ending_required": 0,
        "include_final_stage": False,
        "cat_hunt_enabled": False,
        "cat_hunt_target": 150,
        "death_link": False,
    }

    def test_generics_all(self) -> None:
        self.test_all_state_can_reach_everything()
        self.test_empty_state_can_reach_something()
        #self.test_fill()