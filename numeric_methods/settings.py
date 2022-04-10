from numeric_methods.language.docs import APPLY_LANGUAGE_DOCS, GET_LANGUAGE_DOCS, SET_LANGUAGE_DOCS

LANGUAGE = "ENGLISH"

LANGUAGE_VARIANTS = ("en", "ENGLISH"), ("ru", "RUSSIAN")

SUPPORTED_LANGUAGES = "ENGLISH", "RUSSIAN"

DOCUMENTATION_SUBSCRIBERS = []


def apply_documentation(function):
    function.__doc__ = function.__all_docs__.get(
        LANGUAGE,
        f"No documentation found for {LANGUAGE} language"
    )
    return function


def set_documentation(docs: dict[str, str]):
    def decorator(function):
        function.__all_docs__ = docs
        return function

    return decorator


def subscribe_documentation(function):
    DOCUMENTATION_SUBSCRIBERS.append(function)
    return function


@apply_documentation
@set_documentation(APPLY_LANGUAGE_DOCS)
@subscribe_documentation
def apply_language():
    global DOCUMENTATION_SUBSCRIBERS
    global LANGUAGE
    for subscriber in DOCUMENTATION_SUBSCRIBERS:
        apply_documentation(subscriber)


@apply_documentation
@set_documentation(GET_LANGUAGE_DOCS)
@subscribe_documentation
def get_language() -> str:
    global LANGUAGE
    return LANGUAGE


@apply_documentation
@set_documentation(SET_LANGUAGE_DOCS)
@subscribe_documentation
def set_language(name: str) -> bool:
    global LANGUAGE
    for variant in LANGUAGE_VARIANTS:
        if name in variant:
            LANGUAGE = variant[-1]
            return True
    return False
