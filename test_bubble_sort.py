import pytest
from bubble_sort import bubble_sort

def test_bubble_sort_with_small_list():
    # Arrange
    small_list: int = [1,8,2,9]
    expected_list: int = [1,2,8,9]
    # Act
    result = bubble_sort(small_list)
    # Assert
    assert result == expected_list
    
def test_bubble_sort_with_100_list():
    # Arrange
    bigger_list = [90, 51, 39, 30, 52, 10, 81, 18, 59, 34, 85, 66, 94, 82, 15, 1, 99, 95, 50, 32, 20, 8, 23, 
                                       6, 74, 88, 7, 2, 26, 69, 28, 70, 17, 72, 76, 19, 62, 73, 48, 63, 35, 
                                       61, 9, 91, 47, 41, 68, 22, 56, 11, 64, 98, 38, 93, 12, 57, 87, 13, 58, 
                                       37, 97, 55, 79, 53, 75, 45, 43, 3, 14, 29, 42, 77, 4, 33, 27, 80, 46, 
                                       21, 24, 5, 100, 49, 83, 67, 36, 84, 89, 40, 25, 92, 44, 78, 16, 71, 
                                       60, 54, 65, 96, 31, 86]
    
    expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                                      21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
                                      39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                                      57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 
                                      75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 
                                      93, 94, 95, 96, 97, 98, 99, 100]

    # Act
    result = bubble_sort(bigger_list)
    # Assert
    assert result == expected_list
    
def test_bubble_sort_works_with_list():
    # Arrange
    empty_list =  []
    expected_list = []
    # Act
    result = bubble_sort(empty_list)
    # Assert
    assert result == expected_list
    
def test_bubble_sort_is_not_working_when_parameter_is_not_a_list():
    # Arrange
    parameter =  "test"
    # Act & Assert
    with pytest.raises(TypeError):
        bubble_sort(parameter)