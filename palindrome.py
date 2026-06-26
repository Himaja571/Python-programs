def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]     
input_number = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input_number):
    print(f"'{input_number}' is a palindrome.")
else:
    print(f"'{input_number}' is not a palindrome.")
