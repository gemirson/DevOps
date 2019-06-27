import pytest
from DevOps import Sum
from DevOps import Sub
from DevOps import Mul
from DevOps import Div

def test_somar():
    assert Sum(2,4)==6
def test_sub():
    assert Sub(2,4)==-2
def test_mul():
    assert Mul(2,4)==8   
def test_div():
    assert Div(2,4)==0.5     