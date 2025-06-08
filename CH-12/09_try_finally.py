def main():
    try:
        a = int(input("\nEnter a number: "))
        print(f"You entered: {a}")
        return

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        return

    finally:  # finally is used in functions to execute a block of code regardless of whether an exception occurred or not without finally the code inside the finally block will not execute
        print("\nHey im inside a finally")


main()
