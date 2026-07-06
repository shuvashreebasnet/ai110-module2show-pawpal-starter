import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pawpal_system import Owner, Pet, Task, Scheduler
import datetime


def test_mark_complete_changes_task_status():
    task = Task(description="Feed cat", due_time=datetime.time(9, 0), frequency=1)

    task.mark_complete()

    assert task.completion_status == "completed"


def test_adding_task_increases_pet_task_count():
    pet = Pet(name="Mochi", age=3)
    task = Task(description="Walk", due_time=datetime.time(18, 0), frequency=1)

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0] is task


def test_scheduler_sorts_tasks_by_due_time():
    owner = Owner(owner_id=1, owner_name="Jordan", email="jordan@example.com")
    pet = Pet(name="Mochi", age=3)
    task1 = Task(description="Breakfast", due_time=datetime.time(9, 0), frequency=1)
    task2 = Task(description="Lunch", due_time=datetime.time(12, 0), frequency=1)
    task3 = Task(description="Snack", due_time=datetime.time(10, 30), frequency=1)

    pet.add_task(task2)
    pet.add_task(task3)
    pet.add_task(task1)
    owner.add_pet(pet)

    scheduler = Scheduler(start_time="08:00", end_time="20:00", duration=12, owner=owner)
    schedule = scheduler.sort_by_time()

    assert [task.due_time for task in schedule] == [datetime.time(9, 0), datetime.time(10, 30), datetime.time(12, 0)]


def test_scheduler_filters_tasks_by_pet_name():
    owner = Owner(owner_id=1, owner_name="Jordan", email="jordan@example.com")
    pet1 = Pet(name="Mochi", age=3)
    pet2 = Pet(name="Kiki", age=2)
    task1 = Task(description="Breakfast", due_time=datetime.time(9, 0), pet_name="Mochi")
    task2 = Task(description="Lunch", due_time=datetime.time(12, 0), pet_name="Kiki")
    task3 = Task(description="Snack", due_time=datetime.time(10, 30), pet_name="Mochi")

    pet1.add_task(task1)
    pet1.add_task(task3)
    pet2.add_task(task2)
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    scheduler = Scheduler(start_time="08:00", end_time="20:00", duration=12, owner=owner)
    schedule = scheduler.sort_by_pet("Mochi")

    assert [task.pet_name for task in schedule] == ["Mochi", "Mochi"]
    assert [task.description for task in schedule] == ["Breakfast", "Snack"]


def test_owner_can_add_pet():
    owner = Owner(owner_id=1, owner_name="Jordan", email="jordan@example.com")
    pet = Pet(name="Mochi", age=3)

    owner.add_pet(pet)

    assert len(owner.pets) == 1
    assert owner.pets[0] is pet
