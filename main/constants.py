# C:\Users\Admin\making_friends_0\main\constants.py
TITLE = "MAKING FRIENDS — The Lonely Doctor"

# Storm-day timing (minutes)
MEAL_MINS = 5 * 60
EXERCISE_MINS = 8 * 60
SLEEP_MINS = 16 * 60
DAY_MINS = SLEEP_MINS

# 16 ritual levers (16 = meditation/meta)
MAIN_CHOICES = [
    "The rain stutters on the lightning plate.",
    "A jar of blinking eyes opens slightly.",
    "A coil hums behind the sealed door.",
    "A pale moth writes circles on the lamp.",
    "The slab is cold; the straps are warm.",
    "You count the cracks in the tiles.",
    "Something in the attic learns a name.",
    "A fuse prays to be spared.",
    "A second heart taps once, then waits.",
    "An old bell remembers storms.",
    "A broken lens dreams in green.",
    "The sea rehearses thunder.",
    "Your notebook grows heavier.",
    "A copper hand reaches for the switch.",
    "Dust tastes like last winter.",
    "The Lonely Doctor meditates.",  # meta lever (Save/Quit/Return)
]

# Transitional Stage routing hints (keep MAIN_CHOICES text unchanged)
TRANSITIONAL_SLOTS = {
    "A second heart taps once, then waits.": "T1_GENESIS_OF_IGOR",
    "The sea rehearses thunder.": "T2_TEAM_OF_FOUR_AND_HARBOR",
    "A broken lens dreams in green.": "T3_FURNITURE_AND_FIRST_PLANNERS",
    "Your notebook grows heavier.": "T4_SCALING_CYCLES",
}
META_SLOT = "The Lonely Doctor meditates."
