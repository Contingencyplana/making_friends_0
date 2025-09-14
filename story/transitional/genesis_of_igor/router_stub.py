# Minimal router stub for Genesis of Igor.
# The real routing will be filled by Copilot; keep function names aligned with choices.yaml effects.

def route_genesis_of_igor(effect_id: str):
    handlers = {
        'igor_first_word': lambda: 'SCENE: First word',
        'mimic_moth': lambda: 'SCENE: Mimic moth',
        'spark_count_fix': lambda: 'SCENE: Spark count fix',
        'tray_rhythm': lambda: 'SCENE: Tray rhythm',
        'name_seed': lambda: 'SCENE: Name seed',
        'first_joke': lambda: 'SCENE: First joke',
        'prophecy_tap': lambda: 'SCENE: Prophecy tap',
        'deputy_of_lamps': lambda: 'SCENE: Deputy of lamps',
        'knot_skill': lambda: 'SCENE: Knot skill',
        'bell_plan': lambda: 'SCENE: Bell plan',
        'green_possible': lambda: 'SCENE: Green possible',
        'harbor_call': lambda: 'SCENE: Harbor call (foreshadow Harbor of Hulks)',
        'weight_of_plans': lambda: 'SCENE: Weight of plans',
        'timing_gag': lambda: 'SCENE: Timing gag',
        'winter_improve': lambda: 'SCENE: Winter improve',
        'yes_master': lambda: 'SCENE: Yes, Master',
    }
    return handlers.get(effect_id, lambda: 'SCENE: (missing)')()
