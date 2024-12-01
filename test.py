from main import check
import unittest
from main import add, subtract, multiply, divide

class TestMath(unittest.TestCase):
    def test_add(self):  # функция проверки первой функции add файла main
        self.assertEqual(add(2, 5), 7)  # функция, проверяющая сумму 2 и 5 равную 7
        self.assertNotEqual(add(3, 7), 9)  # функция, проверяющая сумму 2 и 5 равную 9 - неправильно

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)  # функция, проверяющая разность
        self.assertNotEqual(subtract(4, 2), 1)

    def test_multiply(self):
        self.assertNotEqual(multiply(2, 5), 12)  # функция, проверяющая умножение
        self.assertEqual(multiply(3, 6), 18)

    def test_divide(self):
        self.assertNotEqual(divide(4, 2), 3)  # функция, проверяющая деление
        self.assertEqual(divide(20, 5), 4)

    def test_divide_by_zero(self): # функция, проверяющая деление на 0
        self.assertRaises(ValueError, divide, 6, 0)

class TestCheck(unittest.TestCase):
    def test_check(self):  # функция, проверяющая остаток от деления
        self.assertTrue(check(2))  # проверка на четность
        self.assertTrue(check(6))
        self.assertTrue(check(220))

        self.assertTrue(not check(1))  # проверка на не четность с True
        self.assertTrue(not check(3))
        self.assertTrue(not check(57))

if __name__ == '__main__':
	unittest.main()
