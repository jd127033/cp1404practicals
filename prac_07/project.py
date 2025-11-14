"""Project class to manage project data.
Estimated time: 45 minutes
Actual time: 40
"""


class Project:
    """Represent a project object"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise Project instance.
            name: Project name
            start_date: Project start date
            priority (int): Project priority
            cost_estimate (float): Estimated project cost
            completion_percentage (int): Completion percentage from 0% - 100%
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string representation of project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """returns comparison based on priority."""
        return self.priority < other.priority

    def update_priority(self, new_priority):
        """Updates a project priority."""
        self.priority = new_priority

    def is_complete(self):
        """Check if the project is complete."""
        return self.completion_percentage == 100

    def update_completion(self, new_percentage):
        """Updates completion percentage."""
        self.completion_percentage = new_percentage

    def convert_file_format(self):
        """Convert project to txt file friendly format"""
        return (f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t"
                f"{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}")
