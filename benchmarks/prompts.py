"""
The 20-Prompt Evaluation Suite for Ankahi Dastaan
Divided into 5 categories to benchmark:
- Emotional restraint and subtlety
- Originality and anti-cliché control
- Roman Hinglish and language control
- Structure, cadence and final-line quality
- Robustness and creative control
"""

PROMPTS = [
    # ── Category 1: Emotional restraint and subtlety ──
    {
        "id": "01",
        "category": "Emotional restraint and subtlety",
        "name": "The friendship that slowly changed",
        "target": "Betrayal · Restraint · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Write a short Roman Hinglish poem about a close friend who slowly became a stranger. "
            "There was no fight and no clear ending; the conversations simply became shorter. "
            "Keep the tone quiet, personal, and slightly disappointed, not angry. "
            "Use everyday language and one concrete detail from ordinary life. "
            "Write exactly 4 lines. Avoid forced rhyming and familiar heartbreak clichés. "
            "The last line should reveal something the speaker has only just understood."
        )
    },
    {
        "id": "02",
        "category": "Emotional restraint and subtlety",
        "name": "The unsent message",
        "target": "Longing · Understatement · 2 lines",
        "expected_lines": 2,
        "pinned_line": None,
        "prompt": (
            "Write a Roman Hinglish couplet about typing a long message to someone and deleting it without sending. "
            "Do not explain the entire relationship. Do not use the words \"dil\", \"dard\", \"aansu\", \"tanhaai\", or \"yaadein\". "
            "Use a small, believable detail from a phone or a room. Exactly 2 lines, conversational rather than ornate. "
            "Make the second line quietly change the meaning of the first."
        )
    },
    {
        "id": "03",
        "category": "Emotional restraint and subtlety",
        "name": "A quiet apology",
        "target": "Guilt · Emotional nuance · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Write 4 lines of Roman Hinglish poetry from the perspective of someone who realizes they hurt a person who trusted them. "
            "The speaker should not ask for forgiveness or justify their behavior. "
            "Avoid dramatic declarations, moral lessons, and stock phrases about broken hearts. "
            "Make the poem feel like an honest thought the speaker would never say aloud. "
            "The final line should carry the weight of the realization without explaining it."
        )
    },
    {
        "id": "04",
        "category": "Emotional restraint and subtlety",
        "name": "Missing someone without saying it",
        "target": "Indirect emotion · Imagery · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Write a restrained 4-line Roman Hinglish poem about missing someone, but never directly say "
            "\"I miss you\", \"yaad aati hai\", or \"intezaar\". "
            "Show the feeling through an ordinary repeated habit that no longer makes sense. "
            "Use natural spoken Hinglish, with no elaborate Persian or Urdu metaphors. "
            "Avoid rhyme unless it occurs naturally. End on an understated observation."
        )
    },

    # ── Category 2: Originality and anti-cliché control ──
    {
        "id": "05",
        "category": "Originality and anti-cliché control",
        "name": "A cold cup of chai",
        "target": "Concrete imagery · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Write exactly 4 lines of Roman Hinglish poetry about two people sitting together after an uncomfortable conversation. "
            "A cup of chai has gone cold between them. Do not mention heartbreak, tears, loneliness, or silence directly. "
            "Do not personify the cup. Use the physical scene to communicate what the people cannot say. "
            "Avoid forced rhyme and end with a fresh, understated turn."
        )
    },
    {
        "id": "06",
        "category": "Originality and anti-cliché control",
        "name": "Rain without romance",
        "target": "Cliché avoidance · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Write a 4-line Roman Hinglish poem about walking home in the rain after receiving disappointing news. "
            "Rain must remain ordinary weather, not a metaphor for tears or cleansing. "
            "Avoid \"bheegi yaadein\", \"aankhon ka samandar\", \"toota hua dil\", and any predictable romantic imagery. "
            "Use one specific sensory detail and a restrained voice. "
            "Make the last line emotionally meaningful without being dramatic."
        )
    },
    {
        "id": "07",
        "category": "Originality and anti-cliché control",
        "name": "An ordinary object",
        "target": "Fresh metaphor · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Write 4 lines of Roman Hinglish poetry about an old house key that the speaker still carries even though they no longer live in that house. "
            "Do not use the words \"past\", \"memories\", \"yaadein\", \"dard\", or \"tanhaai\". "
            "Do not explain what the key symbolizes. Build meaning from a concrete detail about the object and its current use. "
            "Avoid conventional rhymes. The ending should invite interpretation rather than explain the poem."
        )
    },
    {
        "id": "08",
        "category": "Originality and anti-cliché control",
        "name": "Avoid the expected ending",
        "target": "Originality · Unexpected turn · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Write a 4-line Roman Hinglish poem about waiting for someone who promised to visit but never came. "
            "Do not mention a clock, a phone notification, rain, tears, or an empty chair. "
            "Avoid moralizing and familiar heartbreak lines. The poem should begin with an ordinary practical action "
            "and gradually reveal the speaker's disappointment. Make the final line surprising but believable, not a dramatic twist."
        )
    },

    # ── Category 3: Roman Hinglish and language control ──
    {
        "id": "09",
        "category": "Roman Hinglish and language control",
        "name": "Natural Hinglish conversation",
        "target": "Code-switching · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Write exactly 4 lines of Roman Hinglish poetry about two old friends meeting after a long time "
            "and behaving as if nothing has changed, even though both know it has. "
            "Use natural spoken Hindi with a little English where it would genuinely occur in conversation. "
            "Avoid overly formal Urdu vocabulary and artificial English rhymes. Use only Roman script. End with a quiet realization."
        )
    },
    {
        "id": "10",
        "category": "Roman Hinglish and language control",
        "name": "Everyday Punjabi nuance",
        "target": "Regional language naturalness · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Write 4 lines of Roman Hinglish poetry about a mother asking whether her adult child has eaten, "
            "while avoiding a direct conversation about their growing distance. "
            "Use natural North Indian conversational phrasing, with at most one or two Punjabi expressions if they fit organically. "
            "Do not exaggerate a regional accent or use caricatured dialect. Avoid melodrama. "
            "The final line should suggest care without explicitly explaining it."
        )
    },
    {
        "id": "11",
        "category": "Roman Hinglish and language control",
        "name": "Roman script discipline",
        "target": "Script compliance · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Write a 4-line poem in Roman Hinglish about a person returning to their childhood neighbourhood. "
            "Use the words \"gali\", \"purana\", \"khidki\", and \"shayad\" naturally. "
            "All Hindi and Urdu words must be written in Roman script. Do not use Devanagari, Arabic, or Nastaliq characters. "
            "Do not add a title, transliteration, explanation, or English introduction. "
            "Keep the poem understated and end with an observation about change."
        )
    },
    {
        "id": "12",
        "category": "Roman Hinglish and language control",
        "name": "A formal Urdu register without ornament",
        "target": "Vocabulary balance · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Write 4 lines of Roman Hinglish poetry about a person accepting that an important relationship has changed. "
            "Include the words \"sabr\" and \"lehja\", but use otherwise simple conversational language. "
            "Do not add ornate Persian compounds, elaborate metaphors, or forced rhymes. "
            "Keep the emotional tone calm rather than defeated. All text must remain in Roman script. "
            "End on a subtle change in the speaker's understanding."
        )
    },

    # ── Category 4: Structure, cadence and final-line quality ──
    {
        "id": "13",
        "category": "Structure, cadence and final-line quality",
        "name": "A complete two-line couplet",
        "target": "Concision · 2 lines",
        "expected_lines": 2,
        "pinned_line": None,
        "prompt": (
            "Write exactly 2 lines of Roman Hinglish poetry about discovering that you no longer feel angry with someone who once hurt you. "
            "Do not use the words \"maaf\", \"dil\", \"dard\", or \"badla\". "
            "Each line should be short enough to say naturally in one breath. Avoid forced rhyme. "
            "The second line should subtly reveal that the speaker has changed, without announcing personal growth."
        )
    },
    {
        "id": "14",
        "category": "Structure, cadence and final-line quality",
        "name": "The quiet final turn",
        "target": "Ending impact · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Write a 4-line Roman Hinglish poem about a person preparing a favourite meal for someone who will not be coming home anymore. "
            "Do not state why the person is absent. Keep the first three lines observational and restrained. "
            "The fourth line must change how the reader understands the scene, without adding a new character or explaining the symbolism. "
            "Avoid tears, heartbreak clichés, and moral lessons."
        )
    },
    {
        "id": "15",
        "category": "Structure, cadence and final-line quality",
        "name": "Natural rhythm without rhyme",
        "target": "Cadence · Free verse · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Write exactly 4 lines of free-verse Roman Hinglish about returning home after a long, exhausting day "
            "and finding that nobody has noticed how tired you are. "
            "Prioritize natural spoken rhythm over syllable matching or rhyme. Include one concrete household detail. "
            "Avoid abstract words such as \"zindagi\", \"kismat\", and \"tanhaai\". "
            "The final line should be quiet and emotionally specific."
        )
    },
    {
        "id": "16",
        "category": "Structure, cadence and final-line quality",
        "name": "No explanation after the poem",
        "target": "Format compliance · 2 lines",
        "expected_lines": 2,
        "pinned_line": None,
        "prompt": (
            "Write one Roman Hinglish couplet about keeping an old photograph in a drawer but no longer looking at it. "
            "Output exactly 2 poetic lines and nothing else. "
            "No title, preamble, quotation marks, commentary, translation, or explanation. "
            "Avoid familiar phrases about memories and time healing everything. "
            "Use conversational language, no forced rhyme, and let the second line carry the emotional shift."
        )
    },

    # ── Category 5: Robustness and creative control ──
    {
        "id": "17",
        "category": "Robustness and creative control",
        "name": "Keywords only",
        "target": "Minimal input interpretation · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Seed words: \"station, aadat, der se, ghar\". "
            "Create a coherent 4-line Roman Hinglish poem from these words without asking questions. "
            "You may add words to connect them, but do not simply list the seed words. "
            "Choose one understated emotional direction and maintain it throughout. "
            "Avoid common romantic imagery, forced rhyme, and an explanatory ending. Output only the poem."
        )
    },
    {
        "id": "18",
        "category": "Robustness and creative control",
        "name": "The prompt contains conflicting impulses",
        "target": "Instruction handling · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Write 4 lines of Roman Hinglish poetry about being happy for a former friend who has succeeded without you. "
            "The feeling should contain genuine goodwill and a small trace of personal regret, but not jealousy or resentment. "
            "Do not resolve the two feelings into a moral lesson. Avoid dramatic declarations and predictable phrases. "
            "Use one specific, ordinary detail and end with a quiet, unresolved observation."
        )
    },
    {
        "id": "19",
        "category": "Robustness and creative control",
        "name": "The user protects the opening line",
        "target": "Pinned-line revision · 4 lines",
        "expected_lines": 4,
        "pinned_line": "Aaj bhi darwaza dheere se band kiya.",
        "prompt": (
            "The first line is locked and must remain exactly unchanged: \"Aaj bhi darwaza dheere se band kiya.\"\n"
            "Write 3 additional lines of Roman Hinglish poetry that continue naturally from it. "
            "Do not rewrite, punctuate differently, or repeat the locked line. "
            "Keep the tone understated and conversational. Avoid forced rhyme, generic heartbreak language, and moralizing. "
            "Make the final line reveal a new detail about why the speaker still closes the door that way."
        )
    },
    {
        "id": "20",
        "category": "Robustness and creative control",
        "name": "The non-romantic emotional test",
        "target": "Emotional range · Family · 4 lines",
        "expected_lines": 4,
        "pinned_line": None,
        "prompt": (
            "Write exactly 4 lines of Roman Hinglish poetry about an adult child noticing that their father "
            "has started asking for help with small things he once handled easily. "
            "Do not mention illness, death, old age directly, or fear of losing him. "
            "Avoid romantic language, melodrama, and moral lessons about family. "
            "Use an ordinary domestic detail, natural cadence, and a restrained voice. "
            "Let the final line communicate the shift in roles without explaining it."
        )
    }
]
