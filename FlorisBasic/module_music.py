#####Floris Notes#####
# I've used songs from the following sources:
# - Music from Rejenorst Sound Design: http://www.rejenorst.com/music/music.html
# - Native Warband v1.143 by TaleWorlds
# - Utrehd's Music Pack v0.8 by Utrehd and rejenorst
# - Warband Live Music v1.0 by CHUR
# - Warband Live Music Remixes by Rejenorst
######################
from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
##Floris: Almost everything in this file has been changed. All mp3's are from the mods, all ogg's are from native.

  ("bogus",								"cant_find_this.ogg",				0,																							0),

##Menu
#Minimal
  ("mount_and_blade_title_screen",		"min_menu.mp3",						mtf_module_track|mtf_sit_main_title|mtf_start_immediately,									0),															# 87,6 dB
#Extended
  ("mount_and_blade_title_screen_2",	"mount_and_blade_title_screen.ogg",	mtf_sit_main_title|mtf_start_immediately,													0),															# 87,4 dB
  ("mount_and_blade_title_screen_3",	"ext_menu.mp3",						mtf_module_track|mtf_sit_main_title|mtf_start_immediately,									0),															# 87,4 dB

##Ambushed
#Minimal
  ("ambushed_by_neutral",				"min_ambushed_by_neutral.mp3",		mtf_module_track|mtf_sit_ambushed|mtf_sit_siege,											mtf_sit_fight|mtf_sit_multiplayer_fight),					# 90,8 dB
  ("ambushed_by_swadian",				"min_ambushed_by_swadian.mp3",		mtf_module_track|mtf_culture_1|mtf_sit_ambushed|mtf_sit_siege,								mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 89,4 dB
  ("ambushed_by_vaegir",				"min_ambushed_by_vaegir.mp3",		mtf_module_track|mtf_culture_2|mtf_sit_ambushed|mtf_sit_siege,								mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 87,5 dB
  ("ambushed_by_khergit",				"min_ambushed_by_khergit.mp3",		mtf_module_track|mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege,								mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 86,3 dB
  ("ambushed_by_nord",					"min_ambushed_by_nord.mp3",			mtf_module_track|mtf_culture_4|mtf_sit_ambushed|mtf_sit_siege,								mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 87,5 dB
  ("ambushed_by_rhodok",				"min_ambushed_by_rhodok.mp3",		mtf_module_track|mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege,								mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 81,8 dB
  ("ambushed_by_sarranid",				"min_ambushed_by_sarranid.mp3",		mtf_module_track|mtf_culture_6|mtf_sit_ambushed|mtf_sit_siege,								mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 80,6 dB
#Extended
  ("ambushed_by_neutral_2",				"ambushed_by_neutral.ogg",			mtf_sit_ambushed|mtf_sit_siege,																mtf_sit_fight|mtf_sit_multiplayer_fight),					# 91,0 dB
  ("ambushed_by_swadian_2",				"ambushed_by_swadian.ogg",			mtf_culture_1|mtf_sit_ambushed|mtf_sit_siege,												mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 89,7 dB
  ("ambushed_by_swadian_3",				"ext_ambushed_by_swadian.mp3",		mtf_module_track|mtf_culture_1|mtf_sit_ambushed|mtf_sit_siege,								mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 89,7 dB
  ("ambushed_by_vaegir_2",				"ambushed_by_vaegir.ogg",			mtf_culture_2|mtf_sit_ambushed|mtf_sit_siege,												mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 86,9 dB
  ("ambushed_by_vaegir_3",				"ext_ambushed_by_vaegir.mp3",		mtf_module_track|mtf_culture_2|mtf_sit_ambushed|mtf_sit_siege,								mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 87,3 dB
  ("ambushed_by_khergit_2",				"ambushed_by_khergit.ogg",			mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege,												mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 85,8 dB
  ("ambushed_by_khergit_3",				"ext_ambushed_by_khergit.mp3",		mtf_module_track|mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege,								mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 85,1 dB
  ("ambushed_by_nord_2",				"ambushed_by_nord.ogg",				mtf_culture_4|mtf_sit_ambushed|mtf_sit_siege,												mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 88,0 dB
  ("ambushed_by_nord_3",				"ext_ambushed_by_nord.mp3",			mtf_module_track|mtf_culture_4|mtf_sit_ambushed|mtf_sit_siege,								mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 87,6 dB
  ("ambushed_by_rhodok_2",				"ambushed_by_rhodok.ogg",			mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege,												mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 81,4 dB
  ("ambushed_by_swadian_3",				"ext_ambushed_by_rhodok.mp3",		mtf_module_track|mtf_culture_1|mtf_sit_ambushed|mtf_sit_siege,								mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 81,8 dB
  ("ambushed_by_sarranid_2",			"middle_eastern_action.ogg",		mtf_culture_6|mtf_sit_ambushed|mtf_sit_siege,												mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 80,5 dB
  ("ambushed_by_sarranid_3",			"ext_ambushed_by_sarranid.mp3",		mtf_module_track|mtf_culture_4|mtf_sit_ambushed|mtf_sit_siege,								mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),	# 81,1 dB

##Arena Fights
#Minimal
  ("arena_1",							"min_arena_1.mp3",					mtf_module_track|mtf_sit_arena,																0),															# 89,8 dB
  ("arena_swadia",						"min_arena_swadia.mp3",				mtf_module_track|mtf_culture_1|mtf_sit_arena,												0),															# 90,6 dB
  ("arena_vaegir",						"min_arena_vaegir.mp3",				mtf_module_track|mtf_culture_2|mtf_sit_arena,												0),															# 90,3 dB
  ("arena_khergit",						"min_arena_khergit.mp3",			mtf_module_track|mtf_culture_3|mtf_sit_arena,												0),															# 90,6 dB
  ("arena_nord",						"min_arena_nord.mp3",				mtf_module_track|mtf_culture_4|mtf_sit_arena,												0),															# 90,9 dB
  ("arena_rhodok",						"min_arena_rhodok.mp3",				mtf_module_track|mtf_culture_5|mtf_sit_arena,												0),															# 91,1 dB
  ("arena_sarranid",					"min_arena_sarranid.mp3",			mtf_module_track|mtf_culture_6|mtf_sit_arena,												0),															# 90,5 dB
#Extended
  ("arena_2",							"arena_1.ogg",						mtf_sit_arena,																				0),															# 90,4 dB
  ("arena_3",							"ext_arena_3.mp3",					mtf_module_track|mtf_sit_arena,																0),															# 90,2 dB
  ("arena_4",							"ext_arena_4.mp3",					mtf_module_track|mtf_sit_arena,																0),															# 90,1 dB
  ("arena_5",							"ext_arena_5.mp3",					mtf_module_track|mtf_looping|mtf_sit_arena,													0),															# 90,5 dB

##Travelling
#Minimal
  ("armorer",							"min_travelling.mp3",				mtf_module_track|mtf_sit_travel,															0),															# 81,1 dB
#Extended
  ("armorer_2",							"armorer.ogg",						mtf_sit_travel,																				0),															# 80,8 dB

##Bandit Fights
#Minimal
  ("bandit_fight",						"min_bandit_fight.mp3",				mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,					0),															# 87,2 dB
#Extended
  ("bandit_fight_2",					"bandit_fight.ogg",					mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,									0),															# 87,7 dB
  ("bandit_fight_3",					"ext_bandit_fight_3.mp3",			mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,					0),															# 87,3 dB
  ("bandit_fight_4",					"ext_bandit_fight_4.mp3",			mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,					0),															# 87,5 dB

##Night
#Minimal
  ("calm_night_1",						"calm_night_2.ogg",					mtf_sit_night,																				mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),				# 80,7 dB

##Captured
#Minimal
  ("captured",							"min_captured.mp3",					mtf_module_track|mtf_persist_until_finished,												0),															# 86,5 dB
#Extended
  ("captured_2",						"capture.ogg",						mtf_persist_until_finished,																	0),															# 86,1 dB

##Killed
#Minimal
  ("defeated_by_neutral",				"min_defeated_by_neutral.mp3",		mtf_module_track|mtf_persist_until_finished|mtf_sit_killed,									0),															# 92,6 dB
#Extended
  ("defeated_by_neutral_2",				"defeated_by_neutral.ogg",			mtf_persist_until_finished|mtf_sit_killed,													0),															# 95,6 dB
  ("defeated_by_neutral_3",				"defeated_by_neutral_2.ogg",		mtf_persist_until_finished|mtf_sit_killed,													0),															# 92,8 dB
  ("defeated_by_neutral_4",				"defeated_by_neutral_3.ogg",		mtf_persist_until_finished|mtf_sit_killed,													0),															# 90,2 dB

##Looted Village
#Minimal
  ("empty_village",						"min_empty_village.mp3",			mtf_module_track|mtf_persist_until_finished,												0),															# 76,1 dB
  ("encounter_hostile_nords",			"encounter_hostile_nords.ogg",		mtf_persist_until_finished|mtf_sit_encounter_hostile,										0),															# 75,2 dB
  ("escape",							"escape.ogg",						mtf_persist_until_finished,																	0),															# dB
#Extended
  ("empty_village_2",					"empty_village.ogg",				mtf_persist_until_finished,																	0),															# 75,6 dB

##Fights
#Minimal
  ("fight_1",							"min_fight_1.mp3",					mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,					0),															# 92,3 dB
  ("fight_2",							"min_fight_2.mp3",					mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,					0),															# 92,3 dB
  ("fight_3",							"min_fight_3.mp3",					mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,					0),															# 91,0 dB
  ("fight_4",							"min_fight_4.mp3",					mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,					0),															# 92,3 dB
  ("fight_as_swadian",					"min_fight_as_swadian.mp3",			mtf_module_track|mtf_culture_1|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,	mtf_culture_all),											# 92,5 dB
  ("fight_as_vaegir",					"min_fight_as_vaegir.mp3",			mtf_module_track|mtf_culture_2|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,	mtf_culture_all),											# 90,2 dB
  ("fight_as_khergit",					"min_fight_as_khergit.mp3",			mtf_module_track|mtf_culture_3|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,	mtf_culture_all),											# 89,8 dB
  ("fight_as_nord",						"min_fight_as_nord.mp3",			mtf_module_track|mtf_culture_4|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,	mtf_culture_all),											# 92,7 dB
  ("fight_as_rhodok",					"min_fight_as_rhodok.mp3",			mtf_module_track|mtf_culture_5|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,	mtf_culture_all),											# 94,7 dB
  ("fight_as_sarranid",					"min_fight_as_sarranid.mp3",		mtf_module_track|mtf_culture_6|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,	mtf_culture_all),											# 92,2 dB
  ("fight_while_mounted_1",				"min_fight_while_mounted_1.mp3",	mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,					0),															# 91,1 dB
  ("fight_while_mounted_2",				"min_fight_while_mounted_2.mp3",	mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,					0),															# 91,2 dB
#Extended
  ("fight_5",							"fight_1.ogg",						mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,									0),															# 91,1 dB
  ("fight_6",							"fight_2.ogg",						mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,									0),															# 93,7 dB
  ("fight_7",							"fight_3.ogg",						mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,									0),															# 90,0 dB
  ("fight_8",							"percussion_battery.ogg",			mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,									0),  														# 89,5 dB
  ("fight_as_vaegir_2",					"fight_as_vaegir.ogg",				mtf_culture_2|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,						mtf_culture_all),											# 90,6 dB
  ("fight_as_khergit_2",				"fight_as_khergit.ogg",				mtf_culture_3|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,						mtf_culture_all),											# 89,1 dB
  ("fight_as_nord_2",					"fight_as_nord.ogg",				mtf_culture_4|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,						mtf_culture_all),											# 92,5 dB
  ("fight_as_rhodok_2",					"fight_as_rhodok.ogg",				mtf_culture_5|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,						mtf_culture_all),											# 95,6 dB
  ("fight_as_sarranid_2",				"ext_fight_as_sarranid.mp3",		mtf_module_track|mtf_culture_6|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,	mtf_culture_all),											# 91,9 dB
  ("fight_while_mounted_3",				"fight_while_mounted_1.ogg",		mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,									0),															# 88,3 dB
  ("fight_while_mounted_4",				"fight_while_mounted_2.ogg",		mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,									0),															# 92,9 dB
  ("fight_while_mounted_5",				"warband_action.ogg",				mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed,									0),															# 88,5 dB
 
##Infiltration
#Minimal
  ("infiltration_swadia",				"min_infiltration_swadia.mp3",		mtf_module_track|mtf_culture_1|mtf_sit_town_infiltrate,										mtf_culture_all),											# 74,6 dB
  ("infiltration_vaegir",				"min_infiltration_vaegir.mp3",		mtf_module_track|mtf_culture_2|mtf_sit_town_infiltrate,										mtf_culture_all),											# 75,7 dB
  ("infiltration_khergit",				"infiltration_khergit.ogg",			mtf_culture_3|mtf_sit_town_infiltrate,														mtf_culture_all),											# 74,5 dB
  ("infiltration_nord",					"min_infiltration_nord.mp3",		mtf_module_track|mtf_culture_4|mtf_sit_town_infiltrate,										mtf_culture_all),											# 75,7 dB
  ("infiltration_rhodok",				"min_infiltration_rhodok.mp3",		mtf_module_track|mtf_culture_5|mtf_sit_town_infiltrate,										mtf_culture_all),											# 74,7 dB
  ("infiltration_sarranid",				"min_infiltration_sarranid.mp3",	mtf_module_track|mtf_culture_6|mtf_sit_town_infiltrate,										mtf_culture_all),											# 74,9 dB

##Killed by...
#Minimal
  ("killed_by_neutral",					"min_killed_by_neutral.mp3",		mtf_module_track|mtf_persist_until_finished|mtf_sit_killed,									0),															# 85,5 dB
  ("killed_by_swadian",					"killed_by_swadian.ogg",			mtf_persist_until_finished|mtf_culture_1|mtf_sit_killed,									0),															# 87,1 dB
  ("killed_by_vaegir",					"min_killed_by_vaegir.mp3",			mtf_module_track|mtf_persist_until_finished|mtf_culture_2|mtf_sit_killed,					0),															# 86,7 dB
  ("killed_by_khergit",					"killed_by_khergit.ogg",			mtf_persist_until_finished|mtf_culture_3|mtf_sit_killed,									0),															# 85,0 dB
  ("killed_by_nord",					"min_killed_by_nord.mp3",			mtf_module_track|mtf_persist_until_finished|mtf_culture_4|mtf_sit_killed,					0),															# 85,8 dB
  ("killed_by_rhodok",					"min_killed_by_rhodok.mp3",			mtf_module_track|mtf_persist_until_finished|mtf_culture_5|mtf_sit_killed,					0),															# 85,5 dB
  ("killed_by_sarranid",				"min_killed_by_sarranid.mp3",		mtf_module_track|mtf_persist_until_finished|mtf_culture_6|mtf_sit_killed,					0),															# 85,6 dB

##Lords Hall
#Minimal
  ("lords_hall_swadian",				"lords_hall_swadian.ogg",			mtf_culture_1|mtf_sit_travel,																mtf_sit_town|mtf_sit_night|mtf_sit_tavern|mtf_culture_all),	# 80,3 dB
  ("lords_hall_vaegir",					"lords_hall_vaegir.ogg",			mtf_culture_2|mtf_sit_travel,																mtf_sit_town|mtf_sit_night|mtf_sit_tavern|mtf_culture_all),	# 70,7 dB
  ("lords_hall_khergit",				"lords_hall_khergit.ogg",			mtf_culture_3|mtf_sit_travel,																mtf_sit_town|mtf_sit_night|mtf_sit_tavern|mtf_culture_all),	# 87,4 dB
  ("lords_hall_nord",					"lords_hall_nord.ogg",				mtf_culture_4|mtf_sit_travel,																mtf_sit_town|mtf_sit_night|mtf_sit_tavern|mtf_culture_all),	# 81,3 dB
  ("lords_hall_rhodok",					"lords_hall_rhodok.ogg",			mtf_culture_5|mtf_sit_travel,																mtf_sit_town|mtf_sit_night|mtf_sit_tavern|mtf_culture_all),	# 78,7 dB
  ("lords_hall_sarranid",				"min_lords_hall_sarranid.mp3",		mtf_module_track|mtf_culture_6|mtf_sit_travel,												mtf_sit_town|mtf_sit_night|mtf_sit_tavern|mtf_culture_all),	# 80,1 dB

##Terrain
#Minimal
  ("mounted_snow_terrain_calm",			"mounted_snow_terrain_calm.ogg",	mtf_sit_travel,																				mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),	# 84,5 dB
  ("outdoor_beautiful_land",			"outdoor_beautiful_land.ogg",		mtf_sit_travel,																				mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),	# 80,1 dB
  ("terrain_1",							"min_terrain_1.mp3",				mtf_module_track|mtf_sit_travel,															mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),	# 82,4 dB
  ("terrain_2",							"min_terrain_2.mp3",				mtf_module_track|mtf_sit_travel,															mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),	# 82,4 dB
  ("neutral_infiltration",				"neutral_infiltration.ogg",			mtf_sit_town_infiltrate,																	0),															# 80,1 dB
  ("retreat",							"min_retreat.mp3",					mtf_module_track|mtf_persist_until_finished|mtf_sit_killed,									0),															# 92,9 dB
#Extended
  ("retreat_2",							"retreat.ogg",						mtf_persist_until_finished|mtf_sit_killed,													0),															# 93,2 dB

##Siege
#Minimal
  ("siege_neutral",						"min_siege_neutral.mp3",			mtf_module_track|mtf_sit_siege,																mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),	# 84,5 dB
  ("enter_the_juggernaut",				"enter_the_juggernaut.ogg",			mtf_sit_siege,																				mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),	# 91,5 dB
  ("siege_attempt",						"siege_attempt.ogg",				mtf_sit_siege,																				mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),	# 87,6 dB
  ("crazy_battle_music",				"crazy_battle_music.ogg",			mtf_sit_siege,																				mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),	# 91,0 dB
#Extended
  ("seige_neutral_2",					"seige_neutral.ogg",				mtf_sit_siege,																				mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),	# 84,5 dB

##Tavern
#Minimal
  ("tavern_1",							"min_tavern_1.mp3",					mtf_module_track|mtf_sit_tavern|mtf_sit_feast,												0),															# 74,6 dB
  ("tavern_2",							"min_tavern_2.mp3",					mtf_module_track|mtf_sit_tavern|mtf_sit_feast,												0),															# 75,3 dB
#Extended
  ("tavern_3",							"tavern_1.ogg",						mtf_sit_tavern|mtf_sit_feast,																0),															# 67,3 dB
  ("tavern_4",							"tavern_2.ogg",						mtf_sit_tavern|mtf_sit_feast,																0),															# 69,2 dB

##Towns
#Minimal
  ("town_neutral",						"town_neutral.ogg",					mtf_sit_town|mtf_sit_travel,																mtf_sit_tavern|mtf_sit_night),								# 74,9 dB
  ("town_swadian",						"town_swadian.ogg",					mtf_culture_1|mtf_sit_town|mtf_sit_travel,													mtf_sit_tavern|mtf_sit_night|mtf_culture_all),				# 78,7 dB
  ("town_vaegir",						"town_vaegir.ogg",					mtf_culture_2|mtf_sit_town|mtf_sit_travel,													mtf_sit_tavern|mtf_sit_night|mtf_culture_all),				# 66,4 dB
  ("town_khergit",						"town_khergit.ogg",					mtf_culture_3|mtf_sit_town|mtf_sit_travel,													mtf_sit_tavern|mtf_sit_night|mtf_culture_all),				# 76,8 dB
  ("town_nord",							"town_nord.ogg",					mtf_culture_4|mtf_sit_town|mtf_sit_travel,													mtf_sit_tavern|mtf_sit_night|mtf_culture_all),				# 73,7 dB
  ("town_rhodok",						"town_rhodok.ogg",					mtf_culture_5|mtf_sit_town|mtf_sit_travel,													mtf_sit_tavern|mtf_sit_night|mtf_culture_all),				# 73,7 dB
  ("town_sarranid",						"min_town_sarranid.mp3",			mtf_module_track|mtf_culture_6|mtf_sit_town|mtf_sit_travel,									mtf_sit_tavern|mtf_sit_night|mtf_culture_all),				# 75,6 dB

##Travel
#Minimal
  ("travel_neutral",					"min_travel_neutral.mp3",			mtf_module_track|mtf_sit_travel,															mtf_sit_town|mtf_sit_tavern|mtf_sit_night),					# 90,2 dB
  ("travel_swadian",					"min_travel_swadian.mp3",			mtf_module_track|mtf_culture_1|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 89,9 dB
  ("travel_vaegir",						"min_travel_vaegir.mp3",			mtf_module_track|mtf_culture_2|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 86,0 dB
  ("travel_khergit",					"min_travel_khergit.mp3",			mtf_module_track|mtf_culture_3|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 77,2 dB
  ("travel_nord",						"min_travel_nord.mp3",				mtf_module_track|mtf_culture_4|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 76,7 dB
  ("travel_rhodok",						"min_travel_rhodok.mp3",			mtf_module_track|mtf_culture_5|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 83,6 dB
  ("travel_sarranid",					"min_travel_sarranid.mp3",			mtf_module_track|mtf_culture_6|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 81,2 dB
#Extended
  ("travel_neutral_2",					"travel_neutral.ogg",				mtf_sit_travel,																				mtf_sit_town|mtf_sit_tavern|mtf_sit_night),					# 89,6 dB
  ("travel_neutral_3",					"ext_travel_neutral_3.mp3",			mtf_module_track|mtf_sit_travel,															mtf_sit_town|mtf_sit_tavern|mtf_sit_night),					# 90,0 dB
  ("travel_neutral_4",					"ext_travel_neutral_4.mp3",			mtf_module_track|mtf_sit_travel,															mtf_sit_town|mtf_sit_tavern|mtf_sit_night),					# 90,3 dB
  ("travel_neutral_5",					"ext_travel_neutral_5.mp3",			mtf_module_track|mtf_sit_travel,															mtf_sit_town|mtf_sit_tavern|mtf_sit_night),					# 89,9 dB
  ("travel_neutral_6",					"ext_travel_neutral_6.mp3",			mtf_module_track|mtf_sit_travel,															mtf_sit_town|mtf_sit_tavern|mtf_sit_night),					# 90,0 dB
  ("travel_neutral_7",					"ext_travel_neutral_7.mp3",			mtf_module_track|mtf_sit_travel,															mtf_sit_town|mtf_sit_tavern|mtf_sit_night),					# 89,1 dB
  ("travel_neutral_8",					"ext_travel_neutral_8.mp3",			mtf_module_track|mtf_sit_travel,															mtf_sit_town|mtf_sit_tavern|mtf_sit_night),					# 88,8 dB
  ("travel_neutral_9",					"ext_travel_neutral_9.mp3",			mtf_module_track|mtf_sit_travel,															mtf_sit_town|mtf_sit_tavern|mtf_sit_night),					# 90,1 dB
  ("travel_swadian_2",					"travel_swadian.ogg",				mtf_culture_1|mtf_sit_travel,																mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 89,2 dB
  ("travel_swadian_3",					"ext_travel_swadian_3.mp3",			mtf_module_track|mtf_culture_1|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 89,9 dB
  ("travel_swadian_4",					"ext_travel_swadian_4.mp3",			mtf_module_track|mtf_culture_1|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 88,8 dB
  ("travel_swadian_5",					"ext_travel_swadian_5.mp3",			mtf_module_track|mtf_culture_1|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 89,8 dB
  ("travel_swadian_6",					"ext_travel_swadian_6.mp3",			mtf_module_track|mtf_culture_1|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 89,4 dB
  ("travel_vaegir_2",					"travel_vaegir.ogg",				mtf_culture_2|mtf_sit_travel,																mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 86,0 dB
  ("travel_vaegir_3",					"ext_travel_vaegir_3.mp3",			mtf_module_track|mtf_culture_2|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 85,4 dB
  ("travel_vaegir_4",					"ext_travel_vaegir_4.mp3",			mtf_module_track|mtf_culture_2|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 85,6 dB
  ("travel_vaegir_5",					"ext_travel_vaegir_5.mp3",			mtf_module_track|mtf_culture_2|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 86,2 dB
  ("travel_vaegir_6",					"ext_travel_vaegir_6.mp3",			mtf_module_track|mtf_culture_2|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 86,4 dB
  ("travel_khergit_2",					"travel_khergit.ogg",				mtf_culture_3|mtf_sit_travel,																mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 77,8 dB
  ("travel_khergit_3",					"ext_travel_khergit_3.mp3",			mtf_module_track|mtf_culture_3|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 78,0 dB
  ("travel_khergit_4",					"ext_travel_khergit_4.mp3",			mtf_module_track|mtf_culture_3|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 77,4 dB
  ("travel_khergit_5",					"ext_travel_khergit_5.mp3",			mtf_module_track|mtf_culture_3|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 78,2 dB
  ("travel_khergit_6",					"ext_travel_khergit_6.mp3",			mtf_module_track|mtf_culture_3|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 78,5 dB
  ("travel_nord_2",						"travel_nord.ogg",					mtf_culture_4|mtf_sit_travel,																mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 76,3 dB
  ("travel_nord_3",						"ext_travel_nord_3.mp3",			mtf_module_track|mtf_culture_4|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 76,1 dB
  ("travel_nord_4",						"ext_travel_nord_4.mp3",			mtf_module_track|mtf_culture_4|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 76,6 dB
  ("travel_nord_5",						"ext_travel_nord_5.mp3",			mtf_module_track|mtf_culture_4|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 76,0 dB
  ("travel_nord_6",						"ext_travel_nord_6.mp3",			mtf_module_track|mtf_culture_4|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 75,9 dB
  ("travel_rhodok_2",					"travel_rhodok.ogg",				mtf_culture_5|mtf_sit_travel,																mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 84,2 dB
  ("travel_rhodok_3",					"ext_travel_rhodok_3.mp3",			mtf_module_track|mtf_culture_5|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 84,3 dB
  ("travel_rhodok_4",					"ext_travel_rhodok_4.mp3",			mtf_module_track|mtf_culture_5|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 84,1 dB
  ("travel_rhodok_5",					"ext_travel_rhodok_5.mp3",			mtf_module_track|mtf_culture_5|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 83,5 dB
  ("travel_rhodok_6",					"ext_travel_rhodok_6.mp3",			mtf_module_track|mtf_culture_5|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 83,6 dB
  ("travel_sarranid_2",					"middle_eastern_travel.ogg",		mtf_culture_6|mtf_sit_travel,																mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 80,5 dB
  ("travel_sarranid_3",					"ext_travel_sarranid_3.mp3",		mtf_module_track|mtf_culture_6|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 81,1 dB
  ("travel_sarranid_4",					"ext_travel_sarranid_4.mp3",		mtf_module_track|mtf_culture_6|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 80,8 dB
  ("travel_sarranid_5",					"ext_travel_sarranid_5.mp3",		mtf_module_track|mtf_culture_6|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 80,7 dB
  ("travel_sarranid_6",					"ext_travel_sarranid_6.mp3",		mtf_module_track|mtf_culture_6|mtf_sit_travel,												mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),	# 80,0 dB

##Other
#Minimal
  ("uncertain_homestead",				"uncertain_homestead.ogg",			mtf_sit_travel,																				mtf_sit_town|mtf_sit_night|mtf_sit_tavern),					# 89,6 dB
  ("hearth_and_brotherhood",			"hearth_and_brotherhood.ogg",		mtf_sit_travel,																				mtf_sit_town|mtf_sit_night|mtf_sit_tavern),					# 78,6 dB
  ("tragic_village",					"min_tragic_village.mp3",			mtf_module_track|mtf_sit_travel,															mtf_sit_town|mtf_sit_night|mtf_sit_tavern),					# 79,4 dB
#Extended
  ("tragic_village_2",					"tragic_village.ogg",				mtf_sit_travel,																				mtf_sit_town|mtf_sit_night|mtf_sit_tavern),					# 79,1 dB

##Victory!
#Minimal
  ("victorious_evil",					"min_victorious_evil.mp3",			mtf_module_track|mtf_persist_until_finished,												0),															# 84,4dB
  ("victorious_neutral_1",				"victorious_neutral_1.ogg",			mtf_persist_until_finished|mtf_sit_victorious,												0),															# 92,8 dB
  ("victorious_neutral_2",				"victorious_neutral_2.ogg",			mtf_persist_until_finished|mtf_sit_victorious,												0),															# 86,1 dB
  ("victorious_neutral_3",				"victorious_neutral_3.ogg",			mtf_persist_until_finished|mtf_sit_victorious,												0),															# 91,0 dB
  ("victorious_swadian",				"min_victorious_swadian.mp3",		mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious,								0),															# 89,8 dB
  ("victorious_vaegir",					"min_victorious_vaegir.mp3",		mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious,								0),															# 90,3 dB
  ("victorious_khergit",				"min_victorious_khergit.mp3",		mtf_persist_until_finished|mtf_culture_3|mtf_sit_victorious,								0),															# 88,9 dB
  ("victorious_nord",					"min_victorious_nord.mp3",			mtf_persist_until_finished|mtf_culture_4|mtf_sit_victorious,								0),															# 88,9 dB
  ("victorious_rhodok",					"min_victorious_rhodok.mp3",		mtf_persist_until_finished|mtf_culture_5|mtf_sit_victorious,								0),															# 88,9 dB
  ("victorious_sarranid",				"min_victorious_sarranid.mp3",		mtf_persist_until_finished|mtf_culture_5|mtf_sit_victorious,								0),															# 90,2 dB
  ("wedding",							"wedding.ogg",						mtf_persist_until_finished,																	0),															# 86,1 dB
  ("coronation",						"coronation.ogg",					mtf_persist_until_finished,																	0),															# 89,7 dB
#Extended
  ("victorious_evil_2",					"victorious_evil.ogg",				mtf_persist_until_finished,																	0),															# 85,1 dB
  ("victorious_swadian_2",				"victorious_swadian.ogg",			mtf_persist_until_finished|mtf_culture_1|mtf_sit_victorious,								0),															# 88,4 dB
  ("victorious_vaegir_2",				"victorious_vaegir.ogg",			mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious,								0),															# 90,8 dB
  ("victorious_vaegir_3",				"victorious_vaegir_2.ogg",			mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious,								0),															# 88,5 dB

]
