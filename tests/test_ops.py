from src.math_ops import add, sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0

def test_sub():
    assert sub(5,3)==2
    assert sub(3,6)==-3
    assert sub(9,9)==0
