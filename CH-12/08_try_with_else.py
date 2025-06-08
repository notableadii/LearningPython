
try:
    
  a = int(input("\nEnter a number: "))
  print(f"You entered: {a}")


except Exception as e:
    print(f"\nAn error occurred: {e}")  
    
else:
    print(f"\nYou entered a valid number: {a}")