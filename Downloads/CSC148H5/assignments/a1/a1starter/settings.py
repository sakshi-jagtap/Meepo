import os

##########################################################
#                      COLOURS                           #
##########################################################
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
ORANGE = (255, 165, 0)
GREEN = (0, 128, 0)
RED = (100, 0, 0)
BLUE = (30, 144, 255)
DARKBLUE = (0, 0, 205)
PURPLE = (102, 0, 204)
YELLOW = (255, 255, 0)


##########################################################
#                     SPECIFICATION                      #
##########################################################

FPS = 10
TITLE = "Base Game"
TILESIZE = 35

SUBJECTS = {"W": "Wall", "R": "Rock", "F": "Flag", "M": "Meepo"}
ATTRIBUTES = {"P": "Push", "S": "Stop", "V": "Victory", "L": "Lose", "Y": "You"}
CHARACTERS = {"1": "Bush", "2": "Meepo", "3": "Wall", "4": "Rock", "5": "Flag"}

BASE_DIR = "."
SPRITES_DIR = "{}/sprites".format(BASE_DIR)
MAP_PATH = "{}/maps/map.txt".format(BASE_DIR)
# MAP_PATH = "{}/maps/student_map5.txt".format(BASE_DIR)

# Actors' sprites
PLAYER_SPRITE_R1 = "{}/playerR1.png".format(SPRITES_DIR)
PLAYER_SPRITE_R2 = "{}/playerR2.png".format(SPRITES_DIR)
PLAYER_SPRITE_U1 = "{}/playerU1.png".format(SPRITES_DIR)
PLAYER_SPRITE_U2 = "{}/playerU2.png".format(SPRITES_DIR)
PLAYER_SPRITE_B1 = "{}/playerB1.png".format(SPRITES_DIR)
PLAYER_SPRITE_B2 = "{}/playerB2.png".format(SPRITES_DIR)

BUSH_SPRITE = "{}/bush.png".format(SPRITES_DIR)
WALL_SPRITE = "{}/wallS.png".format(SPRITES_DIR)
ROCK_SPRITE = "{}/rockS.png".format(SPRITES_DIR)
FLAG_SPRITE = "{}/flagS.png".format(SPRITES_DIR)

IS_PURPLE = "{}/isPurple.png".format(SPRITES_DIR)
IS_DARK_BLUE = "{}/isDarkBlue.png".format(SPRITES_DIR)
IS_LIGHT_BLUE = "{}/isLightBlue.png".format(SPRITES_DIR)

WORDS_SPRITES = {}
for word in (list(SUBJECTS.values()) + list(ATTRIBUTES.values())):
    filepath = "{}/{}.png".format(SPRITES_DIR, word.lower())
    if os.path.exists(filepath):
        WORDS_SPRITES[word.lower()] = filepath
