from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification

class SCPItem(Item):
	game: str = "Super Cat Planet"

class SCPItemData(NamedTuple):
	category: str
	address: Optional[int] = None
	classification: ItemClassification = ItemClassification.filler
	max_quantity: int = 1
	weight: int = 1

def get_items_by_category(category: str) -> Dict[str, SCPItemData]:
	item_dict: Dict[str, SCPItemData] = {}
	for name, data in item_table.items():
		if data.category == category:
			item_dict.setdefault(name, data)

	return item_dict

item_table: Dict[str, SCPItemData] = {

	# Cats
	"Cat":				SCPItemData("Cats", 254000,ItemClassification.progression_skip_balancing,170),
	"Strange Cat":		SCPItemData("Cats", 254001,ItemClassification.progression_skip_balancing,17),

	# Switches
	"Red Switch":			SCPItemData("Switches", 254010,ItemClassification.progression),
	"Orange Switch":		SCPItemData("Switches", 254011,ItemClassification.progression),
	"Left Yellow Switch":	SCPItemData("Switches", 254012,ItemClassification.progression),
	"Right Yellow Switch":	SCPItemData("Switches", 254013,ItemClassification.progression),
	"Green Switch":			SCPItemData("Switches", 254014,ItemClassification.filler),
	"Blue Switch":			SCPItemData("Switches", 254015,ItemClassification.progression),
	"Purple Switch":		SCPItemData("Switches", 254016,ItemClassification.useful),
	"White Switch":			SCPItemData("Switches", 254017,ItemClassification.progression),

	# Misc
	"Pastry Basket": 	SCPItemData("Miscellaneous", 254020,ItemClassification.progression),

	# Junk

	"Costume": SCPItemData("Junk", 254030,ItemClassification.filler),

	# Traps

	"Plonker": SCPItemData("Traps", 254040,ItemClassification.trap),
	#"Death": SCPItemData("Traps", 254041,ItemClassification.trap),
	"Crow": SCPItemData("Traps", 254042,ItemClassification.trap),

}

# event_item_table: Dict[str, SCPItemData] = {}
# ^^^ idk what the fuck this means
