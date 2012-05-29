from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
## CC
missile_distance_trigger	= [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter_agent"),
      
      (eq, "$g_report_shot_distance", 1),
      (get_player_agent_no, ":player_agent"),
      (try_begin),
        (eq, ":shooter_agent", ":player_agent"),
        (agent_get_position, pos2, ":shooter_agent"),
        (agent_get_horse, ":horse_agent", ":player_agent"),
        (try_begin),
          (gt, ":horse_agent", -1),
          (position_move_z, pos2, 220),
        (else_try),
          (position_move_z, pos2, 150),
        (try_end),
        (get_distance_between_positions, ":distance", pos1, pos2),
        (store_div, reg61, ":distance", 100),
        (store_mod, reg62, ":distance", 100),
        (try_begin),
          (lt, reg62, 10),
          (str_store_string, s1, "@{reg61}.0{reg62}"),
        (else_try),
          (str_store_string, s1, "@{reg61}.{reg62}"),
        (try_end),
        (display_message, "@Shot distance: {s1} meters.", 0xCCCCCC),
      (try_end),
    ])]
## CC
unique_items = [
# Player Plate Armor
["blue_plate_armor", "Plate Armor", [("zhongjia_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 6553 , weight(27)|abundance(0)|head_armor(0)|body_armor(55)|leg_armor(17)|difficulty(9) ,imodbits_plate, [],[fac_player_faction] ],
["green_plate_armor", "Plate Armor", [("zhongjia_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 6553 , weight(27)|abundance(0)|head_armor(0)|body_armor(55)|leg_armor(17)|difficulty(9) ,imodbits_plate, [],[fac_player_faction] ],
["red_plate_armor", "Plate Armor", [("zhongjia_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 6553 , weight(27)|abundance(0)|head_armor(0)|body_armor(55)|leg_armor(17)|difficulty(9) ,imodbits_plate, [],[fac_player_faction] ],
["yellow_plate_armor", "Plate Armor", [("zhongjia_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 6553 , weight(27)|abundance(0)|head_armor(0)|body_armor(55)|leg_armor(17)|difficulty(9) ,imodbits_plate, [],[fac_player_faction] ],
# Player Plate Boots
["plate_boots1", "Plate Boots", [("xie1", 0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_plate, [],[fac_player_faction] ],
["plate_boots2", "Plate Boots", [("xie2", 0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_plate, [],[fac_player_faction] ],
["plate_boots3", "Plate Boots", [("xie3",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_plate, [],[fac_player_faction] ],
["plate_boots5", "Plate Boots", [("xie5",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_plate, [],[fac_player_faction] ],

# Player Gauntlets
["gauntlets_1","Gauntlets", [("zuoshou1_L",0),("zuoshou1_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 1040, weight(1.0)|abundance(0)|body_armor(6)|difficulty(0),imodbits_armor, [],[fac_player_faction]],
["gauntlets_2","Gauntlets", [("zuoshou2_L",0),("zuoshou2_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 1040, weight(1.0)|abundance(0)|body_armor(6)|difficulty(0),imodbits_armor, [],[fac_player_faction]],
["gauntlets_3","Gauntlets", [("zuoshou3_L",0),("zuoshou3_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 1040, weight(1.0)|abundance(0)|body_armor(6)|difficulty(0),imodbits_armor, [],[fac_player_faction]],
["gauntlets_5","Gauntlets", [("zuoshou5_L",0),("zuoshou5_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 1040, weight(1.0)|abundance(0)|body_armor(6)|difficulty(0),imodbits_armor, [],[fac_player_faction]],

# End of items
]

from util_common import *
from util_wrappers import *

def modmerge_items(orig_items):
    pos = list_find_first_match_i(orig_items, "items_end")
    OpBlockWrapper(orig_items).InsertBefore(pos, unique_items)	
	
def modmerge(var_set):
    try:
        var_name_1 = "items"
        orig_items = var_set[var_name_1]
        modmerge_items(orig_items)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
