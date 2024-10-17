import re

def assess_password_strength(password):
    strength_score = 0

    # Check for length of at least 8 characters
    if len(password) >= 8:
        strength_score += 1

    # Check for presence of lowercase letters
    if re.search("[a-z]", password):
        strength_score += 1

    # Check for presence of uppercase letters
    if re.search("[A-Z]", password):
        strength_score += 1

    # Check for presence of digits
    if re.search("[0-9]", password):
        strength_score += 1

    # Check for presence of special characters
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1

    # Provide feedback based on the strength score
    if strength_score == 5:
        return "Password Strength: Strong"
    elif strength_score == 4:
        return "Password Strength: Medium"
    elif strength_score == 3:
        return "Password Strength: Weak"
    else:
        return "Password Strength: Very Weak"

def main():
    password = input("Enter a password to check its strength: ")
    print(assess_password_strength(password))

if __name__ == "__main__":
    main()
