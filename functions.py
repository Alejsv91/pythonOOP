global_variable: str = "This is my global variable"

# 1
def first_function():
    print("This is my first function")
    second_function()

# 2 
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
    split_value = value.split("-")
    split_value.sort()
    return split_value

# 7
def prime_numbers(numbers: list[int]) -> bool:
    prime_list: list[int] = []
    for n in numbers:
        if n <= 1:
            continue
        
        for divisor in range(2,int(n ** 0.5) + 1):
            if n% divisor == 0:
                break
        else:
            prime_list.append(n)
    
    return prime_list
            
    



# first_function()
# print(global_variable)
# print(reverse_string("First test"))
# print(f"Total upper: {count_upper_cases("This Is My Value")}")

# value = "this-is-my-test"
# print(f"Ordered{order_string(value)}")

number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(f"The prime numbers are: {prime_numbers(number_list)}")