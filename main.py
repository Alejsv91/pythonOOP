from datetime import date

# Ejericio 1
def repeat_twice(func):
    def wrapper(string: str):
        func(string)
        func(string)
        
    return wrapper

@repeat_twice
def func_test(string: str):
    print(f'Hola, {string}')
    
func_test("Ale")


# Ejercicio 2
user_logger_in = True

def require_login(func):
    def wrapper(name: str):
        if not user_logger_in:
            raise PermissionError(f"User {name} is not authenticated!")
        func(name)
        
    return wrapper

@require_login
def welcome_message(name: str):
    print(f"Bienvenido {name}")
    
welcome_message("Alejandro")

# Ejercicio 3
def log_call(func):
    def wrapper(*args):
        result = func(*args)
        
        print(f"function name: {func.__name__}")
        print(f"function arguments: {args}")
        print(f"date: {date.today()}")
        print(f"result: {result}")
        
        return result
        
    return wrapper

def validate_numbers(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"argument {arg} is not a float")
            
        return func(*args)
    
    return wrapper

@log_call
@validate_numbers
def multiply(a: float, b: float):
    return a * b

multiply(2,2)


    

    