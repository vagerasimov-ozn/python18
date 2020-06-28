import unittest

from get_formatted_name import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Здесь должно быть техническое
    задание, которое должно быть выполнено
    функция должна принимать англ имена и возвращать и х в корректном виде
    1. должны принимать с нижнего регистра и возвращать в верхнем
    2. должна приниматься с пробелами и возвращать в нормальном виде
    3. должна корректно возвращать с нижнего регистра с пробелами с отчеством
    """

    def test_first_last(self):
        """Работает ли корректно Uppercase?"""
        formatted_name = get_formatted_name('semen', 'semenov')
        self.assertEqual(formatted_name,"Semen Semenov")

    def test_chek_whitespace(self):
        """Работает ли корректно c пробелами?"""
        formatted_name = get_formatted_name(' semen ', ' semenov ')
        self.assertEqual(formatted_name,"Semen Semenov")
    def test_first_otch(self):
        """Кейс 3"""
        formatted_name = get_formatted_name(' semen ', 'Semenich', ' semenov ')
        self.assertEqual(formatted_name,"Semen Semenich Semenov")


unittest.main()