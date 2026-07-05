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
        self.completion_status = "completed"


@dataclass
class Pet:
    name: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def update_pet_info(self, name: Optional[str] = None, age: Optional[int] = None) -> None:
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        if task in self.tasks:
            self.tasks.remove(task)

    def list_tasks(self) -> List[Task]:
        return self.tasks


@dataclass
class Owner:
    owner_id: int
    owner_name: str
    email: str
    pets: List[Pet] = field(default_factory=list)

    def update_owner_info(self, owner_name: Optional[str] = None, email: Optional[str] = None) -> None:
        if owner_name is not None:
            self.owner_name = owner_name
        if email is not None:
            self.email = email

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        if pet in self.pets:
            self.pets.remove(pet)


@dataclass
class Scheduler:
    start_time: str
    end_time: str
    duration: int

    def calculate_duration(self) -> int:
        return self.duration

    def validate_times(self) -> bool:
        return self.start_time < self.end_time

    def create_schedule(self) -> List[Task]:
        return []

