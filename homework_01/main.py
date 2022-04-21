"""
Домашнее задание №1
Функции и структуры данных
"""

def power_numbers(*numbers, power = 2):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** power for number in numbers]


def is_prime(number):
    if number < 2:
        return False
    for test_divider in range(2, int(number ** 0.5)+1):
        if number % test_divider == 0:
            return False
    return True

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(numbers, odd_even_prime_string):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if odd_even_prime_string is PRIME:
        prime_list = list(filter(is_prime, numbers))
        return prime_list
    if odd_even_prime_string is ODD:
        return [number for number in numbers if (number % 2 == 1)]
    elif odd_even_prime_string is EVEN:
        return [number for number in numbers if (number % 2 == 0)]