import re
from datetime import datetime

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

def validate_date(date_str, format_str='%Y-%m-%d'):
    """
    Validates if the input string is a properly formatted date.
    
    Args:
        date_str (str): The date string to validate
        format_str (str, optional): The expected date format. Defaults to '%Y-%m-%d'.
        
    Returns:
        bool: True if date is valid, False otherwise
    """
    # Check if date_str is None or not a string
    if date_str is None or not isinstance(date_str, str):
        return False
    
    try:
        # Attempt to parse the date string according to the format
        datetime.strptime(date_str, format_str)
        return True
    except ValueError:
        # If a ValueError is raised, the date format is invalid
        return False