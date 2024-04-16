valid_password = input("Your password: ")

if "password" in valid_password or "123456" in valid_password:
    print("The password may not contain the keywords 'password' or '123456'.")
elif valid_password.startswith("qwerty"):
    print("The password may not start with the keyword “qwerty” but it may contain it.")
elif valid_password.isalpha():
    print("The password must contain at least one non-alphabetic character.")
elif valid_password.isdigit():
    print("The password must contain at least one non-digit character.")
elif not any(char in ("$", "@", "!") for char in valid_password):
    print("The password must contain at least one of the following special characters: $, @ or !.")
elif not (any(char.isupper() for char in valid_password) and any (char.islower() for char in valid_password)):
    print("The password must have both uppercase and lowercase letters.")
else:
    print("The password is valid!")