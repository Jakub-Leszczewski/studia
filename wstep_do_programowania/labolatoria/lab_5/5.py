# Napisz funkcję zmieniającą miejscami dwa elementy listy wraz z obsługą wyjątków.
# Wymagania
# 1. Funkcja przyjmuje listę oraz indeksy.
# 2. Działa in-place (modyfikacja istniejącej listy)
# 3. Obsługuje ujemne indeksy
# 4. Wyrzuca:
# a. ValueError, gdy lista jest pusta
# b. TypeError, gdy argumenty mają niewłaściwe typy
# c. IndexError, gdy indeksy wychodzą poza zakres
# 5. (Dla chętnych - napisanie testów przy pomocy biblioteki pytest)

import pytest

def swap_elements(lst: list, index1: int, index2: int) -> None:
    if not lst:
        raise ValueError('Lista jest pusta!')

    if type(lst) is not list or type(index1) is not int or type(index2) is not int:
        raise TypeError('Nieprawidłowe argumenty!')

    if index1 >= len(lst) or index2 >= len(lst) or index1 < -len(lst) or index2 < -len(lst):
        raise IndexError('Indeksy wychodzą poza zakres!')

    lst[index1], lst[index2] = lst[index2], lst[index1]


def test_swap_elements():
    test_list = [1, 2, 3, 4, 5]
    swap_elements(test_list, 1, 3)
    assert test_list == [1, 4, 3, 2, 5]

def test_swap_edge_elements():
    test_list = [1, 2, 3, 4, 5]
    swap_elements(test_list, 0, 4)
    assert test_list == [5, 2, 3, 4, 1]

def test_swap_negative_elements():
    test_list = [1, 2, 3, 4, 5]
    swap_elements(test_list, -1, -3)
    assert test_list == [1, 2, 5, 4, 3]

def test_swap_empty_list():
    with pytest.raises(ValueError):
        swap_elements([], 0, 1)

def test_swap_wrong_types():
    with pytest.raises(TypeError):
        swap_elements(1, 0, 1)

    with pytest.raises(TypeError):
        swap_elements([1, 2, 3], 'one', 1)

    with pytest.raises(TypeError):
        swap_elements([1, 2, 3], 1, 'two')