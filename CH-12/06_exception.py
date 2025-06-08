
try:
    
  a = int(input("\nEnter a number: "))
  print(f"You entered: {a}")

except ValueError:
    print("\nInvalid input! Please enter a valid integer.")
    
except Exception as e:
    print(f"\nAn error occurred: {e}")  
    
print("\nThank You for using our program!\n")  # This line will always execute regardless of exceptions
