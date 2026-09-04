
# TODO: Read the user's name, age, and height from input
# TODO: Print: Hello, <name>! You are <age> years old and your height is <height> cm.

def main():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    height = input("Enter your height in cm: ")
    int(age)
    float(height)
    print(f"Hello, {name}! You are {age} years old and your height is {height} cm. ")
    

if __name__ == "__main__":
    main()