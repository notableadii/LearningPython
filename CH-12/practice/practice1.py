try:
    with open("CH-12/practice/1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(f"An error occurred: {e}")
try:
    with open("CH-12/practice/2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(f"An error occurred: {e}")
try:
    with open("CH-12/practice/3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(f"An error occurred: {e}")


print("End of file reading process.")
