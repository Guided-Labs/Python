## Re Module

import re

def find_email(text):
    """Find the first email address in a given text."""
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"
    match = re.search(pattern, text)
    return match.group() if match else None

email = find_email("Contact us at info@example.com.")
print(f"Found email: {email}") 