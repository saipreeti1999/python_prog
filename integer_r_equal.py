def test_numbers5(x,y):
    if x==y or abs(x-y)==5 or (x+y)==5:
        return True
    else:
        return False
print(test_numbers5(7,2))
print(test_numbers5(3,2))
print(test_numbers5(2,2))
