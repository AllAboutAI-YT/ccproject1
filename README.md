# Email Validation Library

A Python library for validating email addresses using regular expressions and proper validation rules.

## Features

- Validate email format using regex pattern
- Check for invalid inputs (none, non-string)
- Simple API with boolean return values

## Usage

```python
from cc import validate_email

# Validate an email address
is_valid = validate_email("user@example.com")  # Returns True

# Invalid examples
validate_email(None)  # Returns False
validate_email("")  # Returns False
validate_email("invalid@email")  # Returns False
```

## License

MIT