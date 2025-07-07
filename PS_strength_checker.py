import re #The re module provides tools to search, match, and manipulate strings using regular expressions — patterns used to match character combinations in strings.

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = not re.search(r"[a-z]", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

   
    strength = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

   
    feedback = []
    if length_error:
        feedback.append("Password should be at least 8 characters long")
    if lowercase_error:
        feedback.append("Password should contain at least one lowercase letter")
    if uppercase_error:
        feedback.append("Password should contain at least one uppercase letter")
    if digit_error:
        feedback.append("Password should contain at least one number")
    if special_char_error:
        feedback.append("Password should contain at least one special character (e.g., !, @, #, $)cl")

   
    if strength == 5:
        level = "Strong "
    elif strength >= 3:
        level = "Moderate"
    else:
        level = "Weak"

    return strength, level, feedback


if __name__ == "__main__":
    user_password = input("Enter your password to check its strength: ")
    strength_score, strength_level, feedback_messages = check_password_strength(user_password)

    print("\nPassword Strength Level:", strength_level)
    print("Score (out of 5):", strength_score)

    if feedback_messages:
        print("\nSuggestions to improve your password:")
        for msg in feedback_messages:
            print("-", msg)
