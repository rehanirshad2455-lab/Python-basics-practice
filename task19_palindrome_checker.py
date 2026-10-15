def is_palindrome(str):
    if(str[::-1] == str):
        print("palindrome")
    else:
        print("not a palindrome")

str = "hello"
is_palindrome(str)