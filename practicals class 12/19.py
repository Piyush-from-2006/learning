'''Define a function in swapCase(S) in Python that creates and returns
another string with case of all alphabets swapped/interchanged.
e.g. if the string is, S= "Hello NCS"
then the function should return: "hELLO ncs"'''
def swap_case(s):
    swapped_string = ''

    for char in s:
        if char.islower():
            swapped_string += char.upper()
        elif char.isupper():
            swapped_string += char.lower()
        else:
            swapped_string += char

    return swapped_string

# Example usage
S = "Hello NCS"
result = swap_case(S)
print("Swapped case string:", result)  # Output: "hELLO ncs"
