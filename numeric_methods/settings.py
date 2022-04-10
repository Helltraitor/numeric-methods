from numeric_methods.language.docs import GET_LANGUAGE_DOCS, SET_LANGUAGE_DOCS
from numeric_methods.language.properties import LANGUAGE, TRANSLATE


@TRANSLATE.documentation(GET_LANGUAGE_DOCS)
def get_language() -> str:
    return LANGUAGE.current


@TRANSLATE.documentation(SET_LANGUAGE_DOCS)
def set_language(name: str) -> bool:
    language = LANGUAGE.get_acceptable(name)
    if language is not None:
        LANGUAGE.current = language
        TRANSLATE.update()
        return True
    return False
