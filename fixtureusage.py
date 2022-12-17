import pytest
class Test_With_Fixtures():
    @pytest.fixture
    def inp_data(self,data):
        return data
    @pytest.mark.parametrize('inp_data', [(1, 3, 4),(2, 4, 6)] )
    def test_addnum(self,inp_data):
        assert inp_data[0]+inp_data[1] == inp_data[2]

    @pytest.mark.parametrize('inp_data', [(1, 3, 4),(2, 4, 6)] )
    def test_concatstr(self,inp_data):
        assert inp_data[0]!=inp_data[1]

    def test_t1(n1,n2,res):
        assert n1+n2 == res