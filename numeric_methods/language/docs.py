# settings.py
APPLY_LANGUAGE_DOCS = {
    "ENGLISH": """
    Applies a new language for every subscribed function which is almost all function in package.
    This function has O(n) complexity, that is why this operation could take some time
    Example:
        | from numeric_methods import settings
        |
        |
        | help(settings)  # English documentation
        | if settings.set_language("ru"):
        |     settings.apply_language()
        |
        | help(settings)  # Russian documentation if it has
    """,
    "RUSSIAN": """
    Применяет новый язык к каждой подписанной функции, коих большинство в пакете.
    Эта функция имеет сложность O(n), поэтому эта операция может занять некоторое время
    Пример:
        | from numeric_methods import settings
        |
        |
        | help(settings)  # Английская документация
        | if settings.set_language("ru"):
        |     settings.apply_language()
        |
        | help(settings)  # Русская документация, если есть
    """,
}

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

    :param name: Название поддерживаемого языка: ENGLISH или RUSSIAN (en или ru)
    :return: True если указанный язык применен к пакету, иначе False
    """
}
