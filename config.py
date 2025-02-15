# SPDX-License-Identifier: GPL-3.0-or-later

## Supported file version
SUPPORTED_FILE_VERSION = 6, 0, 1

## length precision for geometry
LP = 4
## geographic location precision
GEOLOC_PRECISION = 9
## time precision
TIME_PRECISION = 1

## max number of columns of formatted output
MAXLEN = 80
## number of columns for second line indent
INDENT = 6

## min edge length
MIN_EDGE_LENGTH = 1e-05
## min face area
MIN_FACE_AREA = 1e-08
## min intersection length
MIN_INTERSECTION_LENGTH = 1e-05
## flat face difference
FLAT_DIFFERENCE = 1e-03

## number of magnetic cells for MESH alignment (align_meshes.py)
MAGNET_NCELL = 3

## run fds commands
# from sys.platform: linux is any Linux, darwin is any MacOS, win32 is any Windows
FDS_COMMAND = {
    "linux": """cd '{p}' && export OMP_NUM_THREADS={t} && mpiexec -n {n} fds '{f}' ; sleep 5 ; exit""",
    "darwin": """cd '{p}' && export OMP_NUM_THREADS={t} && mpiexec -n {n} fds '{f}' ; sleep 5 ; exit""",
    "win32": """cd "{p}" && fdsinit && mpiexec -n {n} -env OMP_NUM_THREADS {t} fds "{f}" & timeout 5 & exit""",
}
## run smokeview commands
SMV_COMMAND = {
    "linux": """cd '{p}' && smokeview '{f}'""",
    "darwin": """cd '{p}' && smokeview '{f}'""",
    "win32": """cd "{p}" && fdsinit && smokeview "{f}" """,
}
## run terminal commands
# In darwin, to have the terminal close, the user should also modify
# a (much debated in the forums ;-) default of the Terminal App setting:
# Preferences → Profiles → (pick whichever is yours) →
# → Shell → When the shell exits: (change this to "Close if the shell exits cleanly").
TERM_COMMAND = {
    "linux": """gnome-terminal --window --title "FDS" -- bash -c "{c}" """,
    "darwin": """osascript -e 'tell app "Terminal" to do script "{c}" ' """,
    "win32": """START "FDS" cmd /c "{c}" """,
}


## Default SURF Materials
DEFAULT_MAS = {  # name: diffuse_color
    "INERT": ((0.8, 0.8, 0.2, 1.0),),
    "HVAC": ((0.2, 0.2, 0.8, 0.5),),
    "MIRROR": ((1.0, 0.0, 1.0, 0.2),),
    "OPEN": ((0.2, 0.8, 0.8, 0.05),),
    "PERIODIC": ((1.0, 0.0, 1.0, 0.2),),
}

## Frequently used output QUANTITY
# from FDS User's guide table:
# name, units, qtype
FDS_QUANTITIES = """\
ABSORPTION COEFFICIENT,1/m,DIPS
ACTUATED SPRINKLERS,,D
ADIABATIC SURFACE TEMPERATURE,°C,BD
AEROSOL VOLUME FRACTION,mol/mol,DIPS
AMPUA,kg/m²,BD
AMPUA_Z,kg/m²,BD
ASPIRATION,%/m,D
BACKGROUND PRESSURE,Pa,DIPS
BACK WALL TEMPERATURE,°C,BD
BURNING RATE,kg/(m²·s),BD
CHAMBER OBSCURATION,%/m,D
CHI_R,,DIS
CONDUCTIVITY,W/(m·K),DIPS
CONTROL,,D
CONTROL VALUE,,D
CONDENSATION HEAT FLUX,kW/m²,BD
CONVECTIVE HEAT FLUX,kW/m²,BD
CPUA,kW/m²,BD
CPUA_Z,kW/m²,BD
CPU TIME,s,D
DENSITY,kg/m³,DIPS
DEPOSITION VELOCITY,m/s,BD
DIVERGENCE,1/s,DIPS
DROPLET VOLUME FRACTION,,DPS
ENTHALPY,kJ/m³,DIPS
ENTHALPY FLUX X,kW/m²,DIPS
ENTHALPY FLUX Y,kW/m²,DIPS
ENTHALPY FLUX Z,kW/m²,DIPS
EXTINCTION COEFFICIENT,1/m,DIPS
FED,,D
FIC,,DS
FRICTION VELOCITY,m/s,BD
GAUGE HEAT FLUX,kW/m²,BD
ENTHALPY FLUX WALL,kW/m²,BD
TOTAL HEAT FLUX,kW/m²,BD
HRRPUA,kW/m²,D
HRRPUV,kW/m³,DIPS
INCAPACITATION TIME,min,D
INCIDENT HEAT FLUX,kW/m²,BD
INSIDE WALL TEMPERATURE,°C,D
INSIDE WALL DEPTH,m,D
INTERNAL ENERGY,kJ/m³,DIPS
ITERATION,,D
LAYER HEIGHT,m,D
LINK TEMPERATURE,°C,D
LOWER TEMPERATURE,°C,D
MASS FLUX,kg/(m²·s),BD
MASS FLUX WALL,kg/(m²·s),BD
MASS FLUX X,kg/(m²·s),DIPS
MASS FLUX Y,kg/(m²·s),DIPS
MASS FLUX Z,kg/(m²·s),DIPS
MASS FRACTION,kg/kg,DIPS
MIXTURE FRACTION,kg/kg,DIPS
MPUA,kg/m,BD
MPUA_Z,kg/m²,BD
MPUV,kg/m³,DPS
MPUV_Z,kg/m³,DPS
NORMAL VELOCITY,m/s,DB
NUMBER OF PARTICLES,,D
OPEN NOZZLES,,D
OPTICAL DENSITY,1/m,DIPS
ORIENTED VELOCITY,m/s,D
PATH OBSCURATION,%,D
PARTICLE AGE,s,PA
PARTICLE BULK DENSITY,kg/m³,PA
PARTICLE DIAMETER,µm,PA
PARTICLE FLUX X,kg/(m²·s),PS
PARTICLE FLUX Y,kg/(m²·s),PS
PARTICLE FLUX Z,kg/(m²·s),PS
PARTICLE MASS,kg,PA
PARTICLE PHASE,,PA
PARTICLE TEMPERATURE,°C,PA
PARTICLE U,m/s,PA
PARTICLE V,m/s,PA
PARTICLE VELOCITY,m/s,PA
PARTICLE W,m/s,PA
PARTICLE WEIGHTING FACTOR,,PA
PARTICLE X,m,PA
PARTICLE Y,m,PA
PARTICLE Z,m,PA
PRESSURE,Pa,DIPS
PRESSURE COEFFICIENT,,BD
PRESSURE ZONE,,DS
RADIATIVE HEAT FLUX,kW/m²,BD
RADIATIVE HEAT FLUX GAS,kW/m²,D
RADIOMETER,kW/m²,BD
RELATIVE HUMIDITY,%,DIPS
SENSIBLE ENTHALPY,kJ/m³,DIPS
SOLID CELL DENSITY,kg/m³,DIPS
SOLID CELL Q_S,kW/m³,DIPS
SOLID CELL VOLUME RATIO,m³/m³,DIPS
SOLID CONDUCTIVITY,W/(m·K),D
SOLID DENSITY,kg/m³,D
SOLID SPECIFIC HEAT,kJ/(kg·K),D
SPECIFIC ENTHALPY,kJ/kg,DIPS
SPECIFIC HEAT,kJ/(kg·K),DIPS
SPECIFIC INTERNAL ENERGY,kJ/kg,DIPS
SPECIFIC SENSIBLE ENTHALPY,kJ/kg,DIPS
SPRINKLER LINK TEMPERATURE,°C,D
SURFACE DENSITY,kg/m²,BD
SURFACE DEPOSITION,kg/m²,BD
TEMPERATURE,°C,DIPS
THERMOCOUPLE,°C,D
TIME,s,D
TIME STEP,s,D
TRANSMISSION,%/m,D
U-VELOCITY,m/s,DIPS
V-VELOCITY,m/s,DIPS
W-VELOCITY,m/s,DIPS
UPPER TEMPERATURE,°C,D
VELOCITY,m/s,DIPS
VISCOSITY,kg/(m·s),DIPS
VISIBILITY,m,DIPS
VOLUME FRACTION,mol/mol,DIPS
WALL CLOCK TIME,s,D
WALL CLOCK TIME ITERATIONS,s,D
WALL TEMPERATURE,°C,BD
WALL THICKNESS,m,BD"""


## Color table from FDS source code (data.f90)
FDS_COLORS = {
    "INVISIBLE": (255, 255, 255),
    "ALICE BLUE": (240, 248, 255),
    "ANTIQUE WHITE": (250, 235, 215),
    "ANTIQUE WHITE 1": (255, 239, 219),
    "ANTIQUE WHITE 2": (238, 223, 204),
    "ANTIQUE WHITE 3": (205, 192, 176),
    "ANTIQUE WHITE 4": (139, 131, 120),
    "AQUAMARINE": (127, 255, 212),
    "AQUAMARINE 1": (118, 238, 198),
    "AQUAMARINE 2": (102, 205, 170),
    "AQUAMARINE 3": (69, 139, 116),
    "AZURE": (240, 255, 255),
    "AZURE 1": (224, 238, 238),
    "AZURE 2": (193, 205, 205),
    "AZURE 3": (131, 139, 139),
    "BANANA": (227, 207, 87),
    "BEIGE": (245, 245, 220),
    "BISQUE": (255, 228, 196),
    "BISQUE 1": (238, 213, 183),
    "BISQUE 2": (205, 183, 158),
    "BISQUE 3": (139, 125, 107),
    "BLACK": (0, 0, 0),
    "BLANCHED ALMOND": (255, 235, 205),
    "BLUE": (0, 0, 255),
    "BLUE 2": (0, 0, 238),
    "BLUE 3": (0, 0, 205),
    "BLUE 4": (0, 0, 139),
    "BLUE VIOLET": (138, 43, 226),
    "BRICK": (156, 102, 31),
    "BROWN": (165, 42, 42),
    "BROWN 1": (255, 64, 64),
    "BROWN 2": (238, 59, 59),
    "BROWN 3": (205, 51, 51),
    "BROWN 4": (139, 35, 35),
    "BURLY WOOD": (222, 184, 135),
    "BURLY WOOD 1": (255, 211, 155),
    "BURLY WOOD 2": (238, 197, 145),
    "BURLY WOOD 3": (205, 170, 125),
    "BURLY WOOD 4": (139, 115, 85),
    "BURNT ORANGE": (204, 85, 0),
    "BURNT SIENNA": (138, 54, 15),
    "BURNT UMBER": (138, 51, 36),
    "CADET BLUE": (95, 158, 160),
    "CADET BLUE 1": (152, 245, 255),
    "CADET BLUE 2": (142, 229, 238),
    "CADET BLUE 3": (122, 197, 205),
    "CADET BLUE 4": (83, 134, 139),
    "CADMIUM ORANGE": (255, 97, 3),
    "CADMIUM YELLOW": (255, 153, 18),
    "CARROT": (237, 145, 33),
    "CHARTREUSE": (127, 255, 0),
    "CHARTREUSE 1": (118, 238, 0),
    "CHARTREUSE 2": (102, 205, 0),
    "CHARTREUSE 3": (69, 139, 0),
    "CHOCOLATE": (210, 105, 30),
    "CHOCOLATE 1": (255, 127, 36),
    "CHOCOLATE 2": (238, 118, 33),
    "CHOCOLATE 3": (205, 102, 29),
    "CHOCOLATE 4": (139, 69, 19),
    "COBALT": (61, 89, 171),
    "COBALT GREEN": (61, 145, 64),
    "COLD GREY": (128, 138, 135),
    "CORAL": (255, 127, 80),
    "CORAL 1": (255, 114, 86),
    "CORAL 2": (238, 106, 80),
    "CORAL 3": (205, 91, 69),
    "CORAL 4": (139, 62, 47),
    "CORNFLOWER BLUE": (100, 149, 237),
    "CORNSILK": (255, 248, 220),
    "CORNSILK 1": (238, 232, 205),
    "CORNSILK 2": (205, 200, 177),
    "CORNSILK 3": (139, 136, 120),
    "CRIMSON": (220, 20, 60),
    "CYAN": (0, 255, 255),
    "CYAN 2": (0, 238, 238),
    "CYAN 3": (0, 205, 205),
    "CYAN 4": (0, 139, 139),
    "DARK GOLDENROD": (184, 134, 11),
    "DARK GOLDENROD 1": (255, 185, 15),
    "DARK GOLDENROD 2": (238, 173, 14),
    "DARK GOLDENROD 3": (205, 149, 12),
    "DARK GOLDENROD 4": (139, 101, 8),
    "DARK GRAY": (169, 169, 169),
    "DARK GREEN": (0, 100, 0),
    "DARK KHAKI": (189, 183, 107),
    "DARK OLIVE GREEN": (85, 107, 47),
    "DARK OLIVE GREEN 1": (202, 255, 112),
    "DARK OLIVE GREEN 2": (188, 238, 104),
    "DARK OLIVE GREEN 3": (162, 205, 90),
    "DARK OLIVE GREEN 4": (110, 139, 61),
    "DARK ORANGE": (255, 140, 0),
    "DARK ORANGE 1": (255, 127, 0),
    "DARK ORANGE 2": (238, 118, 0),
    "DARK ORANGE 3": (205, 102, 0),
    "DARK ORANGE 4": (139, 69, 0),
    "DARK ORCHID": (153, 50, 204),
    "DARK ORCHID 1": (191, 62, 255),
    "DARK ORCHID 2": (178, 58, 238),
    "DARK ORCHID 3": (154, 50, 205),
    "DARK ORCHID 4": (104, 34, 139),
    "DARK SALMON": (233, 150, 122),
    "DARK SEA GREEN": (143, 188, 143),
    "DARK SEA GREEN 1": (193, 255, 193),
    "DARK SEA GREEN 2": (180, 238, 180),
    "DARK SEA GREEN 3": (155, 205, 155),
    "DARK SEA GREEN 4": (105, 139, 105),
    "DARK SLATE BLUE": (72, 61, 139),
    "DARK SLATE GRAY": (47, 79, 79),
    "DARK SLATE GRAY 1": (151, 255, 255),
    "DARK SLATE GRAY 2": (141, 238, 238),
    "DARK SLATE GRAY 3": (121, 205, 205),
    "DARK SLATE GRAY 4": (82, 139, 139),
    "DARK TURQUOISE": (0, 206, 209),
    "DARK VIOLET": (148, 0, 211),
    "DEEP PINK": (255, 20, 147),
    "DEEP PINK 1": (238, 18, 137),
    "DEEP PINK 2": (205, 16, 118),
    "DEEP PINK 3": (139, 10, 80),
    "DEEP SKYBLUE": (0, 191, 255),
    "DEEP SKYBLUE 1": (0, 178, 238),
    "DEEP SKYBLUE 2": (0, 154, 205),
    "DEEP SKYBLUE 3": (0, 104, 139),
    "DIM GRAY": (105, 105, 105),
    "DODGERBLUE": (30, 144, 255),
    "DODGERBLUE 1": (28, 134, 238),
    "DODGERBLUE 2": (24, 116, 205),
    "DODGERBLUE 3": (16, 78, 139),
    "EGGSHELL": (252, 230, 201),
    "EMERALD GREEN": (0, 201, 87),
    "FIREBRICK": (178, 34, 34),
    "FIREBRICK 1": (255, 48, 48),
    "FIREBRICK 2": (238, 44, 44),
    "FIREBRICK 3": (205, 38, 38),
    "FIREBRICK 4": (139, 26, 26),
    "FLESH": (255, 125, 64),
    "FLORAL WHITE": (255, 250, 240),
    "FOREST GREEN": (34, 139, 34),
    "GAINSBORO": (220, 220, 220),
    "GHOST WHITE": (248, 248, 255),
    "GOLD": (255, 215, 0),
    "GOLD 1": (238, 201, 0),
    "GOLD 2": (205, 173, 0),
    "GOLD 3": (139, 117, 0),
    "GOLDENROD": (218, 165, 32),
    "GOLDENROD 1": (255, 193, 37),
    "GOLDENROD 2": (238, 180, 34),
    "GOLDENROD 3": (205, 155, 29),
    "GOLDENROD 4": (139, 105, 20),
    "GRAY": (128, 128, 128),
    "GRAY 1": (3, 3, 3),
    "GRAY 10": (26, 26, 26),
    "GRAY 11": (28, 28, 28),
    "GRAY 12": (31, 31, 31),
    "GRAY 13": (33, 33, 33),
    "GRAY 14": (36, 36, 36),
    "GRAY 15": (38, 38, 38),
    "GRAY 16": (41, 41, 41),
    "GRAY 17": (43, 43, 43),
    "GRAY 18": (46, 46, 46),
    "GRAY 19": (48, 48, 48),
    "GRAY 2": (5, 5, 5),
    "GRAY 20": (51, 51, 51),
    "GRAY 21": (54, 54, 54),
    "GRAY 22": (56, 56, 56),
    "GRAY 23": (59, 59, 59),
    "GRAY 24": (61, 61, 61),
    "GRAY 25": (64, 64, 64),
    "GRAY 26": (66, 66, 66),
    "GRAY 27": (69, 69, 69),
    "GRAY 28": (71, 71, 71),
    "GRAY 29": (74, 74, 74),
    "GRAY 3": (8, 8, 8),
    "GRAY 30": (77, 77, 77),
    "GRAY 31": (79, 79, 79),
    "GRAY 32": (82, 82, 82),
    "GRAY 33": (84, 84, 84),
    "GRAY 34": (87, 87, 87),
    "GRAY 35": (89, 89, 89),
    "GRAY 36": (92, 92, 92),
    "GRAY 37": (94, 94, 94),
    "GRAY 38": (97, 97, 97),
    "GRAY 39": (99, 99, 99),
    "GRAY 4": (10, 10, 10),
    "GRAY 40": (102, 102, 102),
    "GRAY 42": (107, 107, 107),
    "GRAY 43": (110, 110, 110),
    "GRAY 44": (112, 112, 112),
    "GRAY 45": (115, 115, 115),
    "GRAY 46": (117, 117, 117),
    "GRAY 47": (120, 120, 120),
    "GRAY 48": (122, 122, 122),
    "GRAY 49": (125, 125, 125),
    "GRAY 5": (13, 13, 13),
    "GRAY 50": (127, 127, 127),
    "GRAY 51": (130, 130, 130),
    "GRAY 52": (133, 133, 133),
    "GRAY 53": (135, 135, 135),
    "GRAY 54": (138, 138, 138),
    "GRAY 55": (140, 140, 140),
    "GRAY 56": (143, 143, 143),
    "GRAY 57": (145, 145, 145),
    "GRAY 58": (148, 148, 148),
    "GRAY 59": (150, 150, 150),
    "GRAY 6": (15, 15, 15),
    "GRAY 60": (153, 153, 153),
    "GRAY 61": (156, 156, 156),
    "GRAY 62": (158, 158, 158),
    "GRAY 63": (161, 161, 161),
    "GRAY 64": (163, 163, 163),
    "GRAY 65": (166, 166, 166),
    "GRAY 66": (168, 168, 168),
    "GRAY 67": (171, 171, 171),
    "GRAY 68": (173, 173, 173),
    "GRAY 69": (176, 176, 176),
    "GRAY 7": (18, 18, 18),
    "GRAY 70": (179, 179, 179),
    "GRAY 71": (181, 181, 181),
    "GRAY 72": (184, 184, 184),
    "GRAY 73": (186, 186, 186),
    "GRAY 74": (189, 189, 189),
    "GRAY 75": (191, 191, 191),
    "GRAY 76": (194, 194, 194),
    "GRAY 77": (196, 196, 196),
    "GRAY 78": (199, 199, 199),
    "GRAY 79": (201, 201, 201),
    "GRAY 8": (20, 20, 20),
    "GRAY 80": (204, 204, 204),
    "GRAY 81": (207, 207, 207),
    "GRAY 82": (209, 209, 209),
    "GRAY 83": (212, 212, 212),
    "GRAY 84": (214, 214, 214),
    "GRAY 85": (217, 217, 217),
    "GRAY 86": (219, 219, 219),
    "GRAY 87": (222, 222, 222),
    "GRAY 88": (224, 224, 224),
    "GRAY 89": (227, 227, 227),
    "GRAY 9": (23, 23, 23),
    "GRAY 90": (229, 229, 229),
    "GRAY 91": (232, 232, 232),
    "GRAY 92": (235, 235, 235),
    "GRAY 93": (237, 237, 237),
    "GRAY 94": (240, 240, 240),
    "GRAY 95": (242, 242, 242),
    "GRAY 97": (247, 247, 247),
    "GRAY 98": (250, 250, 250),
    "GRAY 99": (252, 252, 252),
    "GREEN": (0, 255, 0),
    "GREEN 2": (0, 238, 0),
    "GREEN 3": (0, 205, 0),
    "GREEN 4": (0, 139, 0),
    "GREEN YELLOW": (173, 255, 47),
    "HONEYDEW": (240, 255, 240),
    "HONEYDEW 1": (224, 238, 224),
    "HONEYDEW 2": (193, 205, 193),
    "HONEYDEW 3": (131, 139, 131),
    "HOT PINK": (255, 105, 180),
    "HOT PINK 1": (255, 110, 180),
    "HOT PINK 2": (238, 106, 167),
    "HOT PINK 3": (205, 96, 144),
    "HOT PINK 4": (139, 58, 98),
    "INDIAN RED": (205, 92, 92),
    "INDIAN RED 1": (255, 106, 106),
    "INDIAN RED 2": (238, 99, 99),
    "INDIAN RED 3": (205, 85, 85),
    "INDIAN RED 4": (139, 58, 58),
    "INDIGO": (75, 0, 130),
    "IVORY": (255, 255, 240),
    "IVORY 1": (238, 238, 224),
    "IVORY 2": (205, 205, 193),
    "IVORY 3": (139, 139, 131),
    "IVORY BLACK": (41, 36, 33),
    "KELLY GREEN": (0, 128, 0),
    "KHAKI": (240, 230, 140),
    "KHAKI 1": (255, 246, 143),
    "KHAKI 2": (238, 230, 133),
    "KHAKI 3": (205, 198, 115),
    "KHAKI 4": (139, 134, 78),
    "LAVENDER": (230, 230, 250),
    "LAVENDER BLUSH": (255, 240, 245),
    "LAVENDER BLUSH 1": (238, 224, 229),
    "LAVENDER BLUSH 2": (205, 193, 197),
    "LAVENDER BLUSH 3": (139, 131, 134),
    "LAWN GREEN": (124, 252, 0),
    "LEMON CHIFFON": (255, 250, 205),
    "LEMON CHIFFON 1": (238, 233, 191),
    "LEMON CHIFFON 2": (205, 201, 165),
    "LEMON CHIFFON 3": (139, 137, 112),
    "LIGHT BLUE": (173, 216, 230),
    "LIGHT BLUE 1": (191, 239, 255),
    "LIGHT BLUE 2": (178, 223, 238),
    "LIGHT BLUE 3": (154, 192, 205),
    "LIGHT BLUE 4": (104, 131, 139),
    "LIGHT CORAL": (240, 128, 128),
    "LIGHT CYAN": (224, 255, 255),
    "LIGHT CYAN 1": (209, 238, 238),
    "LIGHT CYAN 2": (180, 205, 205),
    "LIGHT CYAN 3": (122, 139, 139),
    "LIGHT GOLDENROD": (255, 236, 139),
    "LIGHT GOLDENROD 1": (238, 220, 130),
    "LIGHT GOLDENROD 2": (205, 190, 112),
    "LIGHT GOLDENROD 3": (139, 129, 76),
    "LIGHT GOLDENROD YELLOW": (250, 250, 210),
    "LIGHT GREY": (211, 211, 211),
    "LIGHT PINK": (255, 182, 193),
    "LIGHT PINK 1": (255, 174, 185),
    "LIGHT PINK 2": (238, 162, 173),
    "LIGHT PINK 3": (205, 140, 149),
    "LIGHT PINK 4": (139, 95, 101),
    "LIGHT SALMON": (255, 160, 122),
    "LIGHT SALMON 1": (238, 149, 114),
    "LIGHT SALMON 2": (205, 129, 98),
    "LIGHT SALMON 3": (139, 87, 66),
    "LIGHT SEA GREEN": (32, 178, 170),
    "LIGHT SKY BLUE": (135, 206, 250),
    "LIGHT SKY BLUE 1": (176, 226, 255),
    "LIGHT SKY BLUE 2": (164, 211, 238),
    "LIGHT SKY BLUE 3": (141, 182, 205),
    "LIGHT SKY BLUE 4": (96, 123, 139),
    "LIGHT SLATE BLUE": (132, 112, 255),
    "LIGHT SLATE GRAY": (119, 136, 153),
    "LIGHT STEEL BLUE": (176, 196, 222),
    "LIGHT STEEL BLUE 1": (202, 225, 255),
    "LIGHT STEEL BLUE 2": (188, 210, 238),
    "LIGHT STEEL BLUE 3": (162, 181, 205),
    "LIGHT STEEL BLUE 4": (110, 123, 139),
    "LIGHT YELLOW 1": (255, 255, 224),
    "LIGHT YELLOW 2": (238, 238, 209),
    "LIGHT YELLOW 3": (205, 205, 180),
    "LIGHT YELLOW 4": (139, 139, 122),
    "LIME GREEN": (50, 205, 50),
    "LINEN": (250, 240, 230),
    "MAGENTA": (255, 0, 255),
    "MAGENTA 2": (238, 0, 238),
    "MAGENTA 3": (205, 0, 205),
    "MAGENTA 4": (139, 0, 139),
    "MANGANESE BLUE": (3, 168, 158),
    "MAROON": (128, 0, 0),
    "MAROON 1": (255, 52, 179),
    "MAROON 2": (238, 48, 167),
    "MAROON 3": (205, 41, 144),
    "MAROON 4": (139, 28, 98),
    "MEDIUM ORCHID": (186, 85, 211),
    "MEDIUM ORCHID 1": (224, 102, 255),
    "MEDIUM ORCHID 2": (209, 95, 238),
    "MEDIUM ORCHID 3": (180, 82, 205),
    "MEDIUM ORCHID 4": (122, 55, 139),
    "MEDIUM PURPLE": (147, 112, 219),
    "MEDIUM PURPLE 1": (171, 130, 255),
    "MEDIUM PURPLE 2": (159, 121, 238),
    "MEDIUM PURPLE 3": (137, 104, 205),
    "MEDIUM PURPLE 4": (93, 71, 139),
    "MEDIUM SEA GREEN": (60, 179, 113),
    "MEDIUM SLATE BLUE": (123, 104, 238),
    "MEDIUM SPRING GREEN": (0, 250, 154),
    "MEDIUM TURQUOISE": (72, 209, 204),
    "MEDIUM VIOLET RED": (199, 21, 133),
    "MELON": (227, 168, 105),
    "MIDNIGHT BLUE": (25, 25, 112),
    "MINT": (189, 252, 201),
    "MINT CREAM": (245, 255, 250),
    "MISTY ROSE": (255, 228, 225),
    "MISTY ROSE 1": (238, 213, 210),
    "MISTY ROSE 2": (205, 183, 181),
    "MISTY ROSE 3": (139, 125, 123),
    "MOCCASIN": (255, 228, 181),
    "NAVAJO WHITE": (255, 222, 173),
    "NAVAJO WHITE 1": (238, 207, 161),
    "NAVAJO WHITE 2": (205, 179, 139),
    "NAVAJO WHITE 3": (139, 121, 94),
    "NAVY": (0, 0, 128),
    "OLD LACE": (253, 245, 230),
    "OLIVE": (128, 128, 0),
    "OLIVE DRAB": (192, 255, 62),
    "OLIVE DRAB 1": (179, 238, 58),
    "OLIVE DRAB 2": (154, 205, 50),
    "OLIVE DRAB 3": (105, 139, 34),
    "ORANGE": (255, 128, 0),
    "ORANGE 1": (255, 165, 0),
    "ORANGE 2": (238, 154, 0),
    "ORANGE 3": (205, 133, 0),
    "ORANGE 4": (139, 90, 0),
    "ORANGE 5": (245, 102, 0),
    "ORANGE RED": (255, 69, 0),
    "ORANGE RED 1": (238, 64, 0),
    "ORANGE RED 2": (205, 55, 0),
    "ORANGE RED 3": (139, 37, 0),
    "ORCHID": (218, 112, 214),
    "ORCHID 1": (255, 131, 250),
    "ORCHID 2": (238, 122, 233),
    "ORCHID 3": (205, 105, 201),
    "ORCHID 4": (139, 71, 137),
    "PALE GOLDENROD": (238, 232, 170),
    "PALE GREEN": (152, 251, 152),
    "PALE GREEN 1": (154, 255, 154),
    "PALE GREEN 2": (144, 238, 144),
    "PALE GREEN 3": (124, 205, 124),
    "PALE GREEN 4": (84, 139, 84),
    "PALE TURQUOISE": (187, 255, 255),
    "PALE TURQUOISE 1": (174, 238, 238),
    "PALE TURQUOISE 2": (150, 205, 205),
    "PALE TURQUOISE 3": (102, 139, 139),
    "PALE VIOLET RED": (219, 112, 147),
    "PALE VIOLET RED 1": (255, 130, 171),
    "PALE VIOLET RED 2": (238, 121, 159),
    "PALE VIOLET RED 3": (205, 104, 137),
    "PALE VIOLET RED 4": (139, 71, 93),
    "PAPAYA WHIP": (255, 239, 213),
    "PEACH PUFF": (255, 218, 185),
    "PEACH PUFF 1": (238, 203, 173),
    "PEACH PUFF 2": (205, 175, 149),
    "PEACH PUFF 3": (139, 119, 101),
    "PEACOCK": (51, 161, 201),
    "PINK": (255, 192, 203),
    "PINK 1": (255, 181, 197),
    "PINK 2": (238, 169, 184),
    "PINK 3": (205, 145, 158),
    "PINK 4": (139, 99, 108),
    "PLUM": (221, 160, 221),
    "PLUM 1": (255, 187, 255),
    "PLUM 2": (238, 174, 238),
    "PLUM 3": (205, 150, 205),
    "PLUM 4": (139, 102, 139),
    "POWDER BLUE": (176, 224, 230),
    "PURPLE": (128, 0, 128),
    "PURPLE 1": (155, 48, 255),
    "PURPLE 2": (145, 44, 238),
    "PURPLE 3": (125, 38, 205),
    "PURPLE 4": (85, 26, 139),
    "RASPBERRY": (135, 38, 87),
    "RAW SIENNA": (199, 97, 20),
    "RED": (255, 0, 0),
    "RED 1": (238, 0, 0),
    "RED 2": (205, 0, 0),
    "RED 3": (139, 0, 0),
    "ROSY BROWN": (188, 143, 143),
    "ROSY BROWN 1": (255, 193, 193),
    "ROSY BROWN 2": (238, 180, 180),
    "ROSY BROWN 3": (205, 155, 155),
    "ROSY BROWN 4": (139, 105, 105),
    "ROYAL BLUE": (65, 105, 225),
    "ROYAL BLUE 1": (72, 118, 255),
    "ROYAL BLUE 2": (67, 110, 238),
    "ROYAL BLUE 3": (58, 95, 205),
    "ROYAL BLUE 4": (39, 64, 139),
    "SALMON": (250, 128, 114),
    "SALMON 1": (255, 140, 105),
    "SALMON 2": (238, 130, 98),
    "SALMON 3": (205, 112, 84),
    "SALMON 4": (139, 76, 57),
    "SANDY BROWN": (244, 164, 96),
    "SAP GREEN": (48, 128, 20),
    "SEA GREEN": (84, 255, 159),
    "SEA GREEN 1": (78, 238, 148),
    "SEA GREEN 2": (67, 205, 128),
    "SEA GREEN 3": (46, 139, 87),
    "SEASHELL": (255, 245, 238),
    "SEASHELL 1": (238, 229, 222),
    "SEASHELL 2": (205, 197, 191),
    "SEASHELL 3": (139, 134, 130),
    "SEPIA": (94, 38, 18),
    "SIENNA": (160, 82, 45),
    "SIENNA 1": (255, 130, 71),
    "SIENNA 2": (238, 121, 66),
    "SIENNA 3": (205, 104, 57),
    "SIENNA 4": (139, 71, 38),
    "SILVER": (192, 192, 192),
    "SKY BLUE": (135, 206, 235),
    "SKY BLUE 1": (135, 206, 255),
    "SKY BLUE 2": (126, 192, 238),
    "SKY BLUE 3": (108, 166, 205),
    "SKY BLUE 4": (74, 112, 139),
    "SKY BLUE 5": (185, 217, 235),
    "SLATE BLUE": (106, 90, 205),
    "SLATE BLUE 1": (131, 111, 255),
    "SLATE BLUE 2": (122, 103, 238),
    "SLATE BLUE 3": (105, 89, 205),
    "SLATE BLUE 4": (71, 60, 139),
    "SLATE GRAY": (112, 128, 144),
    "SLATE GRAY 1": (198, 226, 255),
    "SLATE GRAY 2": (185, 211, 238),
    "SLATE GRAY 3": (159, 182, 205),
    "SLATE GRAY 4": (108, 123, 139),
    "SNOW": (255, 250, 250),
    "SNOW 1": (238, 233, 233),
    "SNOW 2": (205, 201, 201),
    "SNOW 3": (139, 137, 137),
    "SPRING GREEN": (0, 255, 127),
    "SPRING GREEN 1": (0, 238, 118),
    "SPRING GREEN 2": (0, 205, 102),
    "SPRING GREEN 3": (0, 139, 69),
    "STEEL BLUE": (70, 130, 180),
    "STEEL BLUE 1": (99, 184, 255),
    "STEEL BLUE 2": (92, 172, 238),
    "STEEL BLUE 3": (79, 148, 205),
    "STEEL BLUE 4": (54, 100, 139),
    "TAN": (210, 180, 140),
    "TAN 1": (255, 165, 79),
    "TAN 2": (238, 154, 73),
    "TAN 3": (205, 133, 63),
    "TAN 4": (139, 90, 43),
    "TEAL": (0, 128, 128),
    "THISTLE": (216, 191, 216),
    "THISTLE 1": (255, 225, 255),
    "THISTLE 2": (238, 210, 238),
    "THISTLE 3": (205, 181, 205),
    "THISTLE 4": (139, 123, 139),
    "TOMATO": (255, 99, 71),
    "TOMATO 1": (238, 92, 66),
    "TOMATO 2": (205, 79, 57),
    "TOMATO 3": (139, 54, 38),
    "TURQUOISE": (64, 224, 208),
    "TURQUOISE 1": (0, 245, 255),
    "TURQUOISE 2": (0, 229, 238),
    "TURQUOISE 3": (0, 197, 205),
    "TURQUOISE 4": (0, 134, 139),
    "TURQUOISE BLUE": (0, 199, 140),
    "VIOLET": (238, 130, 238),
    "VIOLET RED": (208, 32, 144),
    "VIOLET RED 1": (255, 62, 150),
    "VIOLET RED 2": (238, 58, 140),
    "VIOLET RED 3": (205, 50, 120),
    "VIOLET RED 4": (139, 34, 82),
    "WARM GREY": (128, 128, 105),
    "WHEAT": (245, 222, 179),
    "WHEAT 1": (255, 231, 186),
    "WHEAT 2": (238, 216, 174),
    "WHEAT 3": (205, 186, 150),
    "WHEAT 4": (139, 126, 102),
    "WHITE": (255, 255, 255),
    "WHITE SMOKE": (245, 245, 245),
    "YELLOW": (255, 255, 0),
    "YELLOW 1": (238, 238, 0),
    "YELLOW 2": (205, 205, 0),
    "YELLOW 3": (139, 139, 0),
}
