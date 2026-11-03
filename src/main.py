import argparse
from src.calculator import add, subtract, multiply, divide

def main():
    parser = argparse.ArgumentParser(description="A simple CLI calculator.")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="The operation to perform")
    parser.add_argument("a", type=float, help="The first number")
    parser.add_argument("b", type=float, help="The second number")

    args = parser.parse_args()

    try:
        if args.operation == "add":
            result = add(args.a, args.b)
        elif args.operation == "subtract":
            result = subtract(args.a, args.b)
        elif args.operation == "multiply":
            result = multiply(args.a, args.b)
        elif args.operation == "divide":
            result = divide(args.a, args.b)

        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
