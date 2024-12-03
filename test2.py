import pytest
from main2 import count_vowels


def test_count():
    assert count_vowels('аеоiouy') == 7


def test_count():
    assert count_vowels('вртмЗБВgfdQRT') == 0


def test_count():
    assert count_vowels('аеоАЕИОeiouyIOUY') == 16
