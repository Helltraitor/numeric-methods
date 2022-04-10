from numeric_methods import settings


docs = { "ENGLISH" : "TEST", "RUSSIAN": "ТЕСТ"}


@settings.apply_documentation
@settings.set_documentation(docs)
@settings.subscribe_documentation
def fun():
    pass


# Initial applying
settings.apply_language()
