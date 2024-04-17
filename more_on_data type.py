def remove_vowels(string):
    vowels = "aeiouAEIOU"
    # Use list comprehension to create a new string with vowels removed
    string_without_vowels = ''.join([char for char in string if char not in vowels])
    return string_without_vowels

# Accept input from the user
input_string = input("Enter a string: ")

# Call the remove_vowels function and display the result
result = remove_vowels(input_string)
print("String after removing vowels:", result)
