from typing import Dict, NamedTuple, Optional

from BaseClasses import Location

class SCPLocation(Location):
	game: str = "Super Cat Planet"

class SCPLocationData(NamedTuple):
	category: str
	address: Optional[int] = None

def get_locations_by_category(category: str) -> Dict[str, SCPLocationData]:
	location_dict: Dict[str, SCPLocationData] = {}
	for name, data in location_table.items():
		if data.category == category:
			location_dict.setdefault(name, data)

	return location_dict

location_table: Dict[str, SCPLocationData] = {
	"Orange Switch":		SCPLocationData("Switch",   255049),
	"Green Switch":			SCPLocationData("Switch",   255066),
	"Blue Switch":			SCPLocationData("Switch",   255100),
	"Purple Switch":		SCPLocationData("Switch",   255106),
	"Left Yellow Switch":	SCPLocationData("Switch",   255120),
	"Right Yellow Switch":	SCPLocationData("Switch",   255128),
	"White Switch":			SCPLocationData("Switch",   255158),
	"Red Switch":			SCPLocationData("Switch",   255166),

	"Pastry Basket":		SCPLocationData("Miscellaneous",   255199),
	"Star":					SCPLocationData("Miscellaneous",   255201),
}

cat_location_table: Dict[str, SCPLocationData] = {

	# Village
	"Cat [Village - Benches]":					SCPLocationData("Cat",   255000),
	"Cat [Village - Picnic Top]":				SCPLocationData("Cat",   255001),
	"Cat [Village - Picnic Bottom]":			SCPLocationData("Cat",   255002),
	"Cat [Village - New Cat Village Top]":		SCPLocationData("Cat",   255003),
	"Cat [Village - New Cat Village Bottom]":	SCPLocationData("Cat",   255004),
	"Cat [Village - House 1]":					SCPLocationData("Cat",   255005),
	"Cat [Village - House 2]":					SCPLocationData("Cat",   255006),
	"Cat [Village - House Hidden]":				SCPLocationData("Cat",   255007),
	"Cat [Village - Hangout 1]":				SCPLocationData("Cat",   255008),
	"Cat [Village - Hangout 2]":				SCPLocationData("Cat",   255009),
	"Cat [Village - Hangout 3]":				SCPLocationData("Cat",   255010),
	"Cat [Village - Above Hangout]":			SCPLocationData("Cat",   255011),
	"Cat [Dye Shop]":							SCPLocationData("Cat",   255012),
	"Cat [Village - Pastry Preorder]":			SCPLocationData("Cat",   255013),
	"Cat [Village - Right of Pit]":				SCPLocationData("Cat",   255014),
	"Cat [Village - Pit]":						SCPLocationData("Cat",   255016),
	"Cat [Village - Crossroads]":				SCPLocationData("Cat",   255017),
	"Cat [Village - Outside Canyon]":			SCPLocationData("Cat",   255019),

	# Canyon
	"Cat [Canyon - Entrance 1]":				SCPLocationData("Cat",   255020),
	"Cat [Canyon - Entrance 2]":				SCPLocationData("Cat",   255021),
	"Cat [Canyon - Entrance 3]":				SCPLocationData("Cat",   255022),
	"Cat [Canyon - Pat Clanet 1]":				SCPLocationData("Cat",   255023),
	"Cat [Canyon - Pat Clanet 2]":				SCPLocationData("Cat",   255024),
	"Cat [Canyon - Floating Island]":			SCPLocationData("Cat",   255025),
	"Cat [Canyon - Floating Island Party 1]":	SCPLocationData("Cat",   255026),
	"Cat [Canyon - Floating Island Party 2]":	SCPLocationData("Cat",   255027),
	"Cat [Canyon - Floating Island Party 3]":	SCPLocationData("Cat",   255028),
	"Cat [Canyon - Hot]":						SCPLocationData("Cat",   255029),
	"Cat [Canyon - Cool]":						SCPLocationData("Cat",   255030),
	"Cat [Canyon - Above Hot and Cool]":		SCPLocationData("Cat",   255031),
	"Cat [Canyon - Top Plateau 1]":				SCPLocationData("Cat",   255032),
	"Cat [Canyon - Top Plateau 2]":				SCPLocationData("Cat",   255033),
	"Cat [Canyon - Top Plateau 3]":				SCPLocationData("Cat",   255034),
	"Cat [Canyon - Turnip]":					SCPLocationData("Cat",   255035),
	"Cat [Canyon - Outside Maze]":				SCPLocationData("Cat",   255036),
	"Cat [Canyon - Maze]":						SCPLocationData("Cat",   255037),
	"Cat [Canyon - Maze Success 1]":			SCPLocationData("Cat",   255038),
	"Cat [Canyon - Maze Success 2]":			SCPLocationData("Cat",   255039),
	"Cat [Canyon - Above Maze]":				SCPLocationData("Cat",   255040),
	"Cat [Dress Shop]":							SCPLocationData("Cat",   255041),
	"Cat [Canyon - Before Danger]":				SCPLocationData("Cat",   255043),
	"Cat [Canyon - Danger 1]":					SCPLocationData("Cat",   255044),
	"Cat [Canyon - Danger 2]":					SCPLocationData("Cat",   255045),
	"Cat [Canyon - Danger 3]":					SCPLocationData("Cat",   255046),
	"Cat [Canyon - Past Danger]":				SCPLocationData("Cat",   255203),
	"Cat [Canyon - Orange Switch 1]":			SCPLocationData("Cat",   255047),
	"Cat [Canyon - Orange Switch 2]":			SCPLocationData("Cat",   255048),

	# Jungle
	"Cat [Jungle - Crossroads 1]":				SCPLocationData("Cat",   255050),
	"Cat [Jungle - Crossroads 2]":				SCPLocationData("Cat",   255051),
	"Cat [Jungle - Left of Crossroads]":		SCPLocationData("Cat",   255052),
	"Cat [Jungle - Confusing]":					SCPLocationData("Cat",   255053),
	"Cat [Jungle - Thorn Tunnel]":				SCPLocationData("Cat",   255202),
	"Cat [Jungle - Canfuzling]":				SCPLocationData("Cat",   255055),
	"Cat [Jungle - Hidey Hole]":				SCPLocationData("Cat",   255056),
	"Cat [Jungle - Outside Factory]":			SCPLocationData("Cat",   255057),
	"Cat [Jungle - Right of Crossroads 1]":		SCPLocationData("Cat",   255058),
	"Cat [Jungle - Right of Crossroads 2]":		SCPLocationData("Cat",   255059),
	"Cat [Jungle - Funkatronic 1]":				SCPLocationData("Cat",   255060),
	"Cat [Jungle - Funkatronic 2]":				SCPLocationData("Cat",   255061),
	"Cat [Jungle - Secret Clubhouse 1]":		SCPLocationData("Cat",   255062),
	"Cat [Jungle - Secret Clubhouse 2]":		SCPLocationData("Cat",   255063),
	"Cat [Jungle - Secret Clubhouse 3]":		SCPLocationData("Cat",   255064),
	"Cat [Jungle - Path Past Clubhouse 1]":		SCPLocationData("Cat",   255067),
	"Cat [Jungle - Path Past Clubhouse 2]":		SCPLocationData("Cat",   255068),
	"Cat [Jungle - Thorns Above Lava Caves 1]":	SCPLocationData("Cat",   255069),
	"Cat [Jungle - Thorns Above Lava Caves 2]":	SCPLocationData("Cat",   255070),
	"Cat [Jungle - Above Lava Caves 1]":		SCPLocationData("Cat",   255071),
	"Cat [Jungle - Above Lava Caves 2]":		SCPLocationData("Cat",   255072),
	"Cat [Jungle - Above Lava Caves 3]":		SCPLocationData("Cat",   255073),
	"Cat [Jungle - Above Lava Caves 4]":		SCPLocationData("Cat",   255074),

	# Factory
	"Cat [Factory - Entrance 1]":				SCPLocationData("Cat",   255075),
	"Cat [Factory - Entrance 2]":				SCPLocationData("Cat",   255076),
	"Cat [Factory - Entrance 3]":				SCPLocationData("Cat",   255077),
	"Cat [Factory - Entrance 4]":				SCPLocationData("Cat",   255078),
	"Cat [Factory - Entrance 5]":				SCPLocationData("Cat",   255079),
	"Cat [Factory - Entrance 6]":				SCPLocationData("Cat",   255080),
	"Cat [Factory - Entrance 7]":				SCPLocationData("Cat",   255081),
	"Cat [Factory - Welcome]":					SCPLocationData("Cat",   255082),
	"Cat [Factory - Saws Right Side]":			SCPLocationData("Cat",   255083),
	"Cat [Factory - Saws Left Side Top]":		SCPLocationData("Cat",   255084),
	"Cat [Factory - Saws Left Side Bottom]":	SCPLocationData("Cat",   255085),
	"Cat [Factory - Above Crossroads]":			SCPLocationData("Cat",   255086),
	"Cat [Factory - Still Floating]":			SCPLocationData("Cat",   255087),
	"Cat [Factory - Old Switch]":				SCPLocationData("Cat",   255088),
	"Cat [Factory - Cool]":						SCPLocationData("Cat",   255090),
	"Cat [Factory - Okay]":						SCPLocationData("Cat",   255091),
	"Cat [Factory - Pistons 1]":				SCPLocationData("Cat",   255093),
	"Cat [Factory - Pistons 2]":				SCPLocationData("Cat",   255094),
	"Cat [Factory - Pistons 3]":				SCPLocationData("Cat",   255095),
	"Cat [Factory - Crossroads]":				SCPLocationData("Cat",   255096),
	"Cat [Factory - Crossroads Binary]":		SCPLocationData("Cat",   255097),
	"Cat [Factory - Blue Switch 1]":			SCPLocationData("Cat",   255098),
	"Cat [Factory - Blue Switch 2]":			SCPLocationData("Cat",   255099),
	"Cat [Factory - Complex 1]":				SCPLocationData("Cat",   255101),
	"Cat [Factory - Complex 2]":				SCPLocationData("Cat",   255102),

	# Mushrooms
	"Cat [Wings Shop]":							SCPLocationData("Cat",   255104),

	# Lava Caves
	"Cat [Lava Caves - Entrance from Factory]":	SCPLocationData("Cat",   255107),
	"Cat [Lava Caves - Lava Hotel 1]":			SCPLocationData("Cat",   255108),
	"Cat [Lava Caves - Lava Hotel 2]":			SCPLocationData("Cat",   255109),
	"Cat [Lava Caves - Lava Hotel 3]":			SCPLocationData("Cat",   255110),
	"Cat [Lava Caves - Lava Hotel 4]":			SCPLocationData("Cat",   255111),
	"Cat [Lava Caves - Left Path 1]":			SCPLocationData("Cat",   255112),
	"Cat [Lava Caves - Left Path 2]":			SCPLocationData("Cat",   255113),
	"Cat [Lava Caves - Left Path 3]":			SCPLocationData("Cat",   255115),
	"Cat [Lava Caves - Left Path 4]":			SCPLocationData("Cat",   255116),
	"Cat [Lava Caves - Left Path 5]":			SCPLocationData("Cat",   255117),
	"Cat [Lava Caves - Left Switch 1]":			SCPLocationData("Cat",   255118),
	"Cat [Lava Caves - Left Switch 2]":			SCPLocationData("Cat",   255119),
	"Cat [Lava Caves - Lava Bubbles]":			SCPLocationData("Cat",   255121),
	"Cat [Lava Caves - Convection]":			SCPLocationData("Cat",   255122),
	"Cat [Lava Caves - Above Right Path]":		SCPLocationData("Cat",   255123),
	"Cat [Lava Caves - Right Path]":			SCPLocationData("Cat",   255124),
	"Cat [Lava Caves - Right Path Clock]":		SCPLocationData("Cat",   255125),
	"Cat [Lava Caves - Right Switch 1]":		SCPLocationData("Cat",   255126),
	"Cat [Lava Caves - Right Switch 2]":		SCPLocationData("Cat",   255127),
	"Cat [Lava Caves - By Old Gate]":			SCPLocationData("Cat",   255129),

	# Ice Caves
	"Cat [Ice Caves - By Crows]":				SCPLocationData("Cat",   255130),
	"Cat [Ice Caves - Waterfall]":				SCPLocationData("Cat",   255131),
	"Cat [Ice Caves - Lake]":					SCPLocationData("Cat",   255132),
	"Cat [Ice Caves - Above Lake]":				SCPLocationData("Cat",   255134),
	"Cat [Ice Caves - Below Switch Path]":		SCPLocationData("Cat",   255136),
	"Cat [Ice Caves - Whirling]":				SCPLocationData("Cat",   255137),
	"Cat [Ice Caves - Swirling]":				SCPLocationData("Cat",   255138),
	"Cat [Ice Caves - Entrance from Flowers]":	SCPLocationData("Cat",   255139),
	"Cat [Ice Caves - Wind near Flowers 1]":	SCPLocationData("Cat",   255140),
	"Cat [Ice Caves - Wind near Flowers 2]":	SCPLocationData("Cat",   255141),
	"Cat [Ice Caves - Above Japanese]":			SCPLocationData("Cat",   255142),
	"Cat [Ice Caves - Japanese]":				SCPLocationData("Cat",   255143),
	"Cat [Ice Caves - Before Switch Path]":		SCPLocationData("Cat",   255144),
	"Cat [Ice Caves - Mash]":					SCPLocationData("Cat",   255145),
	"Cat [Ice Caves - Switch Path 1]":			SCPLocationData("Cat",   255147),
	"Cat [Ice Caves - Switch Path 2]":			SCPLocationData("Cat",   255148),
	"Cat [Ice Caves - Switch Path 3]":			SCPLocationData("Cat",   255149),
	"Cat [Ice Caves - Switch Path 4]":			SCPLocationData("Cat",   255150),
	"Cat [Ice Caves - Switch Path 5]":			SCPLocationData("Cat",   255151),
	"Cat [Ice Caves - Switch Path 6]":			SCPLocationData("Cat",   255152),
	"Cat [Ice Caves - Switch Path 7]":			SCPLocationData("Cat",   255153),
	"Cat [Ice Caves - Switch Path 8]":			SCPLocationData("Cat",   255155),
	"Cat [Ice Caves - White Switch 1]":			SCPLocationData("Cat",   255156),
	"Cat [Ice Caves - White Switch 2]":			SCPLocationData("Cat",   255157),

	# FLowers
	"Cat [Hat Shop]":							SCPLocationData("Cat",   255159),
	"Cat [Flowers - Switch Path 1]":			SCPLocationData("Cat",   255160),
	"Cat [Flowers - Switch Path 2]":			SCPLocationData("Cat",   255161),
	"Cat [Flowers - Switch Path 3]":			SCPLocationData("Cat",   255163),
	"Cat [Flowers - Red Switch 1]":				SCPLocationData("Cat",   255164),
	"Cat [Flowers - Red Switch 2]":				SCPLocationData("Cat",   255165),
	"Cat [Flowers - Above Switch]":				SCPLocationData("Cat",   255168),
	"Cat [Flowers - Pink Lake]":				SCPLocationData("Cat",   255169),
	"Cat [Flowers - Above Switch Path 1]":		SCPLocationData("Cat",   255171),
	"Cat [Flowers - Above Switch Path 2]":		SCPLocationData("Cat",   255172),
	"Cat [Flowers - Above Switch Path 3]":		SCPLocationData("Cat",   255173),
	"Cat [Flowers - Cozy]":						SCPLocationData("Cat",   255174),
	"Cat [Flowers - Guard 1]":					SCPLocationData("Cat",   255175),
	"Cat [Flowers - Guard 2]":					SCPLocationData("Cat",   255176),
	"Cat [Flowers - Below Guards]":				SCPLocationData("Cat",   255177),
	"Cat [Flowers - Entrance from Canyon 1]":	SCPLocationData("Cat",   255178),
	"Cat [Flowers - Entrance from Canyon 2]":	SCPLocationData("Cat",   255179),
	"Cat [Flowers - Tree 1]":					SCPLocationData("Cat",   255180),
	"Cat [Flowers - Tree 2]":					SCPLocationData("Cat",   255181),

	# Crows
	"Cat [Crows - Entrance]":					SCPLocationData("Cat",   255182),
	"Cat [Crows - Watch Out]":					SCPLocationData("Cat",   255183),
	"Cat [Crows - Tricky]":						SCPLocationData("Cat",   255184),
	"Cat [Crows - Never Give Up]":				SCPLocationData("Cat",   255186),
	"Cat [Crows - Talkative]":					SCPLocationData("Cat",   255187),
	"Cat [Crows - Cheese]":						SCPLocationData("Cat",   255188),
	"Cat [Crows - Switches]":					SCPLocationData("Cat",   255189),
	"Cat [Crows - Lake]":						SCPLocationData("Cat",   255190),
	"Cat [Crows - Almost There]":				SCPLocationData("Cat",   255191),
	"Cat [Crows - Believe]":					SCPLocationData("Cat",   255192),
	#cat [crows - real] {not sure if this can be a check}

	# Final Stage
	"Cat [Final - Pastries]":					SCPLocationData("Cat",   255198),


}

strange_cat_location_table: Dict[str, SCPLocationData] = {
	"Strange Cat [Village - All the Way Out Here]":	SCPLocationData("Strange Cat",   255015),
	"Strange Cat [Village - Outside Jungle]":		SCPLocationData("Strange Cat",   255018),
	"Strange Cat [Canyon - Enjoying the View]":		SCPLocationData("Strange Cat",   255042),
	"Strange Cat [Jungle - Solitude]":				SCPLocationData("Strange Cat",   255054),
	"Strange Cat [Factory - Complicated]":			SCPLocationData("Strange Cat",   255092),
	"Strange Cat [Lava Caves - Costume Rater]":		SCPLocationData("Strange Cat",   255114),
	"Strange Cat [Ice Caves - Privacy]":			SCPLocationData("Strange Cat",   255133),
	"Strange Cat [Ice Caves - Mash Harder]":		SCPLocationData("Strange Cat",   255146),
	"Strange Cat [Ice Caves - Antisocial]":			SCPLocationData("Strange Cat",   255154),
	"Strange Cat [Flowers - In the Plants]":		SCPLocationData("Strange Cat",   255162),
	"Strange Cat [Flowers - Petals]":				SCPLocationData("Strange Cat",   255170),
	"Strange Cat [Crows - Hiding Spot]":			SCPLocationData("Strange Cat",   255185),
	"Strange Cat [Warp Room - Not Over Yet]":		SCPLocationData("Strange Cat",   255193),
	"Strange Cat [Void - Trespassing]":				SCPLocationData("Strange Cat",   255194),
	"Strange Cat [Void - Gone]":					SCPLocationData("Strange Cat",   255195),
	"Strange Cat [Void - Stay]":					SCPLocationData("Strange Cat",   255197),
	"Strange Cat [Final - Not Much Longer Now]":	SCPLocationData("Strange Cat",   255200),
}

"""
costume_location_table: Dict[str, SCPLocationData] = {
	"Dye [White - 0]": 			SCPLocationData("Costume", 255300),
	"Dye [Pink - 1]": 			SCPLocationData("Costume", 255300),
	"Dye [Salmon - 5]": 		SCPLocationData("Costume", 255300),
	"Dye [Indigo - 7]": 		SCPLocationData("Costume", 255300),
	"Dye [Chartreuse - 10]": 	SCPLocationData("Costume", 255300),
	"Dye [White - 15]": 		SCPLocationData("Costume", 255300),
	"Dye [White - 18]": 		SCPLocationData("Costume", 255300),
	"Dye [White - 21]": 		SCPLocationData("Costume", 255300),
	"Dye [White - 24]": 		SCPLocationData("Costume", 255300),
	"Dye [Black - ???]": 		SCPLocationData("Costume", 255300),
	"Dye [White - HAT]": 		SCPLocationData("Costume", 255300),
	"Dye [White - ALL]": 		SCPLocationData("Costume", 255300),
	"Dye [White - ALL]": 		SCPLocationData("Costume", 255300),
	"Dye [White - ALL]": 		SCPLocationData("Costume", 255300),

	"Dress [Plain - 0]": 			SCPLocationData("Costume", 255300),
	"Dress [Star - 10]": 			SCPLocationData("Costume", 255300),
	"Dress [Stripe - 15]": 			SCPLocationData("Costume", 255300),
	"Dress [Dots - 20]": 			SCPLocationData("Costume", 255300),
	"Dress [Trimmed Stripe - 25]": 	SCPLocationData("Costume", 255300),
	"Dress [Stripes - 30]":			SCPLocationData("Costume", 255300),
	"Dress [Vertical Stripe - 40]":	SCPLocationData("Costume", 255300),
	"Dress [Heart - 50]": 			SCPLocationData("Costume", 255300),
	"Dress [Trim - 60]": 			SCPLocationData("Costume", 255300),
	"Dress [Hem - 70]": 			SCPLocationData("Costume", 255300),
	"Dress [Black Trim - 80]":		SCPLocationData("Costume", 255300),

	"Hat [None - 0]": 				SCPLocationData("Costume", 255300),
	"Hat [Ears - 15]": 				SCPLocationData("Costume", 255300),
	"Hat [Big Ears - 30]": 			SCPLocationData("Costume", 255300),
	"Hat [Halo - 45]": 				SCPLocationData("Costume", 255300),
	"Hat [Sleepy Hat - 60]": 		SCPLocationData("Costume", 255300),
	"Hat [Scarf - 70]": 			SCPLocationData("Costume", 255300),
	"Hat [Headband - 75]": 			SCPLocationData("Costume", 255300),
	"Hat [Necklace - 90]": 			SCPLocationData("Costume", 255300),
	"Hat [Bow - 105]": 				SCPLocationData("Costume", 255300),
	"Hat [Shades - 120]": 			SCPLocationData("Costume", 255300),
	"Hat [Squid - 135]":	 		SCPLocationData("Costume", 255300),
	"Hat [Scarlet - 150]": 			SCPLocationData("Costume", 255300),

	"Wings [Angel - 0]": 			SCPLocationData("Costume", 255300),
	"Wings [Fly - 0]":	 			SCPLocationData("Costume", 255300),
	"Wings [Bat - 0]": 				SCPLocationData("Costume", 255300),
	"Wings [Moth - 0]": 			SCPLocationData("Costume", 255300),
	"Wings [Fairy - 0]":	 		SCPLocationData("Costume", 255300),
	"Wings [Gear - 0]":		 		SCPLocationData("Costume", 255300),
	"Wings [Propellor - 0]": 		SCPLocationData("Costume", 255300),
	"Wings [Jet - 0]": 				SCPLocationData("Costume", 255300),
	"Wings [Cirno - 0]": 			SCPLocationData("Costume", 255300),
	"Wings [Scarlet - 0]": 			SCPLocationData("Costume", 255300),
}
"""

hidden_costume_location_table: Dict[str, SCPLocationData] = {
	"Hidden Costume [Jungle - Secret Clubhouse Top]":	SCPLocationData("Hidden Costume",   255065),
	"Hidden Costume [Factory - Old Switch]":			SCPLocationData("Hidden Costume",   255089),
	"Hidden Costume [Factory - Complex]":				SCPLocationData("Hidden Costume",   255103),
	"Hidden Costume [Mushrooms - Left of Save]":		SCPLocationData("Hidden Costume",   255105),
	"Hidden Costume [Ice Caves - Behind Waterfall]":	SCPLocationData("Hidden Costume",   255135),
	"Hidden Costume [Flowers - Red Switch]":			SCPLocationData("Hidden Costume",   255167),
	"Hidden Costume [Void - Skull]":					SCPLocationData("Hidden Costume",   255196),
}

full_location_table: Dict[str, SCPLocationData] = {}

full_location_table.update(location_table)

full_location_table.update(cat_location_table)
full_location_table.update(strange_cat_location_table)
full_location_table.update(hidden_costume_location_table)

# event_location_table: Dict[str, SCPLocationData] = {}
# Also dont knwo what the fuck this is either mun ^^^
# i actually know what it does now but i like this comment so i'm leaving it :3