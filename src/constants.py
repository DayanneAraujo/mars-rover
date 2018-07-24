# Actions
PLATEAU = 'plateau'
LANDIND = 'landing'
INSTRUCTIONS = 'instructions'

# SPIN
RIGHT = 'r'
LEFT = 'l'

# MOVE
MOVE = 'm'

# Cardinal Compass
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

HEADINGS = 'nswe'
MOVEMENTS = {NORTH: (0, 1),
             SOUTH: (0, -1),
             EAST: (1, 0),
             WEST: (-1, 0)}

CARDINAL_FLOW = [NORTH, EAST, SOUTH, WEST]
CARDINAL_FLOW_LEN = len(CARDINAL_FLOW)
