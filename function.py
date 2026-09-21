global_variable: str = "This is my global variable"

# 1
def first_function():
    print("This is my first function")
    second_function()
    
def second_function():
    global global_variable
    print("This is my second function")
    global_variable = "Value change from second_function"
    print(global_variable)

# 3    
def sum_number_list(my_list: list[int]):
    result = 0
    for number in my_list:
        result += number
    return result

# 4
def reverse_string(value: str):
    return value[::-1]

# 5
def count_upper_cases(value: str):
    upper_counter: int = 0
    for l in value:
        if l.isupper():
            upper_counter += 1
    
    return  upper_counter

# 6
def order_string(value: str):
    pass
    



# first_function()
# print(global_variable)
# print(reverse_string("First test"))
print(f"Total upper: {count_upper_cases("This Is My Value")}")