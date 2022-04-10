import unittest

import numeric_methods.settings
from numeric_methods.settings import (
    set_documentation, subscribe_documentation, apply_language, get_language, set_language
)


class ApplyDocumentation(unittest.TestCase):
    # Tested through the other classes
    pass


class SubscribeDocumentation(unittest.TestCase):
    def tearDown(self):
        numeric_methods.settings.DOCUMENTATION_SUBSCRIBERS = []

    def test_subscribe(self):
        def empty():
            pass

        subscribe_documentation(empty)
        self.assertEqual(empty, numeric_methods.settings.DOCUMENTATION_SUBSCRIBERS[-1])


class SetDocumentation(unittest.TestCase):
    def setUp(self):
        def _empty():
            pass

        self._empty = _empty
        self._docs = {
            "ENGLISH": "TEST",
            "RUSSIAN": "ТЕСТ"
        }

        subscribe_documentation(self._empty)

    def tearDown(self):
        numeric_methods.settings.DOCUMENTATION_SUBSCRIBERS = []
        set_language("en")
        apply_language()

    def test_none_docs(self):
        self.assertFalse(hasattr(self._empty, "__all_docs__"))

    def test_setting(self):
        _empty = set_documentation(self._docs)(self._empty)
        self.assertIs(_empty, self._empty)
        self.assertTrue(hasattr(_empty, "__all_docs__"))
        self.assertIs(_empty.__all_docs__, self._docs)
        set_language("en")
        apply_language()
        self.assertEqual(_empty.__doc__, self._docs[get_language()])
        set_language("ru")
        apply_language()
        self.assertEqual(_empty.__doc__, self._docs[get_language()])


class ApplyLanguage(unittest.TestCase):
    # Tested through the other classes
    pass


class SetLanguage(unittest.TestCase):
    def tearDown(self):
        set_language("en")

    def test_default(self):
        self.assertEqual(get_language(), "ENGLISH")

    def test_getting(self):
        set_language("ru")
        self.assertEqual(get_language(), "RUSSIAN")


class GetLanguage(unittest.TestCase):
    def tearDown(self):
        set_language("en")

    def test_setting(self):
        set_language("ru")
        self.assertEqual(get_language(), "RUSSIAN")

    def test_raising(self):
        self.assertFalse(set_language("fr"))


if __name__ == '__main__':
    unittest.main()
