from calculator import square
import pytest
def main():
    test_square()
    
def test_square():
    if square(2) == 4:
        print("Test Passed: square(2) is 4")
    try:
        assert square(4) == 9
    except AssertionError:
        print("not")
def test_str():
    with pytest.raises(TypeError):
        print("False")
        
if __name__ == "__main__":
    main()
    
