"""
Personal Information Manager

Create a tuple to store a person's basic info: (name, age, city, country)
Create a list to store their hobbies

Allow the user to:
- Display all information
- Add new hobbies
- Remove hobbies
- Update age (by creating a new tuple)
"""

def personal_info_manager():
    # Create initial person tuple
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")
    country = input("Enter your country: ")

    person = (name, age, city, country)

    # Create hobbies list
    hobbies = input("Enter your hobbies (separated by commas): ").split(",")
    hobbies = [hobby.strip() for hobby in hobbies]

    while True:
        print("\n=== Personal Information Manager ===")
        print("1. Display all information")
        print("2. Add new hobby")
        print("3. Remove hobby")
        print("4. Update age")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nPersonal Information")
            print(f"Name: {person[0]}")
            print(f"Age: {person[1]}")
            print(f"City: {person[2]}")
            print(f"Country: {person[3]}")
            print("Hobbies:", ", ".join(hobbies))

        elif choice == "2":
            hobby = input("Enter a new hobby: ")
            hobbies.append(hobby)
            print("Hobby added!")

        elif choice == "3":
            hobby = input("Enter hobby to remove: ")
            if hobby in hobbies:
                hobbies.remove(hobby)
                print("Hobby removed!")
            else:
                print("Hobby not found!")

        elif choice == "4":
            new_age = int(input("Enter new age: "))
            person = (person[0], new_age, person[2], person[3])
            print("Age updated!")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:
- List of even numbers
- List of odd numbers
- List of numbers greater than the average

Show statistics: sum, average, min, max
"""

def number_operations():
    numbers = []

    # Get 10 numbers from user
    print("\nEnter 10 numbers:")
    for i in range(10):
        num = int(input(f"Number {i + 1}: "))
        numbers.append(num)

    # Display original list
    print(f"\nOriginal numbers: {numbers}")

    # Create filtered lists
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    # Calculate average
    average = sum(numbers) / len(numbers)

    # Numbers greater than average
    above_average = [num for num in numbers if num > average]

    # Display results
    print(f"Even numbers: {even_numbers}")
    print(f"Odd numbers: {odd_numbers}")
    print(f"Numbers greater than average: {above_average}")

    print("\nStatistics")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {average}")
    print(f"Minimum: {min(numbers)}")
    print(f"Maximum: {max(numbers)}")


if __name__ == "__main__":
    personal_info_manager()
    print("\n==============================\n")
    number_operations()