def find_max(a, b):
    
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None  

def main():
    """Main function to get user input and display the largest number."""
    
    try:
        a = float(input("Enter the first number (a): "))
        b = float(input("Enter the second number (b): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return  

    
    max_number = find_max(a, b)

    
    if max_number is not None:
        print(f"The largest number is: {max_number}")
    else:
        print("Both numbers are equal.")


if __name__ == "__main__":
    main()
