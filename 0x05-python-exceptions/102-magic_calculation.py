def magic_calculation(a, b):
    result = 0  # Initialize result to 0
    
    for i in range(1, 3):  # Loop over range(1, 3)
        try:
            if i > a:  # If i is greater than a, raise an exception
                raise Exception('Too far')
            else:
                result += a ** b / i  # Otherwise, perform the calculation and add to result
        except Exception:
            result = b + a  # If an exception occurs, set result to b + a
            break  # Exit the loop after handling the exception
    
    return result  # Return the final result

# Test function call
print(magic_calculation(2, 3))
