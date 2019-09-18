import pytest
from principal import soma
from principal import sub

def test_Somar():
    assert soma(2,4) == 6

def test_sub():
    assert sub(9,5) == 4