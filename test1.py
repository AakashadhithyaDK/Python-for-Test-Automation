import math
import sys
import src.calculate
import pytest


def test_num():
    num=5
    assert num==5 , 'not equal'


#@pytest.mark.skipif(sys.version_info < (3, 12), reason='deferred')
def test_sqrt():
    num=25
    print('initialization')
    ans=math.sqrt(num)
    print('sqrt calculated')
    assert ans== 5,'squareroot is wrong'
    print('sqrt wrong assertion error')


def test_voteeligibility():
    age=19
    assert age>=18,'not eligible to vote'



@pytest.mark.parametrize('num1,num2,num3,add,diff,pro,quo',
                        [
                            (10,20,30,60,-10,200,0),
                            (-10,-20,-30,-60,-10,200,0),
                            (0,0,0,0,0,0,0)
                        ])

def test_calculate(num1,num2,num3,add,diff,pro,quo):
    sum,difference,product,quotient=src.calculate.calculate(num1,num2,num3)
    assert sum==add,'Sum is wrong'
    assert difference== diff, 'diff is wrong'
    assert product == pro,'product wrong'
    assert quotient== quo ,'quotient wrong'