from datetime import datetime

def are_all_complete(dailies) -> bool:
    for daily in dailies:
        if daily["isDue"] and not daily["completed"]:
            return False
    return True

# Check if it is a new day (after 6am)
def is_new_day(date_completed: datetime) -> bool:
    today = datetime.now()
    morning = today.replace(hour=6, minute=0, second=0, microsecond=0)
    return (
        (is_early_morning(date_completed)) and
        today >= morning
    )

# Check if the time when the dailies were completed was early morning (12am-5:59am) of the same day
def is_early_morning(date_completed: datetime) -> bool:
    today = datetime.now()
    return date_completed.month == today.month and \
        date_completed.day == today.day and \
        date_completed.year == today.year and \
        date_completed.hour < 6

def was_previous_day(date_completed: datetime) -> bool:
    today = datetime.now()
    return (
        
    )