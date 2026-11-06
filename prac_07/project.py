import datetime

class Project:
    """Represent a project"""
    def __init__(self, name, start_date, priority, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f'{self.name} {self.start_date} {self.priority} {self.completion_percentage}'

    def __lt__(self, other):
        """Compare projects by priority"""
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == 100

