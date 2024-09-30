#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip if the element is not an integer
            continue
        except IndexError:
            # If we try to access out of range, stop the loop
            break
    print()  # Print new line after all integers
    return count
