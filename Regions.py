from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region, Entrance
from .Locations import SCPLocation, location_table, cat_location_table, strange_cat_location_table, costume_location_table, get_locations_by_category
from .options import SuperCatPlanetOptions, scp_options

class SCPRegionData(NamedTuple):
	locations: Optional[List[str]]
	region_exits: Optional[List[str]]

def create_regions(world: MultiWorld, player: int):

	if(world.option_definitions.cat_rando.value):
		locations.update(cat_location_table)
	if(world.option_definitions.strange_cat_rando.value):
		locations.update(strange_cat_location_table)
	if(world.option_definitions.costume_rando.value):
		locations.update(costume_location_table)
	
	scpareas = ["Village", "Canyon", "Jungle", "Factory", "Mushrooms", "Lava Caves", "Ice Caves", "Flowers", "Crows", "Warp Room", "Void", "Final"]
	
	regMenu = Region("Menu", player, world)
	world.regions.append(regMenu)

	regVillage = Region("Village", player, world)
	villageLocNames = list(filter(lambda x: "Village - " in x, location_table))
	villageLocNames.append('Cat [Dye Shop]')
	regVillage.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regVillage) for loc_name in villageLocNames]
	world.regions.append(regVillage)

	regCanyon = Region("Canyon", player, world)
	canyonLocNames = list(filter(lambda x: "Canyon - " in x, location_table))
	canyonLocNames.extend(['Cat [Dress Shop]', 'Orange Switch'])
	regCanyon.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regCanyon) for loc_name in canyonLocNames]
	world.regions.append(regCanyon)

	regJungle = Region("Jungle", player, world)
	jungleLocNames = list(filter(lambda x: "Jungle - " in x, location_table))
	jungleLocNames.append('Green Switch')
	regJungle.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regJungle) for loc_name in jungleLocNames]
	world.regions.append(regJungle)

	regFactory = Region("Factory", player, world)
	factoryLocNames = list(filter(lambda x: "Factory - " in x, location_table))
	factoryLocNames.append('Blue Switch')
	regFactory.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regFactory) for loc_name in factoryLocNames]
	world.regions.append(regFactory)

	regMushrooms = Region("Mushrooms", player, world)
	mushroomsLocNames = [	
		"Cat [Wings Shop]",
		"Hidden Costume [Mushrooms - Left of Save]",
		"Purple Switch"
						]
	regMushrooms.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regMushrooms) for loc_name in mushroomsLocNames]
	world.regions.append(regMushrooms)

	regLava = Region("Lava Caves", player, world)
	lavaLocNames = list(filter(lambda x: "Lava Caves - " in x, location_table))
	lavaLocNames.extend(['Right Yellow Switch', 'Left Yellow Switch'])
	regLava.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regLava) for loc_name in lavaLocNames]
	world.regions.append(regLava)

	regIce = Region("Ice Caves", player, world)
	iceLocNames = list(filter(lambda x: "Ice Caves - " in x, location_table))
	iceLocNames.append('White Switch')
	regIce.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regIce) for loc_name in iceLocNames]
	world.regions.append(regIce)

	regFlowers = Region("Flowers", player, world)
	flowersLocNames = list(filter(lambda x: "Flowers - " in x, location_table))
	flowersLocNames.extend(['Cat [Hat Shop]', 'Red Switch'])
	regFlowers.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regFlowers) for loc_name in flowersLocNames]
	world.regions.append(regFlowers)

	regCrows = Region("Crows", player, world)
	crowsLocNames = list(filter(lambda x: "Crows - " in x, location_table))
	regCrows.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regCrows) for loc_name in crowsLocNames]
	world.regions.append(regCrows)

	regWarpRoom = Region("Warp Room", player, world)
	warproomLocNames = ["Strange Cat [Warp Room - Not Over Yet]"]
	regWarpRoom.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regWarpRoom) for loc_name in warproomLocNames]
	world.regions.append(regWarpRoom)

	regVoid = Region("Void", player, world)
	voidLocNames = list(filter(lambda x: "Void - " in x, location_table))
	regVoid.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regVoid) for loc_name in voidLocNames]
	world.regions.append(regVoid)

	regFinal = Region("Final", player, world)
	finalLocNames = list(filter(lambda x: "Final - " in x, location_table))
	finalLocNames.extend(['Pastry Basket', 'Star'])
	if(world.option_definitions.include_final_stage):
		regFinal.locations += [SCPLocation(player, loc_name, location_table[loc_name].address, regFinal) for loc_name in finalLocNames]
	world.regions.append(regFinal)

def create_region(world: MultiWorld, player: int, name: str, data: SCPRegionData):
	region = Region(name, player, world)
	if data.locations:
		for loc_name in data.locations:
			loc_data = location_table.get(loc_name)
			location = SCPLocation(player, loc_name, loc_data.code if loc_data else None, region)
			region.locations.append(location)

	return region

def connect_regions(world: MultiWorld, player: int, source: str, target: str, rule=None):
    sourceRegion = world.get_region(source, player)
    targetRegion = world.get_region(target, player)
    sourceRegion.connect(targetRegion, rule=rule)