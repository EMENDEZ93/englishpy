

class VerbTypes():
    IRREGULAR = 'Irregular'
    REGULAR = 'Regular'
    PHRASAL_VERB = 'Phrasal_verb'
    TYPES = (
        (IRREGULAR, IRREGULAR),
        (REGULAR, REGULAR),
        (PHRASAL_VERB, PHRASAL_VERB)
    )


class TimesTypes():
    PAST = 'Past'
    PAST_PARTICIPLE = 'Past Participle'
    TYPES = (
        (PAST , PAST ),
        (PAST_PARTICIPLE , PAST_PARTICIPLE ),
    )


class TopicTypes():
    DEFAULT = '--------------------'
    VERBS = 'VERBS'
    LEARNED_WORD = 'LEARNED WORD'
    VOCABULARY = 'VOCABULARY'
    LEARNED_PRESENT = 'LEARNED PRESENT'
    LEARNED_PHRASAL = 'LEARNED PHRASAL'

    TYPES = (
        (VERBS, VERBS),
        (DEFAULT, DEFAULT),
        (LEARNED_WORD, LEARNED_WORD),
        (VOCABULARY, VOCABULARY),
        (LEARNED_PRESENT, LEARNED_PRESENT),
        (LEARNED_PHRASAL, LEARNED_PHRASAL),
    )
