## Datetime Module

import datetime

def get_current_datetime():
    """Get the current date and time using the datetime module."""
    return datetime.datetime.now()

current_time = get_current_datetime()
print(f"Current date and time: {current_time}")
