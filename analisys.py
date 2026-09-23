def bubble_sort(my_list: list[int]): # O(n^2)
    if not isinstance(my_list, list):
        raise TypeError("This sort only works with a list")
    
    for outer_index in range(len(my_list) -1):
        print(f'iteration index: {outer_index}')
        for index in range(len(my_list) -1 , outer_index, -1):
            current_value = my_list[index]
            next_value = my_list[index - 1]
            if(current_value < next_value):
                print(f"{current_value} is less than {next_value}")
                my_list[index - 1] = current_value
                my_list[index ]= next_value
                print(f"moving {my_list[index - 1]} to index {index - 1} and {my_list[index]} to index: {index}")
                print(my_list)
            else:
                print(f"{current_value} is higher than {next_value}")
            print(f"---- index is {index} and value is {my_list[index]} ----")
    print("--- Final list ---")
    print(my_list)
    return my_list

def print_numbers_times_2(numbers_list): #o(n)
	for number in numbers_list:
		print(number * 2)
  
def check_if_lists_have_an_equal(list_a, list_b): # O(n^2)
	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:
				return True
				
	return False

def print_10_or_less_elements(list_to_print): # o(1)
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index])
  
def generate_list_trios(list_a, list_b, list_c): # O(n^3)
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 
