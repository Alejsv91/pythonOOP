def print_params(func):
    def wrapper(*args, **kwargs):
        print(f"Argumentos: {args}")
        print(f"Keyword arguments: {kwargs}")

        result = func(*args, **kwargs)

        print(f"Retorno: {result}")
        return result

    return wrapper

@print_params
def test_function(test_param: str, **kwargs):
    print("This is a test")
    return f"Received: {test_param}"

test_function("First test", k_test="k value")

def validate_parameters(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError(f"{arg} is not int")
            
        return func(*args)

    return wrapper


@validate_parameters
def sumar(*args):
    return sum(args)

print(f"La suma es: {sumar(1,2,3,4,5,6,7)}")

print(f"La segunda suma es: {sumar(1,2,3,4,5,6,7, "T")}")