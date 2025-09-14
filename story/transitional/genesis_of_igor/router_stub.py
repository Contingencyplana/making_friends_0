# Minimal router stub for Genesis of Igor.
# The real routing will be filled by Copilot; keep function names aligned with choices.yaml effects.

def route_genesis_of_igor(effect_id: str):
    """Return a short scene string (3–6 lines) for Genesis of Igor.

    Each scene matches the tone of scene_intro.md, includes a playful Igor line,
    and ends with a one-sentence seed hinting at future planning prowess.
    IDs align with choices.yaml.
    """

    handlers = {
        'igor_first_word': lambda: (
            "Lamp hums; straps sigh. Igor blinks.\n"
            "Doctor: 'Do you hear me?'\n"
            "Igor: 'Y-yes, Master? Yes? Yes!' (tries each 'yes' like a gear)\n"
            "Grumble: 'He’s got echo in him.'\n"
            "Seed: A voice practiced today will carry plans tomorrow."),

        'mimic_moth': lambda: (
            "A pale moth writes circles on the lamp; Igor copies the air with his finger.\n"
            "Doctor: 'Diagramming, are we?'\n"
            "Igor: 'Round and round until it remembers the middle!'\n"
            "Grumble snorts, but his eyes follow the loop.\n"
            "Seed: Patterns rehearsed become plans remembered."),

        'spark_count_fix': lambda: (
            "Coils crackle; Grumble miscounts. 'Five— no, eight—'\n"
            "Igor: 'Seven-and-a-pause, Master! Like polite thunder.'\n"
            "Doctor smiles without looking. 'Polite will do.'\n"
            "The pause lands; the heart agrees.\n"
            "Seed: Timing learned now becomes scheduling later."),

        'tray_rhythm': lambda: (
            "Igor bows too low, taps a metal tray; it answers with a rhythm.\n"
            "Grumble: 'Band practice at a birth?'\n"
            "Igor (grinning): 'The lab likes a little drum.'\n"
            "Doctor’s foot keeps time, almost not on purpose.\n"
            "Seed: Rhythms today grow into coordinated plans."),

        'name_seed': lambda: (
            "'What am I called?' Igor asks the lamp, then the room.\n"
            "Doctor: 'Names are promises.'\n"
            "Igor: 'Then I promise to be useful.'\n"
            "Grumble: 'Useful is a fine surname.'\n"
            "Seed: A chosen name becomes a roadmap."),

        'first_joke': lambda: (
            "A joke spills out of him before he knows why.\n"
            "Doctor: 'Explain the punchline.'\n"
            "Igor: 'If I explain it, it might get a job.'\n"
            "Grumble chuckles despite himself.\n"
            "Seed: Laughter loosens the mind for invention."),

        'prophecy_tap': lambda: (
            "The tapping heart echoes a pattern only Igor seems to hear.\n"
            "Igor: 'It’s saying save-one, save-two, then leap.'\n"
            "Doctor listens with his eyes.\n"
            "Grumble: 'Leaps need bridges.'\n"
            "Seed: A heard cadence turns into a plan to cross."),

        'deputy_of_lamps': lambda: (
            "The moth lands on his knuckle; Igor bows solemnly.\n"
            "Igor: 'Deputy of Lamps, report!'\n"
            "Doctor: 'You’re appointing staff already?'\n"
            "Grumble: 'Hope the moth can carry a clipboard.'\n"
            "Seed: Delegation today grows into orchestration."),

        'knot_skill': lambda: (
            "A leather strap’s knot gives up under Igor’s careful fingers.\n"
            "Doctor: 'Who taught you that?'\n"
            "Igor: 'The knot wanted to be a line.'\n"
            "Grumble: 'Lines turn into lists. Careful.'\n"
            "Seed: Unknotting now becomes problem-solving later."),

        'bell_plan': lambda: (
            "The old bell remembers storms when struck with a fingertip.\n"
            "Igor: 'It says store wood high and keep tea near.'\n"
            "Doctor hides a smile.\n"
            "Grumble: 'I’ll put the kettle on the shelf, then.'\n"
            "Seed: Listening becomes preparedness."),

        'green_possible': lambda: (
            "Through a cracked green lens, the lab turns sea-bright.\n"
            "Igor: 'Everything is possible if it’s green first.'\n"
            "Doctor: 'Then give me your possible list.'\n"
            "Grumble waves the lens like a flag.\n"
            "Seed: A lens today becomes a filter for plans."),

        'harbor_call': lambda: (
            "He sways as if aboard a ship he’s never sailed.\n"
            "Igor: 'Port is left; starboard is the other left.'\n"
            "Doctor: 'And the harbor?'\n"
            "Igor: 'Where plans anchor until weather clears.'\n"
            "Seed: Bearings now become navigation later."),

        'weight_of_plans': lambda: (
            "The Doctor’s notebook grows heavier in Igor’s presence.\n"
            "Igor (playful strain): 'Ideas are putting on boots.'\n"
            "Doctor: 'Then we walk.'\n"
            "Grumble slides the notebook closer to the boy.\n"
            "Seed: A weight today becomes a responsibility chart."),

        'timing_gag': lambda: (
            "He reaches for the copper switch… then pauses, grinning.\n"
            "Doctor: 'Well?'\n"
            "Igor: 'Comedy is just engineering with manners.'\n"
            "Grumble: 'Flip it before the manners curdle.'\n"
            "Seed: Good timing becomes good sequencing."),

        'winter_improve': lambda: (
            "Dust tastes like last winter; Igor sneezes.\n"
            "Igor: 'Next winter should be warmer and have cookies.'\n"
            "Doctor: 'Requirements captured.'\n"
            "Grumble: 'Add socks.'\n"
            "Seed: Complaints now become design criteria later."),

        'yes_master': lambda: (
            "He chirps, 'Yes, Master!' — and means it, for now.\n"
            "Doctor: 'Meaning is the hinge.'\n"
            "Igor: 'I’ll oil the hinge daily.'\n"
            "Grumble: 'And check the door swings both ways.'\n"
            "Seed: Obedience today grows into trustworthy autonomy."),
    }
    return handlers.get(effect_id, lambda: 'SCENE: (missing)')()
