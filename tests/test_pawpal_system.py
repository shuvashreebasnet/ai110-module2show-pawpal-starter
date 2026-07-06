from pawpal_system import Owner, Pet, Scheduler, Task


def test_pet_and_task_are_created_with_defaults():
    task = Task(
        description="Morning walk",
        due_time="08:00",
        frequency=1,
        completion_status="pending",
        priority="high",
    )
    pet = Pet(name="Mochi", age=3, tasks=[task])

    assert pet.name == "Mochi"
    assert pet.age == 3
    assert pet.tasks[0].description == "Morning walk"


def test_owner_can_manage_pets_and_scheduler_can_create_schedule():
    owner = Owner(owner_id=1, owner_name="Jordan", email="jordan@example.com")
    pet_one = Pet(name="Mochi", age=3)
    pet_two = Pet(name="Biscuit", age=5)

    owner.add_pet(pet_one)
    owner.add_pet(pet_two)

    assert owner.pets == [pet_one, pet_two]

    task_one = Task(description="Feed pet", due_time="09:00", frequency=1)
    task_two = Task(description="Morning walk", due_time="08:00", frequency=1)
    pet_one.add_task(task_one)
    pet_two.add_task(task_two)

    scheduler = Scheduler(start_time="08:00", end_time="20:00", duration=12, owner=owner)
    schedule = scheduler.create_schedule()

    assert schedule == [task_one, task_two]
    assert task_one.completion_status == "pending"

    task_one.mark_complete()
    assert task_one.completion_status == "completed"
