def fibonacci(n):
    a, b = 0, 1
    print(a, b, end=" ")
    for _ in range(n - 2):
        a, b = b, a + b
        print(b, end=" ")

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Please input a non-negative integer.")
            else:
                fibonacci(num)
                break
        except ValueError:
            print("Please input a non-negative integer.")
