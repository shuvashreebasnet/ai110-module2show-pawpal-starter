from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    description: str
    due_time: str
    frequency: int = 1
    completion_status: str = "pending"
    priority: str = "medium"

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completion_status = "completed"


@dataclass
class Pet:
    name: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def update_pet_info(self, name: Optional[str] = None, age: Optional[int] = None) -> None:
        """Update the pet's name or age."""
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age

    def add_task(self, task: Task) -> None:
        """Add a task to the pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from the pet's task list."""
        if task in self.tasks:
            self.tasks.remove(task)

    def list_tasks(self) -> List[Task]:
        """Return all tasks assigned to the pet."""
        return self.tasks


@dataclass
class Owner:
    owner_id: int
    owner_name: str
    email: str
    pets: List[Pet] = field(default_factory=list)

    def update_owner_info(self, owner_name: Optional[str] = None, email: Optional[str] = None) -> None:
        """Update the owner's name or email."""
        if owner_name is not None:
            self.owner_name = owner_name
        if email is not None:
            self.email = email

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's pet list."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from the owner's pet list."""
        if pet in self.pets:
            self.pets.remove(pet)


@dataclass
class Scheduler:
    start_time: str
    end_time: str
    duration: int
    owner: Optional[Owner] = None

    def calculate_duration(self) -> int:
        """Return the configured scheduler duration."""
        return self.duration

    def validate_times(self) -> bool:
        """Check whether the scheduler time range is valid."""
        return self.start_time < self.end_time

    def create_schedule(self) -> List[Task]:
        """Collect tasks from all pets owned by the assigned owner."""
        if self.owner is None:
            return []

        tasks: List[Task] = []
        for pet in self.owner.pets:
            tasks.extend(pet.list_tasks())
        return tasks

