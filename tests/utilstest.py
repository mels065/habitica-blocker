import unittest
from freezegun import freeze_time
from datetime import date, datetime

from utils.util import *

def createDailyMock(is_due=True, completed=False):
    return {"isDue": is_due, "completed": completed}

class TestAreAllComplete(unittest.TestCase):
    def test_empty_list(self):
        self.assertIs(are_all_complete([]), True, "Empty list should return true")

    def test_not_due_dailies(self):
        msg = "Should return true for list with all dailies that are not due"
        self.assertIs(are_all_complete([createDailyMock(is_due=False)]), True, msg)
        dailies = [createDailyMock(is_due=False) for i in range(5)]
        self.assertIs(are_all_complete(dailies), True, msg)

    def test_due_completed_dailies(self):
        msg = "Should return true for dailies that are due and completed"
        self.assertIs(are_all_complete([createDailyMock(completed=True)]), True, msg)
        dailies = [createDailyMock(completed=True) for i in range(5)]
        self.assertIs(are_all_complete(dailies), True, msg)
    
    def test_due_incomplete_dailies(self):
        msg = "Should return false if at least one daily is not completed"
        self.assertIs(are_all_complete([createDailyMock()]), False, msg)
        dailies = [createDailyMock(completed=True) for i in range(5)]
        dailies[2]["completed"] = False
        self.assertIs(are_all_complete(dailies), False, msg)

@freeze_time("2001-01-02")
class IsEarlyMorning(unittest.TestCase):
    def test_not_same_day(self):
        date_completed = datetime.today().replace(day=1)
        self.assertFalse(is_early_morning(date_completed), "Should return false if it is not the same day")
    
    def test_same_day_after_six(self):
        msg = "Should return false if same day, but after 6"
        date_completed = datetime.today().replace(hour=6)
        self.assertFalse(is_early_morning(date_completed), msg)

    def test_same_day_before_six(self):
        msg = "Should return true if same day and after 6"
        date_completed = datetime.today().replace(hour=5)
        self.assertTrue(is_early_morning(date_completed), msg)

if __name__ == '__main__':
    unittest.main()