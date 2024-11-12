## Try Block

def divide_numbers(a, b):
    """Divide two numbers and handle division by zero error."""
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result

print(divide_numbers(10, 2))  
print(divide_numbers(10, 0)) 