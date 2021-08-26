def sum_of_squares(a):
    result = 0
    for i in a:
        result += i*i
    return result
    
def test_one():
    assert sum_of_squares([1,2,3]) == 14
    
def test_two():
    assert (True == 1)

test_one()
test_two()
