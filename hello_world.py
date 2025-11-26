from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()  
queue.popleft()   
print(queue)         
def calculator(a, b, op):
    """
    Perform a calculation on two numbers based on the given operator.

    Args:
        a (float or int): The first operand.
        b (float or int): The second operand.
        op (str): The operation to perform. Supported: '+', '-', '*', '/', 'a**a', 'b**b'.

    Returns:
        float or int: The result of the calculation.

    Raises:
        ValueError: If an invalid operator is provided.
        ZeroDivisionError: If division by zero is attempted.
    """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b
    elif op == 'a**a':
        return a ** a
    elif op == 'b**b':
        return b ** b
    else:
        raise ValueError(f"Invalid operator: {op}")

print(calculator(5, 3, '+'))
a = "Hello, World!"
print(a.upper())
print("gigione")