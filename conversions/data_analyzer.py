max_num = None
min_num = None

while True:
    user_input = input("Input: ")
    if user_input == "" or user_input == "stop":
        break
    if user_input.isdigit():
        if max_num is None or user_input > max_num:
            max_num = user_input
        if min_num is None or user_input < min_num:
            min_num = user_input
print("Maximum: " + max_num)
print("Minimum: " + min_num)





