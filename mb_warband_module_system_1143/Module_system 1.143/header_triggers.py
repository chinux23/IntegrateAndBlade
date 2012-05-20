###################################################
# header_triggers.py
# This file contains declarations for triggers
# DO NOT EDIT THIS FILE!
###################################################

#trigger interval flags

#ti_on_game_start         = -2.0
ti_simulate_battle       = -5.0 #can only be used in module_simple_triggers
ti_on_party_encounter    = -6.0 #can only be used in module_simple_triggers
ti_question_answered     = -8
ti_server_player_joined  = -15.0 #can only be used in module_mission_templates triggers
# Used only by the server in multiplayer mode
ti_on_multiplayer_mission_end = -16.0

# Trigger Param 1: player_no
ti_before_mission_start  = -19.0 #can only be used in module_mission_templates triggers
ti_after_mission_start   = -20.0 #can only be used in module_mission_templates triggers
ti_tab_pressed           = -21.0 #can only be used in module_mission_templates triggers
ti_inventory_key_pressed = -22.0 #can only be used in module_mission_templates triggers
ti_escape_pressed        = -23.0 #can only be used in module_mission_templates triggers
ti_battle_window_opened  = -24.0 #can only be used in module_mission_templates triggers
ti_on_agent_spawn 	= -25.0 #can only be used in module_mission_templates triggers
ti_on_agent_killed_or_wounded = -26.0 #can only be used in module_mission_templates triggers
ti_on_agent_knocked_down = -27.0 #can only be used in module_mission_templates triggers
ti_on_agent_hit          = -28.0 #can only be used in module_mission_templates triggers
# Trigger Param 1: damage inflicted agent_id
# Trigger Param 2: damage dealer agent_id
# Trigger Param 3: inflicted damage
# Register 0: damage dealer item_id
# Position Register 0: position of the blow
#                      rotation gives the direction of the blow
# Trigger result: if returned result is greater than or equal to zero, inflicted damage is set to the value specified by the module.

ti_on_player_exit        = -29.0 #can only be used in module_mission_templates triggers
# Trigger Param 1: player_id

ti_on_leave_area         = -30.0 #can only be used in module_mission_templates triggers
ti_on_scene_prop_init    = -40.0 #can only be used in module_scene_props triggers
ti_on_init_scene_prop    = ti_on_scene_prop_init
# Trigger Param 1: prop instance number

ti_on_scene_prop_hit     = -42.0 #can only be used in module_scene_props triggers
# Trigger Param 1: prop instance number
# Trigger Param 2: hit damage
# Position Register 1: Hit Position
# Position Register 2: x holds attacker agent id

ti_on_scene_prop_destroy = -43.0 #can only be used in module_scene_props triggers
# Trigger Param 1: prop instance number

ti_on_scene_prop_use     = -44.0 #can only be used in module_scene_props triggers
# Trigger Param 1: user agent id
# Trigger Param 2: prop instance number

ti_on_scene_prop_is_animating = -45.0 #can only be used in module_scene_props triggers
# Trigger Param 1: prop instance number
# Trigger Param 2: remaining animation time

ti_on_scene_prop_animation_finished = -46.0 #can only be used in module_scene_props triggers
# Trigger Param 1: prop instance number

ti_on_scene_prop_start_use = -47.0 #can only be used in module_scene_props triggers
# Trigger Param 1: user agent id
# Trigger Param 2: prop instance number

ti_on_scene_prop_cancel_use = -48.0 #can only be used in module_scene_props triggers
# Trigger Param 1: user agent id
# Trigger Param 2: prop instance number

ti_on_init_item          = -50.0 #can only be used in module_items triggers
ti_on_weapon_attack      = -51.0 #can only be used in module_items triggers
# Trigger Param 1: attacker agent id
# Position Register 1: Weapon Item Position
ti_on_missile_hit        = -52.0 #can only be used in module_items triggers
# Position Register 1: Missile Position
# Trigger Param 1: shooter agent id
ti_on_item_picked_up     = -53.0 #can only be used in module_mission_templates triggers
# Trigger Param 1: agent id
# Trigger Param 2: item id
# Trigger Param 3: scene prop id (will be deleted after this trigger)
ti_on_item_dropped       = -54.0 #can only be used in module_mission_templates triggers
# Trigger Param 1: agent id
# Trigger Param 2: item id
# Trigger Param 3: scene prop id
ti_on_agent_mount        = -55.0 #can only be used in module_mission_templates triggers
# Trigger Param 1: agent id
# Trigger Param 2: horse agent id
ti_on_agent_dismount     = -56.0 #can only be used in module_mission_templates triggers
# Trigger Param 1: agent id
# Trigger Param 2: horse agent id
ti_on_item_wielded       = -57.0 #can only be used in module_mission_templates triggers
# Trigger Param 1: agent id
# Trigger Param 2: item id
ti_on_item_unwielded     = -58.0 #can only be used in module_mission_templates triggers
# Trigger Param 1: agent id
# Trigger Param 2: item id
ti_on_presentation_load  = -60.0 #can only be used in module_presentations triggers
ti_on_presentation_run   = -61.0 #can only be used in module_presentations triggers
# Trigger Param 1: current time in miliseconds
ti_on_presentation_event_state_change = -62.0 #can only be used in module_presentations triggers
# Trigger Param 1: id of the object that has the event
# Trigger Param 2: value (when available)
ti_on_presentation_mouse_enter_leave  = -63.0 #can only be used in module_presentations triggers
# Trigger Param 1: id of the object that mouse enters/leaves
# Trigger Param 2: 0 if mouse enters, 1 if mouse leaves
ti_on_presentation_mouse_press        = -64.0 #can only be used in module_presentations triggers
# Trigger Param 1: id of the object that mouse is pressed on
# Trigger Param 2: 0: left mouse button, 1 right mouse button, 2 middle mouse button
ti_on_init_map_icon                   = -70.0 #can only be used in module_map_icons triggers
# Trigger Param 1: id of the owner party


ti_once        = 100000000.0

# Keys that can be checked by key_is_down and key_clicked

key_1 = 0x02
key_2 = 0x03
key_3 = 0x04
key_4 = 0x05
key_5 = 0x06
key_6 = 0x07
key_7 = 0x08
key_8 = 0x09
key_9 = 0x0a
key_0 = 0x0b
key_a = 0x1e
key_b = 0x30
key_c = 0x2e
key_d = 0x20
key_e = 0x12
key_f = 0x21
key_g = 0x22
key_h = 0x23
key_i = 0x17
key_j = 0x24
key_k = 0x25
key_l = 0x26
key_m = 0x32
key_n = 0x31
key_o = 0x18
key_p = 0x19
key_q = 0x10
key_r = 0x13
key_s = 0x1f
key_t = 0x14
key_u = 0x16
key_v = 0x2f
key_w = 0x11
key_x = 0x2d
key_y = 0x15
key_z = 0x2c
key_numpad_0 = 0x52
key_numpad_1 = 0x4f
key_numpad_2 = 0x50
key_numpad_3 = 0x51
key_numpad_4 = 0x4b
key_numpad_5 = 0x4c
key_numpad_6 = 0x4d
key_numpad_7 = 0x47
key_numpad_8 = 0x48
key_numpad_9 = 0x49
key_num_lock        = 0x45
key_numpad_slash    = 0xb5
key_numpad_multiply = 0x37
key_numpad_minus    = 0x4a
key_numpad_plus     = 0x4e
key_numpad_enter    = 0x9c
key_numpad_period   = 0x53
key_insert    = 0xd2
key_delete    = 0xd3
key_home      = 0xc7
key_end       = 0xcf
key_page_up   = 0xc9
key_page_down = 0xd1
key_up      = 0xc8
key_down    = 0xd0
key_left    = 0xcb
key_right   = 0xcd
key_f1  = 0x3b
key_f2  = 0x3c
key_f3  = 0x3d
key_f4  = 0x3e
key_f5  = 0x3f
key_f6  = 0x40
key_f7  = 0x41
key_f8  = 0x42
key_f9  = 0x43
key_f10 = 0x44
key_f11 = 0x57
key_f12 = 0x58
key_space         = 0x39
key_escape        = 0x01
key_enter         = 0x1c
key_tab           = 0x0f
key_back_space    = 0x0e
key_open_braces   = 0x1a
key_close_braces  = 0x1b
key_comma         = 0x33
key_period        = 0x34
key_slash         = 0x35
key_back_slash    = 0x2b
key_equals        = 0x0d
key_minus         = 0x0c
key_semicolon     = 0x27
key_apostrophe    = 0x28
key_tilde         = 0x29
key_caps_lock     = 0x3a
key_left_shift     = 0x2a
key_right_shift    = 0x36
key_left_control   = 0x1d
key_right_control  = 0x9d
key_left_alt       = 0x38
key_right_alt      = 0xb8
key_left_mouse_button   = 0xe0
key_right_mouse_button  = 0xe1
key_middle_mouse_button = 0xe2
key_mouse_button_4      = 0xe3
key_mouse_button_5      = 0xe4
key_mouse_button_6      = 0xe5
key_mouse_button_7      = 0xe6
key_mouse_button_8      = 0xe7
key_mouse_scroll_up     = 0xee
key_mouse_scroll_down   = 0xef


# Game keys that can be checked by game_key_is_down and game_key_clicked

gk_move_forward = 0
gk_move_backward = 1
gk_move_left = 2
gk_move_right = 3
gk_action = 4
gk_jump = 5
gk_attack = 6
gk_defend = 7
gk_kick = 8
#gk_parry_then_attack = 8
gk_toggle_weapon_mode = 9
gk_equip_weapon_1 = 10
gk_equip_weapon_2 = 11
gk_equip_weapon_3 = 12
gk_equip_weapon_4 = 13
gk_equip_primary_weapon = 14
gk_equip_secondary_weapon = 15
gk_drop_weapon = 16
gk_sheath_weapon = 17
gk_leave = 18
gk_zoom = 19
gk_view_char = 20
gk_cam_toggle = 21
gk_view_orders = 22
gk_order_1 = 23
gk_order_2 = 24
gk_order_3 = 25
gk_order_4 = 26
gk_order_5 = 27
gk_order_6 = 28
##gk_order_halt = 22
##gk_order_follow = 23
##gk_order_charge = 24
##gk_order_dismount = 25
##gk_order_hold_fire_toggle = 26
##gk_order_advance = 27
##gk_order_fall_back = 28
##gk_order_stand_closer = 29
##gk_order_spread_out = 30
##gk_order_blunt_weapons_toggle = 31
gk_everyone_hear = 29
gk_infantry_hear = 30
gk_archers_hear = 31
gk_cavalry_hear = 32
gk_group0_hear = gk_infantry_hear
gk_group1_hear = gk_archers_hear
gk_group2_hear = gk_cavalry_hear
gk_group3_hear = 33
gk_group4_hear = 34
gk_group5_hear = 35
gk_group6_hear = 36
gk_group7_hear = 37
gk_group8_hear = 38
gk_reverse_order_group = 39
gk_everyone_around_hear = 40
gk_mp_message_all = 41
gk_mp_message_team = 42
gk_character_window = 43
gk_inventory_window = 44
gk_party_window = 45
gk_quests_window = 46
gk_game_log_window = 47
gk_quick_save = 48


#trigger positions
#------------------------------------------------------
trigger_check_pos = 0 
trigger_delay_pos = 1
trigger_rearm_pos = 2
trigger_conditions_pos = 3
trigger_consequences_pos = 4

def ti_val(iv):
  return iv
