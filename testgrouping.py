import math
import pytest
class Test_Numeric():
    def test_num(self):
        num = 5
        assert num == 5, 'not equal'

    # @pytest.mark.skipif(sys.version_info < (3, 12), reason='deferred')
    def test_sqrt(self):
        num = 25
        ans = math.sqrt(num)
        assert ans == 5, 'squareroot is wrong'

    def test_voteeligibility(self):
        age = 19
        assert age >= 18, 'not eligible to vote'

class Test_String():
    def test_uppercase(self):
        word = 'hi'
        assert str.upper(word) == 'HI', 'No uppercase'

    def test_lowercase(self):
        word = 'hi'
        assert str.lower(word) == 'hi', 'No lowercase'

    def test_split(self):
        str1 = 'Hello Aakashadhithya D K'
        # str2=str1
        ls = str.split(str1)
        with pytest.raises(IndexError):
            print(ls[6])
