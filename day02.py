def main():
    # Ask the user for their age
    age_input = input("Enter your age: ")

    # Convert the input to an integer
    age = int(age_input)

    # Create a greeting message using an f-string
    message = f"You are {age} years old!"

    # Print the message
    print(message)

if __name__ == "__main__":
    main()