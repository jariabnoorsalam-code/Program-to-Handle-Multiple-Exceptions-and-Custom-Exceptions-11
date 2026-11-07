# Program to Handle Multiple Exceptions
# and Custom Exceptions
class InvalidAgeError(Exception):
    pass
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Division Result:", result)
    age = int(input("Enter your age: "))
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above!")
    print("You are eligible.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
except InvalidAgeError as e:
    print("Custom Exception:", e)
except Exception as e:
    print("Unexpected Error:", e)
finally:
    print("Program execution completed.")
