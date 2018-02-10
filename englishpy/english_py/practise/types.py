

class VerbTypes():
    IRREGULAR = 'Irregular'
    REGULAR = 'Regular'
    TYPES = (
        (IRREGULAR, IRREGULAR),
        (REGULAR, REGULAR),
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
