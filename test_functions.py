from functions import *

# Test for sum_number_list
def test_sum_number_list_when_list_have_one_value():
    # Arrange
    test_list = [1]
    expected_result = 1
    # Act
    result = sum_number_list(test_list)
    # Assert
    assert result == expected_result
    
def test_sum_number_list_when_list_contains_negative_numbers():
    # Arrange
    test_list = [-10, 12, 20, -100, 200]
    expected_result = 122
    # Act
    result = sum_number_list(test_list)
    # Assert
    assert result == expected_result
    
def test_sum_number_list_when_result_is_negative():
    # Arrange
    test_list = [-1, 50, 275, -1025, 800]
    expected_result = 99
    # Act 
    result = sum_number_list(test_list)
    # Assert
    assert result == expected_result
    
# Test for reverse_string
def test_reverse_string_when_string_contains_special_characters():
    # Arrange
    test_string = "Ale!@#$ñ"
    expected_result = "ñ$#@!elA"
    # Act
    result = reverse_string(test_string)
    # Assert
    assert result == expected_result

def test_reverse_string_when_is_a_long_string():
    # Arrange
    test_string = "Aprendiendo programación orientada a objetos en Python, organizando suites de pruebas dinámicas con pytest para asegurar que todo el código de pythonOOP funcione de manera perfecta y sin errores."
    expected_result = ".serorre nis y atcefrep arenam ed enoicnuf POOnohtyp ed ogidóc le odot euq rarugesa arap tsetyp noc sacimánid sabeurp ed setius odnazinagro ,nohtyP ne sotejbo a adatneiro nóicamargorp odneidnerpA"
    # Act
    result = reverse_string(test_string)
    # Assert
    assert result == expected_result

def test_reverse_string_when_string_is_empty():
    # Arrange
    test_string = ""
    expected_result = ""
    # Act
    result = reverse_string(test_string)
    # Assert
    assert result == expected_result
    
# Test for count_upper_cases
def test_when_string_do_not_contains_uppercase():
    # Arrange
    test_string = 'no uppercases'
    expected_result = 0
    # Act
    result = count_upper_cases(test_string)
    # Assert
    assert result == expected_result

def test_when_string_is_empty():
    # Arrange
    test_string = ""
    expected_result = 0
    # Act
    result = count_upper_cases(test_string)
    # Assert
    assert result == expected_result

def test_when_string_is_long_and_contains_special_characters():
    # Arrange
    test_string = "¡Atención! Un usuario de GitHub (@DevTesting2026) ejecuta hoy 23 suites de pruebas usando pytest."
    expected_result = 6
    # Act
    result = count_upper_cases(test_string)
    # Assert
    assert result == expected_result

# test for order_string
def test_when_is_a_simple_string():
    # Arrange
    test_string = "Pedro-Diego-Enzo-Juan-Eva-Simon"
    expected_result = ['Diego', 'Enzo', 'Eva', 'Juan', 'Pedro', 'Simon']
    # Act
    result = order_string(test_string)
    # Assert
    assert result == expected_result
    
def test_when_is_a_long_string():
    # Arrange
    test_string = "perro-gato-colibri-elefante-jirafa-leon-tigre-oso-lobo-zorro-cebra-hipopotamo-rinoceronte-cocodrilo-serpiente-aguila-halcon-buho-loro-delfin-ballena-tiburon-pulpo-cangrejo-medusa-tortuga-iguana-camaleon"
    expected_result = ['aguila', 'ballena', 'buho', 'camaleon', 'cangrejo', 'cebra', 'cocodrilo', 'colibri', 'delfin', 'elefante', 'gato', 'halcon', 'hipopotamo', 'iguana', 'jirafa', 'leon', 'lobo', 'loro', 'medusa', 'oso', 'perro', 'pulpo', 'rinoceronte', 'serpiente', 'tiburon', 'tigre', 'tortuga', 'zorro']
    # Act
    result = order_string(test_string)
    # Assert
    assert result == expected_result

def test_when_string_contains_numbers():
    # Arrange
    test_string = "1perro-3caballo-2gato-20koala"
    expected_result = ['1perro', '20koala', '2gato', '3caballo']
    # Act
    result = order_string(test_string)
    # Assert
    assert result == expected_result
    
# test for prime_numbers
def test_when_list_contains_standard_prime_numbers():
    # Arrange
    input_list = [2, 3, 4, 5, 16, 17, 20]
    expected_result = [2, 3, 5, 17]
    
    # Act
    result = prime_numbers(input_list)
    
    # Assert
    assert result == expected_result


def test_when_list_contains_no_prime_numbers():
    # Arrange
    input_list = [-5, 0, 1, 9, 15]
    expected_result = []
    
    # Act
    result = prime_numbers(input_list)
    
    # Assert
    assert result == expected_result


def test_when_list_contains_duplicates_and_boundary_values():
    # Arrange
    input_list = [2, 7, 2, 8, 7]
    expected_result = [2, 7, 2, 7]
    
    # Act
    result = prime_numbers(input_list)
    
    # Assert
    assert result == expected_result