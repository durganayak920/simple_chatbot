def divide_numbers(num1, num2):
    """
    Divides num1 by num2 and returns the result.

    Args:
        num1 (float): The numerator.
        num2 (float): The denominator.

    Returns:
        float: The result of division.

    Raises:
        ValueError: If num2 is zero.
    """
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

def main():
    # Get user input for the two numbers
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))

    try:
        result = divide_numbers(num1, num2)
        print(f"The result of {num1} divided by {num2} is: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()