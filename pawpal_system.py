from dataclasses import dataclass
from datetime import date
from typing import List, Optional


@dataclass
class Pet:
    pet_name: str
    pet_type: Optional[str] = None
    age: Optional[int] = None

    def __init__(self, pet_name: str, pet_type: Optional[str] = None, age: Optional[int] = None) -> None:
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.age = age
        self.tasks: List[Task] = []

    def add_pet(self) -> None:
        """Create or register a pet."""
        if not self.pet_name:
            raise ValueError("Pet name is required to create a pet.")
        if not hasattr(self, "tasks"):
            self.tasks = []

    def update_pet_info(self, pet_name: Optional[str] = None, pet_type: Optional[str] = None, age: Optional[int] = None) -> None:
        """Update pet attributes."""
        if pet_name is not None:
            self.pet_name = pet_name
        if pet_type is not None:
            self.pet_type = pet_type
        if age is not None:
            self.age = age


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
        if owner_name is not None:
            self.owner_name = owner_name
        if email is not None:
            self.email = email

    def add_pet(self, pet: Pet) -> None:
        """Associate a new pet with this owner."""
        self.pets.append(pet)

    def add_task(self, task: Task) -> None:
        """Associate a new task with this owner."""
        self.tasks.append(task)


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

    def create_schedule(self, owner: Owner) -> List[Task]:
        """Arrange tasks into a schedule."""
        all_tasks: List[Task] = []
        for pet in owner.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks
