def extract_integers(input_list):
    result = [x for x in input_list if isinstance(x, int)]
    return result

# Test the function
input_list = [1, "hello", 42, "world", 7, "foo", 99]
output_list = extract_integers(input_list)
print(output_list)
