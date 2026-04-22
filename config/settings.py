import os

# Gesture Settings
NUM_POINTS = 64
CONFIDENCE_THRESHOLD = 0.50
DEBOUNCE_INTERVAL = 0.3
TRIGGER_KEY = 'ctrl_l' # Use specific key name for pynput
SEGMENTATION_PAUSE_MS = 250 # Pause in movement to trigger mid-hold

# Mouse Settings
MOUSE_SMOOTHNESS = 10
MOUSE_SPEED = 1

# Automation Settings
MODIFIER_PERSISTENCE_MS = 500 # Keep modifiers pressed for X ms

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, 'data', 'Collection')
MODEL_PATH = os.path.join(BASE_DIR, 'data', 'model.pkl')
MODEL_INFO_PATH = os.path.join(BASE_DIR, 'data', 'model_info.npy')
ACTIONS_CONFIG_PATH = os.path.join(BASE_DIR, 'config', 'actions.json')

# Feature Extraction
MIN_POINTS_THRESHOLD = 10

# Path Suggestion Overlay Settings
PATH_SUGGEST_FONT_FAMILY = "Consolas"
PATH_SUGGEST_FONT_SIZE = 12
PATH_SUGGEST_FONT_WEIGHT = "bold"

PATH_SUGGEST_TEXT_COLOR = "cyan"
PATH_SUGGEST_BG_COLOR = "black"

PATH_SUGGEST_PAD_X = 15
PATH_SUGGEST_PAD_Y = 8

PATH_SUGGEST_ALPHA = 0.85
PATH_SUGGEST_OFFSET_X = 20
PATH_SUGGEST_OFFSET_Y = 80


# Wand Trail Settings
WAND_TRAIL_COLOR = "#00FFFF"
WAND_TRAIL_WIDTH = 8
WAND_TRAIL_MAX_POINTS = 80
WAND_FADE_SPEED = 3

WAND_TIP_INNER_COLOR = "#006DFC"
WAND_TIP_OUTER_COLOR = "#00FFF2"

WAND_TIP_BASE_RADIUS = 5
WAND_TIP_PULSE_AMPLITUDE = 3
WAND_TIP_OUTER_GLOW = 10

WAND_OVERLAY_FPS = 16

# Wand visual settings
WAND_IMAGE_SIZE = (48, 48)

# Where the trail should start relative to the wand image
# x = horizontal offset from image center
# y = vertical offset from image center
WAND_TRAIL_OFFSET_X = -10
WAND_TRAIL_OFFSET_Y = -10

# If False, wand stays fixed orientation
WAND_ROTATE_WITH_MOVEMENT = False