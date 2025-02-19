from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region, Entrance
from .Locations import SCPLocation, location_table, cat_location_table, strange_cat_location_table, costume_location_table, hidden_costume_location_table, get_locations_by_category
from .Options import SuperCatPlanetOptions, scp_options

class SCPRegionData(NamedTuple):
	locations: Optional[List[str]]
	region_exits: Optional[List[str]]

def create_regions(multiworld: MultiWorld, player: int):

	if(getattr(multiworld.worlds[player].options, "cat_rando")):
		location_table.update(cat_location_table)
	if(getattr(multiworld.worlds[player].options, "strange_cat_rando")):
		location_table.update(strange_cat_location_table)
	if(getattr(multiworld.worlds[player].options, "hidden_costume_rando")):
		location_table.update(hidden_costume_location_table)
	
	scpareas = ["Village", "Canyon", "Jungle", "Factory", "Mushrooms_outside", "Mushrooms", "Lava Caves", "Ice Caves", "Flowers", "Crows_intro", "Crows", "Warp Room", "Void", "Final"]
	
	regMenu = Region("Menu", player, multiworld)
	multiworld.regions.append(regMenu)

	regVillage = Region("Village", player, multiworld)
	villageLocNames = list(filter(lambda x: "Village - " in x, location_table))
	if(getattr(multiworld.worlds[player].options, "cat_rando")):
		villageLocNames.append('Cat [Dye Shop]')
	regVillage.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regVillage) for loc_name in villageLocNames]
	multiworld.regions.append(regVillage)

	regCanyon = Region("Canyon", player, multiworld)
	canyonLocNames = list(filter(lambda x: "Canyon - " in x, location_table))
	if(getattr(multiworld.worlds[player].options, "cat_rando")):
		canyonLocNames.append('Cat [Dress Shop]')
	canyonLocNames.append('Orange Switch')
	regCanyon.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regCanyon) for loc_name in canyonLocNames]
	multiworld.regions.append(regCanyon)

	regJungle = Region("Jungle", player, multiworld)
	jungleLocNames = list(filter(lambda x: "Jungle - " in x, location_table))
	jungleLocNames.append('Green Switch')
	regJungle.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regJungle) for loc_name in jungleLocNames]
	multiworld.regions.append(regJungle)

	regFactory = Region("Factory", player, multiworld)
	factoryLocNames = list(filter(lambda x: "Factory - " in x, location_table))
	factoryLocNames.append('Blue Switch')
	regFactory.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regFactory) for loc_name in factoryLocNames]
	multiworld.regions.append(regFactory)

	regOutsideMush = Region("Mushrooms_outside", player, multiworld)
	outmushLocNames = []
	if(getattr(multiworld.worlds[player].options, "cat_rando")):
		outmushLocNames.append("Cat [Lava Caves - Entrance from Factory]")
	regOutsideMush.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regOutsideMush) for loc_name in outmushLocNames]
	multiworld.regions.append(regOutsideMush)

	regMushrooms = Region("Mushrooms", player, multiworld)
	mushroomsLocNames = [ "Purple Switch" ]
	if(getattr(multiworld.worlds[player].options, "cat_rando")):
		mushroomsLocNames.append('Cat [Wings Shop]')
	if(getattr(multiworld.worlds[player].options, "hidden_costume_rando")):
		mushroomsLocNames.append('Hidden Costume [Mushrooms - Left of Save]')
	regMushrooms.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regMushrooms) for loc_name in mushroomsLocNames]
	multiworld.regions.append(regMushrooms)

	regLava = Region("Lava Caves", player, multiworld)
	lavaLocNames = list(filter(lambda x: "Lava Caves - " in x, location_table))
	lavaLocNames.extend(['Right Yellow Switch', 'Left Yellow Switch'])
	lavaLocNames.remove("Cat [Lava Caves - Entrance from Factory]")
	regLava.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regLava) for loc_name in lavaLocNames]
	multiworld.regions.append(regLava)

	regIce = Region("Ice Caves", player, multiworld)
	iceLocNames = list(filter(lambda x: "Ice Caves - " in x, location_table))
	iceLocNames.append('White Switch')
	regIce.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regIce) for loc_name in iceLocNames]
	multiworld.regions.append(regIce)

	regFlowers = Region("Flowers", player, multiworld)
	flowersLocNames = list(filter(lambda x: "Flowers - " in x, location_table))
	if(getattr(multiworld.worlds[player].options, "cat_rando")):
		flowersLocNames.append('Cat [Hat Shop]')
	flowersLocNames.append('Red Switch')
	regFlowers.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regFlowers) for loc_name in flowersLocNames]
	multiworld.regions.append(regFlowers)

	regCrowsIntro = Region("Crows_intro", player, multiworld)
	multiworld.regions.append(regCrowsIntro)

	regCrows = Region("Crows", player, multiworld)
	crowsLocNames = list(filter(lambda x: "Crows - " in x, location_table))
	regCrows.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regCrows) for loc_name in crowsLocNames]
	multiworld.regions.append(regCrows)

	regWarpRoom = Region("Warp Room", player, multiworld)
	if(getattr(multiworld.worlds[player].options, "strange_cat_rando")):
		warproomLocNames = ["Strange Cat [Warp Room - Not Over Yet]"]
	regWarpRoom.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regWarpRoom) for loc_name in warproomLocNames]
	multiworld.regions.append(regWarpRoom)

	regVoid = Region("Void", player, multiworld)
	voidLocNames = list(filter(lambda x: "Void - " in x, location_table))
	regVoid.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regVoid) for loc_name in voidLocNames]
	multiworld.regions.append(regVoid)

	regFinal = Region("Final", player, multiworld)
	finalLocNames = list(filter(lambda x: "Final - " in x, location_table))
	finalLocNames.extend(['Pastry Basket', 'Star'])
	if(getattr(multiworld.worlds[player].options, "include_final_stage")):
		regFinal.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regFinal) for loc_name in finalLocNames]
	multiworld.regions.append(regFinal)

def create_region(multiworld: MultiWorld, player: int, name: str, data: SCPRegionData):
	region = Region(name, player, multiworld)
	if data.locations:
		for loc_name in data.locations:
			loc_data = location_table.get(loc_name)
			location = SCPLocation(player, loc_name, loc_data.code if loc_data else None, region)
			region.locations.append(location)

	return region

def connect_regions(multiworld: MultiWorld, player: int, source: str, target: str, rule=None, twoway=False):
	sourceRegion = multiworld.get_region(source, player)
	targetRegion = multiworld.get_region(target, player)
	sourceRegion.connect(targetRegion, rule=rule)
	if twoway:
		targetRegion.connect(sourceRegion, rule=rule)
