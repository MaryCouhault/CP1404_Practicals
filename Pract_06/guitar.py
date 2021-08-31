class Guitar:
from datetime import datetime

    def __init__(self, name, year, cost) -> None:
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self) -> str:
        return f"{self.name}, ({self.year}): ${self.cost:.2f}"

    def get_age(self):
        year = datetime.now().year
        return year - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False