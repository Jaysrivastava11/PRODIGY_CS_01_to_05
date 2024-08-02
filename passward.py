import re

def assess_password_strength(password):
    # Define criteria
    criteria = {
        'length': len(password) >= 8,
        'uppercase': re.search(r'[A-Z]', password) is not None,
        'lowercase': re.search(r'[a-z]', password) is not None,
        'number': re.search(r'\d', password) is not None,
        'special_char': re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None,
    }
    
    # Evaluate criteria
    strength = sum(criteria.values())
    
    # Provide feedback based on the number of criteria met
    if strength == 5:
        feedback = "Excellent: Your password is very strong!"
    elif strength == 4:
        feedback = "Good: Your password is strong but could be improved."
    elif strength == 3:
        feedback = "Fair: Your password is acceptable but should be stronger."
    elif strength == 2:
        feedback = "Weak: Your password is weak and should be improved."
    else:
        feedback = "Very Weak: Your password is too weak and needs significant improvement."
    
    return feedback

# Example usage
password = input("Enter your password to assess its strength: ")
feedback = assess_password_strength(password)
print(feedback)
 