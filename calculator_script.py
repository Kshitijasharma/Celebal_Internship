def main():
    print("Welcome to the Python Calculator!")
    print("Enter an expression (e.g., 1+2, 4-3, 6*7, 8/4)")

    while True:
        # Take input from the user
        expression = input("Enter expression: ")

        try:
            # Evaluate the expression
            result = eval(expression)
            print(f"The result of {expression} is {result}")
        except Exception as e:
            print(f"Invalid input: {e}")

        # Check if the user wants another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

    print("Thank you for using the Python Calculator.")

if __name__ == "__main__":
    main()
