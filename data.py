# ============================================ #
#                                              #
#   This is the data to build the csuf map     #
# ============================================ #          
#==============================================#

import random
import math

# Method for calculating the distance
def distance(a, b, c, d):
    x = ((a-c)**2 + (b-d)**2)**0.5*2.
    return round(x, 2)

# Method for random color
def generate_color():
    color = random.randrange(0, 2**24)
    hex_color = hex(color)
    std_color = "#" + hex_color[2:]
    return(std_color)


# List for nodes position
#=========================
positions = { 
        # entrance (10, 1->9)
        0: (249, 768),   #10     
        1: (366, 156),   #1->9
        2: (198, 156),  
        3: (125, 148),
        4: (61, 247),
        5: (61, 356),
        6: (61, 472),
        7: (61, 528),
        8: (61, 617),
        9: (156, 750),
        
        
        # parking lot
        10: (145, 675),   #lot A       
        11: (120, 570),   #lot A-south
        12: (160, 510),   #lot D
        13: (120, 468),   #lot SCPS
        14: (55, 286),    #Titan Hall lot
        15: (142, 195),   #lot NPS
        16: (123, 181),   #lot C-west  
        17: (195, 184),   #lot C-east
        18: (375, 143),   #lot CP-north
        19: (375, 108),   #lot CP-south
        
        20: (375, 75),    #lot S
        21: (337, 290),   #lot F
        22: (350, 340),   #lot I
        23: (443, 285),   #lot ESPS
        24: (443, 327),   #lot ENPS
        25: (443, 360),   #Resident Lot 2
        26: (435, 437),   #Resident Lot 1
        27: (363, 437),   #lot J
        28: (330, 475),   #lot H
        29: (266, 703),   #Aboretum parking
        
        30: (219, 701),   #lot G
        
        
        #TSC Fields
        31: (190, 637),   #TS
        32: (252, 657),   #GF 
        33: (265, 615),   #AF
        34: (237, 560),   #TTF
        35: (185, 514),   #TTC
        36: (289, 557),   #TSF
        37: (227, 514),   #IF
        38: (265, 514),   #EP
        
        
        #CSUF Aboretum 
        39: (343, 627),   # Aboretum/Bonatical garden
        40: (309, 672),   # Heritage house
        
        
        # Resident Housing 
        #and North buildinds
        41: (395, 490),   #RH
        42: (401, 456),   #GAS
        43: (423, 483),   #HRE
        
        44: (349, 452),   #RG
        45: (315, 483),   #T
        46: (314, 505),   #MS
        
        47: (115, 591),   #CC
        48: (96, 516),    #CY
        
        
        #South-West buldings
        49: (81, 433),    #UP
        50: (152, 433),   #SRC  
        51: (81, 396),    #GAH 
        52: (114, 360),   #TSU
        53: (105, 311),   #VA     
        
        54: (27, 345),    #ASC
        55: (48, 330),    #TH
        
        56: (218, 443),   #TG
        57: (222, 410),   #KHS
        58: (202, 375),   #B 
        59: (259, 340),   #PL
        60: (195, 285),   #CPAC
        
        61: (195, 250),   #GC    
        62: (234, 252),   #MH
        63: (243, 220),   #DBH
        64: (234, 185),   #MC
        
        
        #South-East buldings
        65: (308, 447),   #SHCC
        66: (352, 407),   #E
        67: (376, 407),   #CS
        68: (309, 341),   #EC  
        
        69: (302, 295),   #H
        70: (309, 240),   #GH
        71: (287, 218),   #LH    
        72: (310, 211),   #AD
        73: (324, 223),   #CJ
        74: (342, 191),   #SGMH
        
        75: (403, 194),   #Marriot
        76: (345, 131),   #CP
        
        #Additional nodes
        77: (90, 370),   # temp parking nearby TSU building (ADD-Lot-1)
        78: (105, 338)   # temp parking between TSU and VA  (ADD-Lot-2)
}



location_names = [ 
        # entrance (10, 1->9)
        "Entrance 10",   #10     
        "Entrance 1",   #1->9
        "Entrance 2",  
        "Entrance 3",
        "Entrance 4",
        "Entrance 5",
        "Entrance 6",
        "Entrance 7",
        "Entrance 8",
        "Entrance 9",
        
        
        # parking lot (ID: 10-30)
        "Parking Lot A",        #lot A          ID=10       
        "Parking Lot A South",  #lot A-south    ID=11
        "Parking Lot D",                       #ID=12
        "State College Parking Structure",     #ID=13
        "Titan Hall Lot",                      #ID=14
        "Nutwood Parking Structure",   
        "Parking Lot C West",   #lot C-west
        "Parking Lot C East",   #lot C-east
        "College Park Parking North",   #lot CP-north
        "College Park Parking South",   #lot CP-south
        
        "Parking Lot S",   #lot S
        "Parking Lot F",   #lot F
        "Parking Lot I",   #lot I
        "Eastside South Parking Structure",   #lot ESPS
        "Eastside North Parking Structure",   #lot ENPS
        "Resident Lot 2",   #Resident Lot 2
        "Resident Lot 1",   #Resident Lot 1
        "Parking Lot J",   #lot J
        "Parking Lot H",   #lot H
        "Aboretum Parking",   #Aboretum parking
        
        "Parking Lot G",   #lot G
        
        
        #TSC Fields
        "Titan Stadium",   #TS
        "Goodwin Field",   #GF 
        "Anderson Field",  #AF
        "Titan Track & Field",  #TTF
        "Titan Tenis Courts",   #TTC
        "Titan Softball Field", #TSF
        "Intramural Field",   #IF
        "East Playfield",     #EP
        
        
        #CSUF Aboretum 
        "Aboretum/Bonatical Garden",   # Aboretum/Bonatical garden
        "Heritage House",   # Heritage house
        
        
        # Resident Housing 
        #and North buildinds
        "Resident Housing",                   #RH
        "Gastronome",                         #GAS
        "Housing & Residential Engagement",   #HRE
        
        "Ruby Gerontology Center",  #RG
        "Titan House",              #T
        "Military Science",         #MS
        
        "Children's Center",   #CC
        "Corporation Yard",    #CY
        
        
        #South-West buldings
        "University Police",           #UP
        "Student Recreation Center",   #SRC  
        "Golleher Alumni House",       #GAH 
        "Titan Student Union",         #TSU
        "Visual Arts Center",          #VA
        
        "Auxiliary Services Corporation",    #ASC
        "Titan Hall",    #TH
        
        "Titan Gymnasium",   #TG
        "Kinesiology & Health Sciences",   #KHS
        "Bookstore",         #B 
        "Pollark Library",   #PL
        "Clayes Performing Arts Center",   #CPAC
        
        "Greenhouse Complex",   #GC
        "McCarthy Hall",   #MH
        "Dan Black Hall",   #DBH
        "Modular Complex",   #MC
        
        
        #South-East buldings
        "Student Health & Counseling Center",   #SHCC
        "Engineering",          #E
        "Computer Science",     #CS
        "Education Classroom",  #EC  
        
        "Humanities",    #H
        "Gordon Hall",   #GH
        "Langsdorf Hall",      #LH
        "Admissions Office",   #AD
        "Carl's Jr.",    #CJ
        "Steven G. Mihaylo Hall",   #SGMH
        
        "Fullerton Marriott",   #Marriot
        "College Park",   #CP
        
        #Additional nodes
        "Additional parking 1",   # temp parking nearby TSU building (ADD-Lot-1)
        "Additional parking 2"    # temp parking between TSU and VA  (ADD-Lot-2)
]


# List for the edges aka (node, node, distance)
#==============================================

edges = [
    # ENTRANCE 
    # entrance 10
    (0, 9, distance(249, 768, 156, 750)),  #to entrance 9
    (0, 29, distance(249, 768, 266, 703)), #to arboretum parking
    (0, 30, distance(249, 768, 219, 701)), #to lot G
    
    # entrance 1
    (1, 2, distance(366, 156, 198, 156)),  #to entrance 2
    (1, 18, distance(366, 156, 375, 150)), #to lot CP-north
    (1, 21, distance(366, 156, 337, 290)), #to lot F
    (1, 23, distance(366, 156, 443, 285)),  #to lot ESPS
    
    # entrance 2
    (2, 3, distance(198, 156, 125, 148)),  #to entrance 3
    (2, 17, distance(198, 156, 195, 184)), #to lot C-east 
    (2, 19, distance(198, 156, 375, 108)), #to lot CP-south
    (2, 20, distance(198, 156, 375, 75)),  #to lot S
    
    # entrance 3
    (3, 4, distance(148, 153, 61, 247)),   #to entrance 4
    (3, 15, distance(148, 153, 142, 195)), #to lot NPS
    (3, 16, distance(148, 153, 123, 181)), #to lot C-west 
    
    # entrance 4
    (4, 5, distance(61, 247, 61, 356)),    #to entrance 5
    (4, 14, distance(61, 247, 55, 286)),   #to Titan Hall lot
    (4, 15, distance(61, 247, 142, 195)),  #to lot NPS
    
    
    # entrance 5
    (5, 6, distance(61, 356, 61, 472)),     #to entrance 6
    (5, 14, distance(61, 356, 55, 286)),    #to Titan Hall Lot
    #(5, 49, distance(61, 358, 81, 433)),   #to UP
    #(5, 51, distance(61, 358, 81, 396)),   #to GAH
    #(5, 52, distance(61, 358, 114, 360)),  #to TSU
    #(5, 53, distance(61, 358, 105, 317)),  #to VA
    #(5, 54, distance(61, 358, 27, 345)),   #to ASC
    #(5, 55, distance(61, 358, 48, 330)),   #to TH
    (5, 77, distance(61, 356, 90, 370)),    #to ADD-Lot-1
    (5, 78, distance(61, 356, 105, 338)),   #to ADD-Lot-2
    
    
    # entrance 6
    (6, 7, distance(61, 472, 61, 528)),   #to entrance 7
    (6, 13, distance(61, 472, 120, 468)), #to lot SCPS
    #(6, 48, distance(61, 472, 96, 516)),  #to CY
    #(6, 49, distance(61, 472, 81, 433)),  #to UP
    #(6, 51, distance(61, 472, 81, 396)),  #to GAH
    
    
    # entrance 7
    (7, 8, distance(61, 528, 61, 617)),    #to entrance 8
    (7, 11, distance(61, 528, 120, 570)),  #to lot A-south
    (7, 12, distance(61, 528, 160, 510)),  #to lot D
    #(7, 47, distance(61, 528, 115, 591)),  #to CC
    #(7, 48, distance(61, 528, 96, 516)),   #to CY
    
    # entrance 8
    (8, 9, distance(61, 617, 156, 750)),  #to entrance 9
    (8, 10, distance(61, 617, 145, 675)), #to lot A
    (8, 11, distance(61, 617, 120, 570)), #to lot A-south
    #(8, 47, distance(61, 617, 115, 591)), #to CC
    
    # entrance 9
    (9, 10, distance(156, 750, 145, 675)), #to lot A
    (9, 30, distance(156, 750, 219, 701)), #to lot G
    
    
    # PARKING LOT ==========================================
    # parking lot A
    (10, 11, distance(145, 675, 120, 570)), #to lot A-south
    (10, 30, distance(145, 675, 219, 701)), #to lot G
    (10, 31, distance(145, 675, 190, 637)), #to TS field
    (10, 32, distance(145, 675, 252, 657)), #to GF field
    (10, 47, distance(145, 675, 115, 591)), #to CC
    
    #parking lot A-south
    (11, 12, distance(120, 570, 160, 510)), #to lot D
    (11, 13, distance(120, 570, 120, 468)), #to lot SCPS
    (11, 31, distance(120, 570, 190, 637)), #to TS field
    (11, 33, distance(120, 570, 265, 615)), #to AF field
    (11, 34, distance(120, 570, 237, 560)), #to TTF field
    (11, 35, distance(120, 570, 185, 514)), #to TTC field
    (11, 47, distance(120, 570, 115, 591)), #to CC
    (11, 48, distance(120, 570, 96, 516)),  #to CY
    
    #parking lot D
    (12, 13, distance(160, 510, 120, 468)), #to lot SCPS
    (12, 31, distance(160, 510, 190, 637)), #to TS field
    (12, 35, distance(160, 510, 185, 514)), #to TTC field
    (12, 48, distance(160, 510, 96, 516)),  #to CY
    (12, 50, distance(160, 510, 152, 433)), #to SRC
    (12, 56, distance(160, 510, 218, 443)), #to TG
    
    #parking lot SCPS
    (13, 48, distance(120, 468, 96, 516)),  #to CY
    (13, 49, distance(120, 468, 81, 433)),  #to UP
    (13, 50, distance(120, 468, 152, 433)), #to SRC
    (13, 51, distance(120, 468, 81, 396)),  #to GAH
    (13, 52, distance(120, 468, 114, 360)), #to TSU
    (13, 56, distance(120, 468, 218, 443)), #to TG
    (13, 77, distance(120, 468, 90, 370)),  #to ADD-lot-1 (parking)
    
    #Titan Hall parkings AREA
    (14, 53, distance(55, 286, 105, 311)), # to VA
    (14, 54, distance(55, 286, 27, 345)),  # to ASC
    (14, 55, distance(55, 286, 48, 330)),  # to TH
    (14, 60, distance(55, 286, 195, 285)), # to CPAC
    (14, 61, distance(55, 286, 195, 250)), # to GC
    (14, 78, distance(55, 286, 105, 338)), # to ADD-lot-2
    
    #parking lot NPS
    (15, 16, distance(142, 195, 123, 181)), # to lot C-west
    (15, 17, distance(142, 195, 195, 184)), # to lot C-east
    (15, 53, distance(142, 195, 105, 311)), # to VA
    (15, 60, distance(142, 195, 195, 285)), # to CPAC
    (15, 61, distance(142, 195, 195, 250)), # to GC
    (15, 62, distance(142, 195, 234, 252)), # to MH
    (15, 63, distance(142, 195, 243, 220)), # to DBH
    
    #parking lot C-west
    (16, 17, distance(123, 181, 195, 184)), # to lot C-east
    
    #parking lot C-east
    (17, 61, distance(195, 184, 195, 250)), # to GC
    (17, 62, distance(195, 184, 234, 252)), # to MH
    (17, 63, distance(195, 184, 243, 220)), # to DBH
    (17, 64, distance(195, 184, 234, 185)), # to MC
    
    #parking lot CP-north
    (18, 19, distance(375, 143, 375, 108)), # to lot CP-south
    (18, 64, distance(375, 143, 234, 185)), # to MC
    (18, 74, distance(375, 143, 342, 191)), # to SGMH
    (18, 75, distance(375, 143, 403, 194)), # to Marriot
    (18, 76, distance(375, 143, 345, 131)), # to CP
    
    #parking lot CP-south
    (19, 20, distance(375, 108, 375, 75)),  # to lot S
    (19, 76, distance(375, 108, 345, 131)), # to CP
    
    #parking lot S
    (20, 76, distance(375, 75, 345, 131)), # to CP
    
    #parking lot F
    (21, 22, distance(337, 290, 350, 340)), # to lot I
    (21, 23, distance(337, 290, 443, 285)), # to lot ESPS
    (21, 24, distance(337, 290, 443, 327)), # to lot ENPS
    (21, 59, distance(337, 290, 259, 340)), # to PL
    (21, 68, distance(337, 290, 309, 341)), # to EC
    (21, 69, distance(337, 290, 302, 295)), # to H
    (21, 70, distance(337, 290, 309, 240)), # to GH
    (21, 73, distance(337, 290, 324, 223)), # to CJ
    (21, 74, distance(337, 290, 342, 191)), # to SGMH
    (21, 75, distance(337, 290, 403, 194)), # to Marriot
    
    #parking lot I
    (22, 24, distance(350, 340, 443, 327)), # to lot ENPS
    (22, 25, distance(350, 340, 443, 360)), # to resident lot 2
    (22, 57, distance(350, 340, 222, 410)), # to KHS
    (22, 65, distance(350, 340, 308, 447)), # to SHCC
    (22, 66, distance(350, 340, 352, 407)), # to E
    (22, 67, distance(350, 340, 376, 407)), # to CS
    (22, 68, distance(350, 340, 309, 341)), # to EC
    (22, 69, distance(350, 340, 302, 295)), # to H
    
    #parking lot ESPS
    (23, 24, distance(443, 285, 443, 327)), # to lot ENPS
    (23, 73, distance(443, 285, 324, 223)), # to CJ
    (23, 74, distance(443, 285, 342, 191)), # to SGMH
    (23, 75, distance(443, 285, 403, 194)), # to Marriot
    
    #parking lot ENPS
    (24, 25, distance(443, 327, 443, 360)), # to resident lot 2
    
    #parking Resident Lot 2
    (25, 26, distance(443, 360, 435, 437)), # to resident lot 1
    (25, 42, distance(443, 360, 401, 456)), # to GAS
    (25, 67, distance(443, 360, 376, 407)), # to CS
    
    #parking Resident lot 1
    (26, 27, distance(435, 437, 363, 437)), # to lot J
    (26, 41, distance(435, 437, 395, 490)), # to RH
    (26, 42, distance(435, 437, 401, 456)), # to GAS
    (26, 43, distance(435, 437, 423, 483)), # to HRE
    (26, 67, distance(435, 437, 376, 407)), # to CS
    
    #parking lot J
    (27, 41, distance(363, 437, 395, 490)), # to RH
    (27, 42, distance(363, 437, 401, 456)), # to GAS
    (27, 44, distance(363, 437, 349, 452)), # to RG
    (27, 65, distance(363, 437, 308, 447)), # to SHCC
    (27, 66, distance(363, 437, 352, 407)), # to E
    (27, 67, distance(363, 437, 376, 407)), # to CS
    
    #parking lot H
    (28, 39, distance(330, 475, 343, 627)), # to Aboretum/Botanical garden
    (28, 44, distance(330, 475, 349, 452)), # to RG
    (28, 45, distance(330, 475, 315, 483)), # to T
    (28, 46, distance(330, 475, 314, 505)), # to MS
    (28, 56, distance(330, 475, 218, 443)), # to TG
    (28, 65, distance(330, 475, 308, 447)), # to SHCC
    (28, 66, distance(330, 475, 352, 407)), # to E
    
    #Aboretum parking
    (29, 30, distance(266, 703, 219, 701)), # to lot G
    (29, 31, distance(266, 703, 190, 637)), # to TS field
    (29, 32, distance(266, 703, 252, 657)), # to GF field
    (29, 40, distance(266, 703, 309, 672)), # to Heritage House
    
    #parking lot G
    (30, 31, distance(219, 701, 190, 637)), # to TS field
    (30, 32, distance(219, 701, 252, 657)), # to GF field
    (30, 34, distance(219, 701, 237, 560)), # to TTF field
    (30, 40, distance(219, 701, 309, 672)), # to Heritage House
    
    
    
    # FIELDS =============================================
    # TS field
    (31, 32, distance(190, 637, 252, 657)), # to GF field
    (31, 33, distance(190, 637, 265, 615)), # to AF field
    (31, 34, distance(190, 637, 237, 560)), # to TTF field
    (31, 35, distance(190, 637, 185, 514)), # to TTC field
    (31, 36, distance(190, 637, 289, 557)), # to TSF field
    (31, 47, distance(190, 637, 115, 591)), #to CC
    
    # GF field
    (32, 33, distance(252, 657, 265, 615)), # to AF field
    (32, 34, distance(252, 657, 237, 560)), # to TTF field
    (32, 39, distance(252, 657, 343, 627)), # to Aboretum/Botanical garden
    (32, 40, distance(252, 657, 309, 672)), # to Heritage House
    
    # AF field
    (33, 34, distance(265, 615, 237, 560)), # to TTF field
    (33, 36, distance(265, 615, 289, 557)), # to TSF field
    (33, 38, distance(265, 615, 265, 514)), # to EP field
    (33, 39, distance(265, 615, 343, 627)), # to Aboretum/Botanical garden
    (33, 40, distance(265, 615, 309, 672)), # to Heritage House
    
    # TTF field
    (34, 35, distance(237, 560, 185, 514)), # to TTC field
    (34, 36, distance(237, 560, 289, 557)), # to TSF
    (34, 37, distance(237, 560, 227, 514)), # to IF
    (34, 38, distance(237, 560, 265, 514)), # to EP
    (34, 39, distance(237, 560, 343, 627)), # to Aboretum/Botanical garden
    (34, 46, distance(237, 560, 314, 505)), # to MS (building)
    
    # TTC field
    (35, 37, distance(185, 514, 227, 514)), # to IF field
    (35, 50, distance(185, 514, 152, 433)), # to SRC
    (35, 56, distance(185, 514, 218, 443)), # to TG
    
    # TSF field
    (36, 37, distance(289, 557, 227, 514)), # to IF field
    (36, 38, distance(289, 557, 265, 514)), # to EP field
    (36, 39, distance(289, 557, 343, 627)), # to Aboretum/Botanical garden
    (36, 41, distance(289, 557, 395, 490)), # to Resident Housing (RH)
    (36, 46, distance(289, 557, 314, 505)), # to MS
    
    # IF field
    (37, 38, distance(227, 514, 265, 514)), # to EP field
    (37, 50, distance(227, 514, 152, 433)), # to SRC
    (37, 56, distance(227, 514, 218, 443)), # to TG
    (37, 65, distance(227, 514, 308, 447)), # to SHCC
    
    # EP field
    (38, 45, distance(265, 514, 315, 483)), # to T
    (38, 46, distance(265, 514, 314, 505)), # to MS
    (38, 56, distance(265, 514, 218, 443)), # to TG
    (38, 65, distance(265, 514, 308, 447)), # to SHCC
    
    # Aboretum/Botanical garden
    (39, 40, distance(343, 627, 309, 672)), # to Heritage House
    (39, 41, distance(343, 627, 395, 490)), # to Resident Housing (RH)
    (39, 44, distance(343, 627, 349, 452)), # to RG
    (39, 46, distance(343, 627, 314, 505)), # to MS
    
    # Buildings ==========================================
    # Resident Housing
    (41, 42, distance(395, 490, 401, 456)), # to GAS
    (41, 43, distance(395, 490, 423, 483)), # to HRE
    (41, 44, distance(395, 490, 349, 452)), # to RG
    
    # (GAS)tronome building
    (42, 43, distance(401, 456, 423, 483)), # to HRE
    (42, 67, distance(401, 456, 376, 407)), # to CS
    
    # Ruby Genrotology Center (RG)
    (44, 65, distance(349, 452, 308, 447)), # to SHCC
    (44, 66, distance(349, 452, 352, 407)), # to E
    
    # Titan House (T)
    (45, 46, distance(315, 483, 314, 505)), # to MS
    (45, 56, distance(315, 483, 218, 443)), # to TG
    (45, 65, distance(315, 483, 308, 447)), # to SHCC
    
    # Military Science (MS)
    (46, 56, distance(314, 505, 218, 443)), # to TG
    
    
    # Buildings (West side) =========================
    # Children's center (CC)
    
    # Corporation Yard (CY)
    (48, 49, distance(96, 516, 81, 433)),  # to UP
    
    # University Police (UP)
    (49, 50, distance(81, 433, 152, 433)), # to SRC
    (49, 51, distance(81, 433, 81, 396)),  # to GAH
    (49, 52, distance(81, 433, 114, 360)), # to TSU
    (49, 58, distance(81, 433, 202, 375)), # to B
    
    # SRC building
    (50, 51, distance(152, 433, 81, 396)),  # to GAH
    (50, 52, distance(152, 433, 114, 360)), # to TSU
    (50, 56, distance(152, 433, 218, 443)), # to TG
    (50, 57, distance(152, 433, 222, 410)), # to KHS
    (50, 58, distance(152, 433, 202, 375)), # to B
    
    # GAH buiding
    (51, 57, distance(81, 396, 222, 410)), # to KHS
    (51, 58, distance(81, 396, 202, 375)), # to B
    
    # TSU building
    (52, 58, distance(114, 360, 202, 375)), # to B
    (52, 59, distance(114, 360, 259, 340)), # to PL
    (52, 60, distance(114, 360, 195, 285)), # to CPAC
    
    # VA building
    (53, 55, distance(105, 311, 48, 330)),  # to Titan Hall
    (53, 58, distance(105, 311, 202, 375)), # to B
    (53, 59, distance(105, 311, 259, 340)), # to PL
    (53, 60, distance(105, 311, 195, 285)), # to CPAC
    (53, 61, distance(105, 311, 195, 250)), # to GC
    
    # ASC building
    (54, 55, distance(27, 345, 48, 330)),  # ASC to TH (*)
    # Titan Hall
    
    # TG building
    (56, 57, distance(218, 443, 222, 410)), # to KHS
    (56, 65, distance(218, 443, 308, 447)), # to SHCC
    
    # KHS building
    (57, 58, distance(222, 410, 202, 375)), # to B
    (57, 59, distance(222, 410, 259, 340)), # to PL
    (57, 60, distance(222, 410, 195, 285)), # to CPAC
    (57, 65, distance(222, 410, 308, 447)), # to SHCC
    
    # Bookstore (B)
    (58, 59, distance(202, 375, 259, 340)), # to PL
    (58, 60, distance(202, 375, 195, 285)), # to CPAC
    
    # Pollak Library (PL)
    (59, 60, distance(259, 340, 195, 285)), # to CPAC
    (59, 62, distance(259, 340, 234, 252)), # to MH
    (59, 65, distance(259, 340, 308, 447)), # to SHCC
    (59, 66, distance(259, 340, 352, 407)), # to E
    (59, 68, distance(259, 340, 309, 341)), # to EC
    (59, 69, distance(259, 340, 302, 295)), # to H
    
    # CPAC building
    (60, 61, distance(195, 285, 195, 250)), # to GC
    (60, 62, distance(195, 285, 234, 252)), # to MH
    (60, 69, distance(195, 285, 302, 295)), # to H
    
    # GC building
    (61, 62, distance(195, 250, 234, 252)), # to MH
    (61, 63, distance(195, 250, 243, 220)), # to DBL
    
    # MH building
    (62, 63, distance(234, 252, 243, 220)), # to DBL
    (62, 69, distance(234, 252, 302, 295)), # to H
    (62, 70, distance(234, 252, 309, 240)), # to GH
    (62, 71, distance(234, 252, 287, 218)), # to LH
    
    # DBH building
    (63, 64, distance(243, 220, 234, 185)), # to MC
    (63, 70, distance(243, 220, 309, 240)), # to GH
    (63, 71, distance(243, 220, 287, 218)), # to LH    
    (63, 74, distance(243, 220, 342, 191)), # to SGMH
    
    # MC building
    (64, 71, distance(234, 185, 287, 218)), # to LH 
    (64, 74, distance(234, 185, 342, 191)), # to SGMH
    
    
    # Buildings (South-side)===============================
    # SHCC building
    (65, 66, distance(308, 447, 352, 407)), # to E
    (65, 68, distance(308, 447, 309, 341)), # to EC
    
    # Engineering (E)
    (66, 67, distance(352, 407, 376, 407)), # to CS
    (66, 68, distance(352, 407, 309, 341)), # to EC
    
    # EC building
    (68, 69, distance(309, 341, 302, 295)), # to H
    
    # Humanity/Social science (H)
    (69, 70, distance(302, 295, 309, 240)), # to GH
    
    # Gordon Hall (GH)
    (70, 71, distance(309, 240, 287, 218)), # to LH 
    (70, 72, distance(309, 240, 310, 216)), # to AD
    (70, 73, distance(309, 240, 324, 223)), # to CJ
    
    # Langsdorf Hall (LH)
    (71, 72, distance(287, 218, 310, 216)), # to AD
    
    # Addmissions Office (AD)
    (72, 73, distance(310, 216, 324, 223)), # to CJ
    (72, 74, distance(310, 216, 342, 191)), # to SGMH
    
    # Carl's Junior (CJ)
    (73, 74, distance(324, 223, 342, 191)), # to SGMH
    
    # SGMH (Mihaylo building)
    (74, 75, distance(342, 191, 403, 194)), # to Marriot
    
    
    # Additional Parking ==================================
    #ADD-lot-1
    (51, 77, distance(90, 370, 81, 396)),   # to GAH
    (52, 77, distance(90, 370, 114, 360)),  # to TSU
    (54, 77, distance(90, 370, 27, 345)),   # to ASC
    (55, 77, distance(90, 370, 48, 330)),   # to TH
    (77, 78, distance(90, 370, 105, 338)),  # to ADD-lot 2
    
    #ADD-lot-2
    (52, 78, distance(105, 338, 114, 360)),  # to TSU
    (53, 78, distance(105, 338, 105, 317)),  # to VA
    (54, 78, distance(105, 338, 27, 345)),   # to ASC
    (55, 78, distance(105, 338, 48, 330)),   # to TH
    (59, 78, distance(105, 338, 259, 340)),  # to PL
    (60, 78, distance(105, 338, 195, 285))   # to CPAC  
]
