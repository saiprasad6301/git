def is_palindrome(text):
    return text == text[::-1]

while True:
    user_input = input("Enter a word or sentence to check (or 'exit' to quit): ").replace(" ", "").lower()
    if user_input == "exit":
        break
    if is_palindrome(user_input):
        print("Yes! It's a palindrome.")
    else:
        print("No, not a palindrome.")

