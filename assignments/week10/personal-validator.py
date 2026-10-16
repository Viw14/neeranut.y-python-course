"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("=== PERSONAL INFORMATION VALIDATOR ===")

name = input("Enter your name: ")
age = input("Enter your age: ")
phone = input("Enter your phone number: ")

print("\nValidation Results:")

# Validate Name
if name.strip() != "" and name.replace(" ", "").isalpha():
    print("Name: Valid (contains only letters and spaces)")
    name_valid = True
else:
    print("Name: Invalid (letters and spaces only)")
    name_valid = False

# Validate Age
if age.isdigit():
    age = int(age)
    if 18 <= age <= 65:
        print("Age: Valid ({} years old)".format(age))
        age_valid = True
    else:
        print("Age: Invalid (must be between 18-65)")
        age_valid = False
else:
    print("Age: Invalid (must be a number)")
    age_valid = False

# Validate Phone Number
if phone.isdigit() and len(phone) == 10:
    print("Phone: Valid (10-digit number)")
    phone_valid = True
else:
    print("Phone: Invalid (must contain exactly 10 digits)")
    phone_valid = False

# Display Formatted Information
if name_valid and age_valid and phone_valid:
    if 18 <= age <= 30:
        age_group = "Young Adult"
    elif 31 <= age <= 50:
        age_group = "Adult"
    else:
        age_group = "Senior Adult"

    print("\nFormatted Information:")
    print("Name: {}".format(name.upper()))
    print("Age Group: {} (18-30)".format(age_group) if age_group == "Young Adult"
          else "Age Group: {}".format(age_group))
    print("Phone: +91-{}".format(phone))
else:
    print("\nPlease enter valid information.")
