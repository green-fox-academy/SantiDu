from Santi_work import *
import unittest
from unittest.mock import patch


##### Apples
class TestApple(unittest.TestCase):
    def test_get_apple(self):
        myapple = Apple()
        self.assertEqual(myapple.get_apple(), "rasin")


##### Sum
class TestSum(unittest.TestCase):
    def setUp(self):
        self.s = Sum()

    def test_sum_emptyls(self):
        self.assertEqual(self.s.sum([]), 0)

    def test_sum_oneItem(self):
        self.assertEqual(self.s.sum([1]), 1)

    def test_sum_mulItems(self):
        self.assertEqual(self.s.sum([4,2,1]), 7)

    def test_sum_None(self):
        self.assertRaises(TypeError, self.s.sum(None))


##### Anagram
class Test_isAnagram(unittest.TestCase):
    def test_anagram_difflen(self):
        self.assertEqual(isAnagram("ab", "bca"), False)

    def test_anagram_equalenNot(self):
        self.assertEqual(isAnagram("abcc", "bcaa"), False)
    
    def test_anagram_isTrue(self):
        self.assertEqual(isAnagram("sssb", "bsss"), True)

    def test_anagram_emptyStr(self):
        self.assertEqual(isAnagram("", ""), True)

    def test_anagram_lenIsOne(self):
        self.assertEqual(isAnagram("a", "a"), True)


##### Count Letters
class Test_countLetters(unittest.TestCase):
    def test_empty_str(self):
        self.assertEqual(countLetters(""), {})

    def test_oneletter(self):
        self.assertEqual(countLetters("a"), {"a":1})

    def test_mulletters(self):
        self.assertEqual(countLetters("baa"), {"a":2, "b":1})


##### Fibonacci
class Test_Fibonacci(unittest.TestCase):
    def test_Fibonacci1(self):
        self.assertEqual(fibonacci(5), 5)

    def test_Fibonacci2(self):
        self.assertEqual(fibonacci(7), 13)

    def test_Fibonacci3(self):
        self.assertEqual(fibonacci(10), 55)


##### Extension
class TestExtend(unittest.TestCase):
    def test_add_2_and_3_is_5(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_2_and_4_is_6(self):
        self.assertEqual(add(2, 4), 6)

    def test_max_of_three_first(self):
        self.assertEqual(max_of_three(5, 4, 3), 5)

    def test_max_of_three_second(self):
        self.assertEqual(max_of_three(3, 6, 5), 6)

    def test_median_four(self):
        self.assertEqual(median([7, 1, 3, 5]), 4)

    def test_median_five(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)

    def test_is_vovel_ö(self):
        self.assertTrue(is_vovel('ö'))

    def test_is_vovel_ü(self):
        self.assertTrue(is_vovel('ü'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_lagopus(self):
        self.assertEqual(translate('lagopus'), 'lavagovopuvus')

    def test_translate_ava(self):
        self.assertEqual(translate('ava'), 'avavava')

    def test_translate_aa(self):
        self.assertEqual(translate('aa'), 'avaava')
        

##### Sharpie
class TestSharpie(unittest.TestCase):
    def setUp(self):
        self.sharpie = Sharpie("blue", 3)

    def test_sharpie_color(self):
        self.assertEqual(self.sharpie.color, "blue")

    def test_sharpie_width(self):
        self.assertEqual(self.sharpie.width, 3)
    
    def test_sharpie_use(self):
        self.sharpie.use()
        self.assertEqual(self.sharpie.ink_amount, 98)


##### Animal
class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.animal = Animal()

    def test_animal_init(self):
        self.assertEquals(self.animal.hunger, 50)
        self.assertEquals(self.animal.thirst, 50)

    def test_animal_eat(self):
        self.animal.eat()
        self.assertEquals(self.animal.hunger, 49)

    def test_animal_drink(self):
        self.animal.drink()
        self.assertEquals(self.animal.thirst, 49)

    def test_animal_play(self):
        self.animal.play()
        self.assertEquals(self.animal.thirst, 51)
        self.assertEquals(self.animal.hunger, 51)


##### Cows and Bulls
class TestCAB(unittest.TestCase):
    def setUp(self):
        random.seed(2)
        self.cab = CAB()
    
    def test_CAB_init(self):
        self.assertEqual(self.cab.num, '1926') 
        self.assertEqual(self.cab.count, 0)
        self.assertEqual(self.cab.ncow, 0)
        self.assertEqual(self.cab.nbull, 0)
        self.assertEqual(self.cab.status, "playing")

    def test_cab_guess(self):
        with patch('builtins.input', side_effect=['6920', '1926']):
            # first attempt
            self.assertEqual(self.cab.guess(), "2 cow, 1 bull")
            self.assertEqual(self.cab.count, 1)
            self.assertEqual(self.cab.status, "playing")
            # second attempt
            self.assertEqual(self.cab.guess(), "4 cow, 0 bull")
            self.assertEqual(self.cab.count, 2)
            self.assertEqual(self.cab.status, "finished")


if __name__ == "__main__":
    unittest.main()