def test_function(i,j):
    if i == 0:
        return j
    else:
        return test_function(i-1,j+1)
print(test_function(6,7))
