def find_combinations(string):
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


input_string = input("Enter a string:")
all_combinations = find_combinations(input_string)
print(all_combinations)
