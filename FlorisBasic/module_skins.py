#####Floris Notes#####
# I've used faces from the following sources:
# - Face and UI textures v1.2 by Jed_Q
# - Face Improvement Project v1.0 by Iboltax
# - Face Textures v1.0 by Aquil
# - Female face model and textures replacer v1.30 by Broken_one, updated by Barf
# - Native Warband v1.134 by TaleWorlds
# - Smiley stuff OSP v1.0 by SendMeSmile
# - Thel's Face Pack 3.0 by Thel
# - Yiyang Chen's new faces textures v1.3 by Yiyang Chen, Jed Q and Rosha
######################
from header_skins import *
from ID_particle_systems import *
####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################

man_face_keys = [
(240,0, -0.4,0.3, "Chin Size"),
(230,0, -0.4,0.8, "Chin Shape"),
(250,0,-0.25,0.55, "Chin Forward"),
(130,0,-0.5,1.0, "Jaw Width"),
(120,0,-0.5,0.6, "Lower Lip"),
(110,0,-0.2,0.6, "Upper Lip"),
(100,0,0.2,-0.2, "Mouth-Nose Distance"),
(90,0,0.55,-0.55, "Mouth Width"),

(30,0,-0.3,0.3, "Nostril Size"),
(60,0,0.25,-0.25, "Nose Height"),
(40,0,-0.2,0.3, "Nose Width"),
(70,0,-0.3,0.4, "Nose Size"),
(50,0,0.2,-0.3, "Nose Shape"),
(80,0,-0.3,0.65, "Nose Bridge"),

(160,0,-0.2,0.25, "Eye Width"),
(190,0,-0.25,0.15, "Eye to Eye Dist"),
(170,0,-0.85,0.85, "Eye Shape"),
(200,0,-0.3, 0.7, "Eye Depth"),
(180,0,-1.5,1.5, "Eyelids"),

(20,0,0.6,-0.25, "Cheeks"),
(260,0,-0.6,0.5, "Cheek Bones"),
(220,0,0.8,-0.8, "Eyebrow Height"),
(210,0,-0.75,0.75, "Eyebrow Shape"),
(10,0,-0.6,0.5, "Temple Width"),

(270,0,-0.3,1.0, "Face Depth"),
(150,0,-0.25,0.45, "Face Ratio"),
(140,0,-0.4,0.5, "Face Width"),

(280,0,1.0,1.0, "Post-Edit"),
]
# Face width-Jaw width Temple width
woman_face_keys = [
(230,0,0.8,-1.0, "Chin Size"), 
(220,0,-1.0,1.0, "Chin Shape"), 
(10,0,-1.2,1.0, "Chin Forward"),
(20,0, -0.6, 1.2, "Jaw Width"), 
(40,0,-0.7,1.0, "Jaw Position"),
(270,0,0.9,-0.9, "Mouth-Nose Distance"),
(30,0,-0.5,1.0, "Mouth Width"),
(50,0, -0.5,1.0, "Cheeks"),

(60,0,-0.5,1.0, "Nose Height"),
(70,0,-0.6,1.0, "Nose Width"),
(80,0,1.5,-0.3, "Nose Size"),
(240,0,-1.0,0.8, "Nose Shape"),
(90,0, 0.0,1.1, "Nose Bridge"),

(100,0,-0.5,1.5, "Cheek Bones"),
(150,0,-0.5,0.1, "Eye Width"),
(110,0,1.0,0.0, "Eye to Eye Dist"),
(120,0,-0.2,1.0, "Eye Shape"),
(130,0,-0.1,1.6, "Eye Depth"),
(140,0,-0.2,1.0, "Eyelids"),


(160,0,-0.2,1.2, "Eyebrow Position"),
(170,0,-0.2,0.7, "Eyebrow Height"),
(250,0,-0.4,0.9, "Eyebrow Depth"),
(180,0,-1.5,1.2, "Eyebrow Shape"),
(260,0,1.0,-0.7, "Temple Width"),

(200,0,-0.5,1.0, "Face Depth"),
(210,0,-0.5,0.9, "Face Ratio"),
(190,0,-0.4,0.8, "Face Width"),

(280,0,0.0,1.0, "Post-Edit"),
]
undead_face_keys = []


chin_size = 0
chin_shape = 1
chin_forward = 2
jaw_width = 3
jaw_position = 4
mouth_nose_distance = 5
mouth_width = 6
cheeks = 7
nose_height = 8
nose_width = 9
nose_size = 10
nose_shape = 11
nose_bridge = 12
cheek_bones = 13
eye_width = 14
eye_to_eye_dist = 15
eye_shape = 16
eye_depth = 17
eyelids = 18
eyebrow_position = 19
eyebrow_height = 20
eyebrow_depth = 21
eyebrow_shape = 22
temple_width = 23
face_depth = 24
face_ratio = 25
face_width = 26

comp_less_than = -1;
comp_greater_than = 1;

skins = [
  (
    "man", 0,
    "fac_man_body", "fac_man_calf_l", "fac_man_handL",
    "fac_male_head", man_face_keys, #Bald: Swadian 16, Rolf, Yaroglek
    ["fac_man_hair_a" #  1 a Swadia 6, Marnid
	,"fac_man_hair_b" #  2 b Swadia
	,"fac_man_hair_c" # 14 n Swadia, Jeremus
	,"fac_man_hair_d" # 21 u Swadia
	,"fac_man_hair_e" # 18 r Vaegir 9, Swadia 4, Graveth
	,"fac_man_hair_f" # 17 q Vaegir, Lezalit
	,"fac_man_hair_g" # 13 m Vaegir
	,"fac_man_hair_h" # 22 v Vaegir 11
	,"fac_man_hair_i" # 16 p Khergit 14, Vaegir 13
	,"fac_man_hair_j" # 19 s Vaegir 8, Khergit 17
	,"fac_man_hair_k" # 12 l Khergit 18, Sanjar
	,"fac_man_hair_l" # 11 k Khergit, Baheshtur, Dustum
	,"fac_man_hair_m" #  7 g Khergit 10
	,"fac_man_hair_n" # 10 j Khergit, Nord, Ragnar
	,"fac_man_hair_o" #  3 c Nord 2, Borcha, Firentis
	,"fac_man_hair_p" #  9 i Nord
	,"fac_man_hair_q" #  4 d Nord 1, Sajjad, Ghazwan, Edwyn, Lethwyn
	,"fac_man_hair_r" # 15 o Rhodok 15, Nord 12, Alayen, Floris
	,"fac_man_hair_s" # 20 t Rhodok 3, Hakim, Valdym
	,"fac_man_hair_t" #  8 h Rhodok, Nizar
	,"fac_man_hair_u" #  6 f Rhodok 5, Sarranid 19, 20, Bunduk, Artimenner, Harlaus
	,"fac_man_hair_v" #  5 e Swadia 7, Sarranid 21, 22, Kastor
	], #man_hair_meshes
    ["fac_beard_a","fac_beard_b","fac_beard_c","fac_beard_d","fac_beard_e","fac_beard_f","fac_beard_g","fac_beard_h","fac_beard_i","fac_beard_j","fac_beard_k","fac_beard_l","fac_beard_m","fac_beard_n","fac_beard_o","fac_beard_p","fac_beard_q","fac_beard_r","fac_beard_s","fac_beard_t","fac_beard_u","fac_beard_v","fac_beard_w",], #beard meshes ,"fac_beard_x"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [("fac_manface_white01",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("fac_manface_white02",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
	 ("fac_manface_white03",0xffd0e0e0,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),     
     ("fac_manface_white04",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
     ("fac_manface_white05",0xffc0c8c8,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("fac_manface_white06",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("fac_manface_white07",0xffb0aab5,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("fac_manface_white08",0xffe0e8e8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("fac_manface_white09",0xffe0e8e8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("fac_manface_white10",0xffe0e8e8,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("fac_manface_white11",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("fac_manface_white12",0xffc0c8c8,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("fac_manface_asian1",0xffe3e8e1,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("fac_manface_asian2",0xffe3e8e1,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("fac_manface_asian3",0xffbbb6ae,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("fac_manface_mideast1",0xffaeb0a6,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("fac_manface_mideast2",0xffd0c8c1,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("fac_manface_mideast3",0xffe0e8e8,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("fac_manface_black01",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]), 
     ("fac_manface_black02",0xff87655c,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("fac_manface_black03",0xff5a342d,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("fac_manface_black04",0xff634d3e,["hair_blonde"],[0xff171313, 0xff007080c]),  
     ("fac_manface_black05",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),   
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
    [[1.6, comp_greater_than, (1.0,eye_to_eye_dist), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.6, comp_less_than, (1.0,eye_to_eye_dist), (1.0,temple_width)],
     [1.5, comp_greater_than, (1.0,face_ratio), (1.0,mouth_width)],
     [0.6, comp_greater_than, (-1.0,nose_width), (1.0,mouth_width)],
     [-1.0, comp_less_than, (-1.0,nose_width), (1.0,mouth_width)],
     ]
  ),
  
  (
    "woman", skf_use_morph_key_10,
    "fac_woman_body",  "fac_woman_calf_l", "fac_woman_handL",
    "fac_female_head", woman_face_keys,
    ["fac_woman_hair_a" #  2 b Swadia, Isolla
	,"fac_woman_hair_b" #  3 c Swadia, Katrin
	,"fac_woman_hair_c" # 20 t Swadia
	,"fac_woman_hair_d" #  7 g Vaegir, Klethi
	,"fac_woman_hair_e" # 10 j Vaegir
	,"fac_woman_hair_f" # 12 l Vaegir
	,"fac_woman_hair_g" #  5 e Khergit, Deshavi, Nadia, Odval
	,"fac_woman_hair_h" # 11 k Khergit
	,"fac_woman_hair_i" # 17 q Khergit
	,"fac_woman_hair_j" #  6 f Nord, Matheld
	,"fac_woman_hair_k" #  8 h Nord
	,"fac_woman_hair_l" # 18 r Nord
	,"fac_woman_hair_m" #  1 a Rhodok, Ymira
	,"fac_woman_hair_n" # 14 n Rhodok
	,"fac_woman_hair_o" # 15 o Rhodok
	,"fac_woman_hair_p" #  4 d Sarranid, Arwa
	,"fac_woman_hair_q" #  9 i Sarranid
	,"fac_woman_hair_r" # 16 p Sarranid
	,"fac_woman_hair_s" # 19 s Sarranid
	], #woman_hair_meshes
    ["fac_jewellery_a","fac_jewellery_b","fac_jewellery_c","fac_jewellery_d","fac_jewellery_e","fac_jewellery_f","fac_jewellery_g","fac_jewellery_h","fac_jewellery_i","fac_jewellery_j"],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["fac_jewellery","fac_jewellery","fac_jewellery","fac_jewellery","fac_jewellery"],
    [("fac_womanface_white01",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),										#blond
     ("fac_womanface_white02",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),				#blond
	 ("fac_womanface_white03",0xffd0e0e0,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),							#orange
     ("fac_womanface_white04",0xffe0e8e8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),	#blond
     ("fac_womanface_white05",0xffe0e8e8,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),							#orange
     ("fac_womanface_white06",0xffc0c8c8,["hair_blonde"],[0xff171313, 0xff007080c]),												#black
     ("fac_womanface_white07",0xffe0e8e8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),				#blond
     ("fac_womanface_white08",0xffb0aab5,["hair_blonde"],[0xff171313, 0xff007080c]),												#black
     ("fac_womanface_white09",0xffc0c8c8,["hair_blonde"],[0xff171313, 0xff007080c]),												#black
     ("fac_womanface_white10",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),									#brown
     ("fac_womanface_white11",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),										#blond
     ("fac_womanface_white12",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),										#brown
     ("fac_womanface_asian01",0xffaf9f7e,["hair_blonde"],[0xff19100c, 0xff0c0d19, 0xff007080c]),
     ("fac_womanface_asian02",0xffe3e8e1,["hair_blonde"],[0xff19100c, 0xff0c0d19, 0xff007080c]),
     ("fac_womanface_asian03",0xffbbb6ae,["hair_blonde"],[0xff19100c, 0xff0c0d19, 0xff007080c]),
     ("fac_womanface_mideast01",0xffaeb0a6,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("fac_womanface_mideast02",0xffd0c8c1,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("fac_womanface_mideast03",0xffe0e8e8,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("fac_womanface_black01",0xff808080,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("fac_womanface_black02",0xff634d3e,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("fac_womanface_black03",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),
     ],#woman_face_textures
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
  ),
  
##  (
##    "undead", 0,
##    "fac_undead_body", "fac_undead_calf_l", "fac_undead_handL",
##    "fac_undead_head", undead_face_keys,
##    [],
##    [],
##    [],
##    [],
##    [("undeadface_a",0xffffffff,[]),
##     ("undeadface_b",0xffcaffc0,[]),
##     ], #undead_face_textures
##    [], #voice sounds
##    "skel_human", 1.0,
##  ),
]

