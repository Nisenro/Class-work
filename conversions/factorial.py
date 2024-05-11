'''
In your script factorial.py, create a function factorial that takes a non-negative integer n and returns the factorial of that number n.aIt should call this function and ask the user for input in the if __name__ == "__main__": block. 
Also add input validation and fail gracefully if the user did not input a non-negative integer by printing “Please input a non-negative integer.” to the screen.
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result = result * i
        return result
    
def valid_input(input):
    if input.isdigit():
        num = int(input)
        if num >= 0:
            return num
        else:
            print("Please input a non-negative number")
            return None
    else:
        print("Please input a non-negative number")
        return None
    
if __name__ == "__main__":
    num = valid_input(input("Enter a non-negative integer: "))
    if num is not None:
        result = factorial(num)
        print(result)

