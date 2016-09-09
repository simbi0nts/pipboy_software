import pygame,json,requests

import RPi.GPIO as GPIO

WIDTH = 480
HEIGHT = 360

# WIDTH = 800
# HEIGHT = 480

# OUTPUT_WIDTH = 480
# OUTPUT_HEIGHT = 360

try:
    r = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyBNZXMm0TB1r6XgTl-K9JoFa68W1OSArA0")
    j = json.loads(r.text)
    j = j['location']
    lat = j['lat']
    lon = j['lng']
    lat -= 0.005
    lon -= 0.014
    lat_big = lat - 0.004
    lon_big = lon + 0.001
    MAP_FOCUS = (lon,lat)
    MAP_FOCUS_BIG = (lon_big,lat_big)   
except Exception, e:
    print "GPIO UNAVAILABLEssss (%s)" % e
    lon = 37.5046400
    lat = 55.7016200
    MAP_FOCUS = (lon, lat)
    MAP_FOCUS1 = (lon, lat)
    MAP_FOCUS2 = (lon, lat)

EVENTS = {
	'SONG_END': pygame.USEREVENT + 1,
    'RAD_ANIM': pygame.USEREVENT + 2
}

ACTIONS = {
	pygame.K_F1: "module_stats",
	pygame.K_F2: "module_items",
	pygame.K_F3: "module_data",
	pygame.K_1:	"knob_1",
	pygame.K_2: "knob_2",
	pygame.K_3: "knob_3",
	pygame.K_4: "knob_4",
	pygame.K_5: "knob_5",
	pygame.K_UP: "dial_up",
	pygame.K_DOWN: "dial_down"
}

# Using GPIO.BOARD as mode
GPIO_ACTIONS = {
	29: "module_stats",
	31: "module_items",
	33: "module_data",
	36: "knob_1",
	35: "knob_2",
	38: "knob_3",
	37: "knob_4",
	40: "knob_5",
#	11: "dial_up",
#	13: "dial_down",
#	15: "switchpin"
}

MAP_ICONS = {
#	"camp": 		pygame.image.load('images/map_icons/camp.png'),
	"factory": 		pygame.image.load('images/map_icons/factory.png'),
	"metro": 		pygame.image.load('images/map_icons/metro.png'),
	"misc": 		pygame.image.load('images/map_icons/ruin.png'),
	"monument": 	pygame.image.load('images/map_icons/monument.png'),
	"vault": 		pygame.image.load('images/map_icons/vault.png'),
	"settlement": 	pygame.image.load('images/map_icons/settlement.png'),
	"ruin": 		pygame.image.load('images/map_icons/ruin.png'),
	"cave": 		pygame.image.load('images/map_icons/cave.png'),
	"landmark": 	pygame.image.load('images/map_icons/landmark.png'),
	"city": 		pygame.image.load('images/map_icons/city.png'),
	"office": 		pygame.image.load('images/map_icons/office.png'),
	"sewer": 		pygame.image.load('images/map_icons/sewer.png'),
}

AMENITIES = {
	'pub': 				MAP_ICONS['vault'],
	'nightclub': 		MAP_ICONS['vault'],
	'bar': 				MAP_ICONS['vault'],
	'fast_food': 		MAP_ICONS['sewer'],
	'cafe': 			MAP_ICONS['sewer'],
	'drinking_water': 	MAP_ICONS['sewer'],
	'restaurant': 		MAP_ICONS['settlement'],
	'cinema': 			MAP_ICONS['office'],
	'pharmacy': 		MAP_ICONS['office'],
	'school': 			MAP_ICONS['office'],
	'bank': 			MAP_ICONS['monument'],
	'townhall': 		MAP_ICONS['monument'],
	'bicycle_parking': 	MAP_ICONS['vault'],
	'place_of_worship': MAP_ICONS['ruin'],
	'theatre': 			MAP_ICONS['cave'],
	'bus_station': 		MAP_ICONS['metro'],
	'parking': 			MAP_ICONS['misc'],
	'fountain': 		MAP_ICONS['office'],
	'marketplace': 		MAP_ICONS['city'],
	'atm': 				MAP_ICONS['sewer'],
}

pygame.font.init()
FONTS = {}
for x in range(8, 28):
	FONTS[x] = pygame.font.Font('MONOFONTO.TTF', x)
