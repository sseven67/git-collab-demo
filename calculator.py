
def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    else:
        raise ValueError("Unsupported operation")


if __name__ == "__main__":
    print(calculate(10, 5, "+"))
