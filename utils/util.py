from datetime import datetime

def are_all_complete(dailies) -> bool:
    for daily in dailies:
        if daily["isDue"] and not daily["completed"]:
            return False
    return True
