import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pawpal_system import Pet, Task


def test_mark_complete_changes_task_status():
    task = Task(description="Feed cat", due_time="09:00", frequency=1)

    task.mark_complete()

    assert task.completion_status == "completed"


def test_adding_task_increases_pet_task_count():
    pet = Pet(name="Mochi", age=3)
    task = Task(description="Walk", due_time="18:00", frequency=1)

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0] is task
