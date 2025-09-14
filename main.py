import sys

def cute_banner():
    print("\n✨ Welcome to the Cute Terminal Calculator! ✨")
    print("(づ｡◕‿‿◕｡)づ  Let's do some math!  (｡♥‿♥｡)\n")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Oops! Please enter a valid number. (｡•́︿•̀｡)")

def get_operator():
    ops = ['+', '-', '*', '/']
    while True:
        op = input("Choose an operator (+, -, *, /): ")
        if op in ops:
            return op
        print("Invalid operator! Try again. (╯°□°）╯︵ ┻━┻")

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            print("Division by zero is not allowed! (ಥ﹏ಥ)")
            return None
        return a / b

def main():
    cute_banner()
    a = get_number("Enter the first number: ")
    op = get_operator()
    b = get_number("Enter the second number: ")
    result = calculate(a, b, op)
    if result is not None:
        print(f"\nYour result: {a} {op} {b} = {result}  (✿◠‿◠)")
    print("\nThanks for using the Cute Calculator! (｡•̀ᴗ-)✧\n")

if __name__ == "__main__":
    main()