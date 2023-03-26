import pytest
    
def convert_scale(x):
    if type(x) == float or type(x) == int:
        return x
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000.0
    elif 'B' in x:
        if len(x) > 1:
            return float(x.replace('B', '')) * 1000000000
        return 1000000.0
    elif 'T' in x:
        return float(x.replace('T', '')) * 1000000000000
    else:
        return float(x)    
    
def test_convert_scale_string():
    #scale = convert_scale('test')
    with pytest.raises(ValueError, match='could not convert string to float'):
        convert_scale('banana')
    #print(scale)
    #assert scale == 0
    
def test_convert_scale_negative():
    scale = convert_scale('-5')
    print(scale)
    assert scale == -5.0

'''def test_convert_scale_M():
    scale = convert_scale('K')
    print(scale)
    assert scale == 0'''

def test_convert_scale_M():
    scale = convert_scale('5M')
    print(scale)
    assert scale == 5000000

'''def test_convert_scale_B():
    scale = convert_scale(f)
    print(scale)
    assert scale == 0'''

def test_convert_scale_B():
    scale = convert_scale('2B')
    print(scale)
    assert scale == 2000000000