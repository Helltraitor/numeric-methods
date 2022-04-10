# settings.py
GET_LANGUAGE_DOCS = {
    "ENGLISH": """
    Returns the current language of package
    Example:
        | from numeric_methods import settings
        |
        |
        | print(settings.get_language())  # ENGLISH

    :return: The string of full language name
    """,
    "RUSSIAN": """
    Возвращает название текущего языка пакета
    Пример:
        | from numeric_methods import settings
        |
        |
        | print(settings.get_language())  # ENGLISH

    :return: Строка полного названия языка
    """
}

SET_LANGUAGE_DOCS = {
    "ENGLISH": """
    Sets up language for whole package. That can be very useful for users who don't know english (default language)
    Example:
        | from numeric_methods import settings
        |
        |
        | settings.set_language("ru")
        | print(settings.get_language())  # RUSSIAN

    :param name: Name of supporting language: ENGLISH or RUSSIAN (en or ru)
    :return: True if the language was applied to package otherwise False
    """,
    "RUSSIAN": """
    Устанавливает язык для всего пакета. Довольно полезно для пользователей, не знакомых с английским
    (языком по умолчанию)

    Пример:
        | from numeric_methods import settings
        |
        |
        | settings.set_language("ru")
        | print(settings.get_language())  # RUSSIAN

    :param name: Название поддерживаемого языка: АНГЛИЙСКИЙ или РУССКИЙ (анг или рус)
    :return: True если указанный язык применен к пакету, иначе False
    """
}
