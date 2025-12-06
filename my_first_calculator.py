def calculator():
    """A basic calculator that performs operations on two numbers."""
    print("=== Basic Calculator ===")
    
    try:
        # Get input from user
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        # Perform calculation based on operator
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operator!")
            return
        
        # Display result
        print(f"\n{num1} {operator} {num2} = {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers!")

if __name__ == "__main__":
    calculator()