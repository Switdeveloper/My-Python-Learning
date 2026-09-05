# Ask the user for their personal information
# Store each answer in a variable with the correct data type
# Print a friendly summary using an f-string

def main():
    # TODO: collect name, age, height, coding preference
    name=input("what your name? ")
    age=int(input("what your age? "))
    height=float(input("what your height? "))
    coding=bool(input(" you love coding y/n? "))
    print(f"Hello {name}! You are {age}years old, {height} feet tall, and you like encoding {coding}")


    # TODO: convert age to int, height to float, coding preference to bool
    # TODO: print the summary
    pass

if __name__ == '__main__':
    main()