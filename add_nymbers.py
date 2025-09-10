def add_numbers(num1, num2):
    """
    Adds two numbers and returns the result.
    
    Args:
        num1 (float): The first number to add.
        num2 (float): The second number to add.
    
    Returns:
        float: The sum of num1 and num2.
    """
    return num1 + num2

def main():
    # Get user input for the two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Calculate and display the result
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()