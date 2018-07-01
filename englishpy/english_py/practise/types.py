

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
    TYPES = (
        (VERBS, VERBS),
        (DEFAULT, DEFAULT),
    )
