import pytest
def test_uppercase():
    word = 'hi'
    assert str.upper(word) == 'HI', 'No uppercase'


def test_lowercase():
    word = 'hi'
    assert str.lower(word) == 'hi', 'No lowercase'

def test_split():
    str1='Hello Aakashadhithya D K'
    #str2=str1
    ls=str.split(str1)
    with pytest.raises(IndexError):
        print(ls[6])

    '''assert len(ls) == 4, 'spliting wrong'
    assert str1.split(), ['Hello','Aakashadhithya','D','K']
    assert ls== ['Hello','Aakashadhithya','D','K']
    assert str1 is str2'''

