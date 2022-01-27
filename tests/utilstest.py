import unittest

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

if __name__ == '__main__':
    unittest.main()