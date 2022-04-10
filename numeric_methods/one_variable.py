from numeric_methods.language.properties import TRANSLATE

docs = {"ENGLISH": "TEST", "RUSSIAN": "ТЕСТ"}


@TRANSLATE.documentation(docs)
def fun():
    pass
