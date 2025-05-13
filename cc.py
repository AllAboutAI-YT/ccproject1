import re

def validate_email(email):
    """
    Validates if the input string is a properly formatted email address.
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if email is valid, False otherwise
    """
    # Regular expression for validating an email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if email is None or not a string
    if email is None or not isinstance(email, str):
        return False
    
    # Check if email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False