import logging

# Configure logging to save logs to a file
logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero.")
        print("Custom Error: Division by zero is not allowed.")
    except TypeError:
        logging.error("Invalid type provided for division.")
        print("Custom Error: Please provide numbers only.")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution of divide_numbers completed.")

def access_list_element(lst, index):
    try:
        value = lst[index]
    except IndexError:
        logging.error("List index out of range.")
        print("Custom Error: The index is out of range.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("Custom Error: An unexpected error occurred.")
    else:
        print(f"Element at index {index}: {value}")
    finally:
        print("Execution of access_list_element completed.")

#  Valid inputs only — guaranteed output
if __name__ == "_main_":
    # Valid division examples
    divide_numbers(100, 25)         # Output: Result: 4.0
    divide_numbers(45, 5)           # Output: Result: 9.0
    divide_numbers(9.0, 3.0)        # Output: Result: 3.0

    # Valid list access examples
    access_list_element([10, 20, 30, 40], 1)  # Output: Element at index 1: 20
    access_list_element(['apple', 'banana', 'cherry'], 2)  # Output: Element at index 2: cherry