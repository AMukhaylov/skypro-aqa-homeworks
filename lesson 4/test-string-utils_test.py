import pytest
from string_utils import StringUtils 

string_utils = StringUtils()

@pytest.mark.parametrize('string, result', [('skypro', 'Skypro'), ('Skypro', 'Skypro'), ('Skypro23', 'Skypro23')])   
def test_capitilize(string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result

@pytest.mark.parametrize('string, result', [(' skypro', 'skypro'), (' Skypro', 'Skypro'), (' Skypro23', 'Skypro23'), 
(' skypro skypro', 'skypro skypro'), ('skypro', 'skypro')])  
def test_trim(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result

@pytest.mark.parametrize('string, delimeter, result', [('s,k,y,p,r,o', ',',["s", "k", "y", "p", "r", "o"]), 
("1:2:3", ':', ["1", "2", "3"]), ('', ', ', [])])
def test_list_delimeter(string, delimeter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(string, delimeter)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [('skypro', 's', True), ('skypro', 'z', False)])
def test_contain_is(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [('skypro', 's', 'kypro'), ('skypro', '', 'skypro')])
def test_delete_symbol(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [('skypro', 's', True), ('skypro', 'o', False), (' skypro', ' ', True)])
def test_starts_with_true(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [('skypro', 'o', True), ('skypro', 's', False), ('skypro ', ' ', True), ('skypro', 'z', False)])
def test_end_with_true(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, result', [('skypro', False), ('', True), ('  ', True),])
def test_is_empty(string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == result
    
@pytest.mark.parametrize('string, joiner, result', [([1,2,3,4], ", ", "1, 2, 3, 4"), 
(["Sky", "Pro"], ", ", "Sky, Pro"), (["Sky", "Pro"], "-", "Sky-Pro")])
def test_list_to_string(string, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(string, joiner)
    assert res == result