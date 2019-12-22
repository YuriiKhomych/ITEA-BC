import sys
sys.path.append("E:/Python/ITEA/ITEA-BC/Andrii_Ravlyk/6_strings/hw")
# print(sys.path)

from hw6_1 import convert_list_to_len
from hw6_2 import find_longest_word
from hw6_3 import filter_long_words
from hw6_4 import split_string
from hw6_5 import check_mob_num
from hw6_6 import get_list_domain

def test_convert_list_to_len():
    assert convert_list_to_len(['a','bb','ccc']) == [1, 2, 3], 'Should be right'

def test_find_longest_word():
    assert find_longest_word(['a', 'bb', 'ccc']) == 3, 'Should be right'
    assert find_longest_word(['a', 'bfghgfb', 'ccc', '7777777777']) == 10, 'Should be right'

def test_filter_long_words():
    assert filter_long_words(['aa','bbbbbb','ggg', 'hfghf'], 3) == ['bbbbbb', 'hfghf'], 'Should be right'

def test_split_string():
    assert split_string('asdf fjdk;afed,fjek,asdf,foo') == ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo'], 'Should be right'

def test_check_mob_num():
    assert check_mob_num(["+380971236789", "+380809123232", "99999x9999"]) == {"+380971236789":"valid", "+380809123232":"valid", "99999x9999":"not_valid"}, 'Should be right'

def test_get_list_domain():
    assert get_list_domain(["aff@mail.ru", "gjgjg@i.ua", "hkhjhkh@apple.com"]) == ["mail.ru", "i.ua", "apple.com"], 'Should be right'

# Run test
test_convert_list_to_len()
test_find_longest_word()
test_filter_long_words()
test_split_string()
test_check_mob_num()
test_get_list_domain()