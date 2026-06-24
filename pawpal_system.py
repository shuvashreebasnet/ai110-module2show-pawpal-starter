from dataclasses import dataclass
from datetime import date
from typing import List, Optional


@dataclass
class Pet:
    pet_name: str
    pet_type: Optional[str] = None
    age: Optional[int] = None

    def add_pet(self) -> None:
        """Create or register a pet."""
        pass

    def update_pet_info(self, pet_name: Optional[str] = None, pet_type: Optional[str] = None, age: Optional[int] = None) -> None:
        """Update pet attributes."""
        pass


@dataclass
class Task:
    task_name: str
    task_time: str
    task_duration: int
    status: str
    priority: str
    date: date

    def add_task(self) -> None:
        """Create or register a new task."""
        pass

    def update_task(self, task_name: Optional[str] = None, task_time: Optional[str] = None, task_duration: Optional[int] = None, status: Optional[str] = None, priority: Optional[str] = None, date: Optional[date] = None) -> None:
        """Update task metadata."""
        pass

    def update_task_status(self, status: str) -> None:
        """Change the task status."""
        pass

    def remove_task(self) -> None:
        """Remove this task."""
        pass


class Owner:
    def __init__(self, owner_id: int, owner_name: str, email: str) -> None:
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.email = email
        self.pets: List[Pet] = []
        self.tasks: List[Task] = []

    def update_owner_info(self, owner_name: Optional[str] = None, email: Optional[str] = None) -> None:
        """Update owner profile information."""
        pass

    def add_pet(self, pet: Pet) -> None:
        """Associate a new pet with this owner."""
        pass

    def add_task(self, task: Task) -> None:
        """Associate a new task with this owner."""
        pass


class Scheduler:
    def __init__(self, start_time: str, end_time: str, duration: int) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration

    def calculate_duration(self) -> int:
        """Compute schedule duration."""
        pass

    def validate_times(self) -> bool:
        """Check whether start and end times are valid."""
        pass

    def create_schedule(self, tasks: List[Task]) -> List[Task]:
        """Arrange tasks into a schedule."""
        pass
