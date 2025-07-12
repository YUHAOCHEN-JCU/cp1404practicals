from datetime import datetime

class Project:
    """Represent information about a project."""
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion = int(completion)

    def is_complete(self):
        """Check if the project is fully completed"""
        return self.completion == 100

    def __lt__(self, other):
        """Define less than comparison based on project priority"""
        return self.priority < other.priority

    def __str__(self):
        """Return string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion}%")

    def to_tab_delimited(self):
        """Convert project details to a tab_delimited string for export"""
        return f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost_estimate:.2f}\t{self.completion}"
