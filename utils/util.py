def are_all_complete(dailies):
    for daily in dailies:
        if daily["isDue"] and not daily["completed"]:
            return False
    return True