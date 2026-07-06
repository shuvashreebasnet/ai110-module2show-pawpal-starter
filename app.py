import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan", key="owner_name_input")
owner_email = st.text_input("Email", value="example@example.com", key="owner_email_input")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(owner_id=1, owner_name=owner_name or "Jordan", email= owner_email or "example@example.com")

owner = st.session_state.owner

if owner_name and owner.owner_name != owner_name:
    owner.update_owner_info(owner_name=owner_name)
    st.session_state.owner = owner

st.markdown("### Add a pet")
with st.form("add_pet_form"):
    new_pet_name = st.text_input("Pet name", key="new_pet_name")
    new_pet_age = st.number_input("Age", min_value=0, max_value=30, value=2, step=1, key="new_pet_age")
    species = st.selectbox("Species", ["dog", "cat", "other"], key="species_select")
    submitted = st.form_submit_button("Add pet")

    if submitted:
        if new_pet_name.strip():
            pet = Pet(name=new_pet_name.strip(), age=int(new_pet_age))
            owner.add_pet(pet)
            st.session_state.owner = owner
            st.success(f"{pet.name} added to your pet list.")
        else:
            st.warning("Please enter a pet name.")

if owner.pets:
    st.markdown("### Current pets")
    pet_rows = [{"name": pet.name, "age": pet.age} for pet in owner.pets]
    st.table(pet_rows)
else:
    st.info("No pets added yet.")

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3, col4 = st.columns(4)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["Low", "Medium", "High"], index=2)
with col4:
    pet = st.selectbox("Pet",[pet.name for pet in owner.pets])

if st.button("Add task"):
    st.session_state.tasks.append(
        {"Title": task_title, "Duration (minutes)": int(duration), "Priority": priority, "Pet": pet}
    )
    tasks = st.session_state.tasks

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("Create a schedule from the tasks stored in your session.")

if st.button("Generate schedule"):
    if not st.session_state.get("tasks"):
        st.info("Add at least one task before generating a schedule.")
    elif not owner.pets:
        st.info("Add at least one pet before generating a schedule.")
    else:
        for pet in owner.pets:
            pet.tasks.clear()

        for task_data in st.session_state.tasks:
            matching_pet = next((pet for pet in owner.pets if pet.name == task_data.get("Pet")), None)
            if matching_pet is None:
                continue

            task = Task(
                description=task_data.get("Title", "Untitled task"),
                due_time="TBD",
                priority=str(task_data.get("Priority", "medium")).lower(),
            )
            matching_pet.add_task(task)

        scheduler = Scheduler(start_time="08:00", end_time="20:00", duration=0, owner=owner)
        planned_tasks = scheduler.create_schedule()

        if planned_tasks:
            st.success("Schedule created.")
            for index, task in enumerate(planned_tasks, start=1):
                st.write(f"{index}. {task.description} — Priority: {task.priority}")
        else:
            st.info("No tasks were included in the schedule.")
