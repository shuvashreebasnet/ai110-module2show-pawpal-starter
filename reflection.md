# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
The purpose of the app is to make task-tracking for pets easy. The 3 core actions a user should be able to perform are create a task, add/edit basic user and pet information, and view the tasks of today. There are four classes: Owner, Pet, Task, and Scheduler. An Owner can have 0 to many Pets, and an Owner can have 0 to many Tasks. The Scheduler must have at least one task to create a schedule.

- What classes did you include, and what responsibilities did you assign to each?
 I included the Owner, Pet, Task, and Scheduler classes. The Owner class contains the attributes ownerID, owner_name, and email. It can update user information. The pet class contains attribute pet_name. It can add a new pet and update pet information. The task class contains task_name, task_time, task_duration, status, priority and date. The task class allows tasks to be added, updated (both in status and in information), and removed. The scheduler class has the attributes start_time, end_time, and duration. It has the attributes calculate_duration, validate_times, and create_schedule. 

**b. Design changes**

- Did your design change during implementation?
Yes
- If yes, describe at least one change and why you made it.
(1) I moved the methods add_task() and remove_task() to be functions for the Pet class rather than the Task class because (according to AI) "tasks are data objects, but the current design gives them manager-style methods." Therefore, giving the methods to the Pet class will allow tasks to be managed for each pet, and based on my UML the owner manages the pets in the list of pets attribute. AI did actually suggest for the add_task() function to be added to the Owner class, but understanding the relationship that a Pet can have 0 to many tasks made me decide to add it to the Pet class instead.

(2) I updated the relationship between the classes. According to AI, Task initally has no link to Owner or Pet. I updated the UML diagram so that the Task class is linked to the Pet class in which a Pet can have 0 to many Tasks instead of Owner having 0 to many tasks. The relationship between Scheduler and Owner is that an Owner can optionally have one schedule. I also added a list of pets as an attribute for Owner to show that 1 to 0..* relationship between Owner and Pets. I made these changes because logically a schedule cannot be created if there are no tasks for it to work with, and the schedule is created across tasks of multiple Pets which can be obtained by the list of Pets attribute under Owner.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
My schedule considers time as a constraint. However, I would also add priority in the future.
- How did you decide which constraints mattered most?
Time is important so that the schedule is manageable and reasonable to the user.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
The scheduler checks for if the time is greater than or less than another time rather than checking if the durations overlap.
- Why is that tradeoff reasonable for this scenario?
Since duration can differ, having a fixed time for tasks allows users to focus on what time to do the task rather than how long they have. Users also might not know how long a task will take. 

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I used AI to create a UML diagram based on my initial classes, attributes and methods of the app, and to create a skeleton of the generated UML diagram. I used AI for debugging when I would run into conflicts integrating the backend of pawpal_system.py to app.py. I also used it to improve my understanding of streamlit python syntax, specifically with time input.
- What kinds of prompts or questions were most helpful?
Asking why I am getting this error and copying the error from the streamlit browser was helpful because Copilot had the specific error, and was able to give me a specific solution. I also wanted to add a time input for the add task function in the app, and asked how I can verify the time input is in an input like 4:30. By providing a specific example, I recieved 2 specific solutions I could implement and had no errors when I ran the app. 

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
After viewing AI's suggestions for what to improve on the initial UML design, I did not accept its suggestion to add an add_task() method to owner. For a pet care app, if there are no pets, it would not make sense to have a task for a pet. It also suggested to create an add_pet() method for the Owner class.
- How did you evaluate or verify what the AI suggested?
Based on my knowledge of Object-Oriented proramming and the relationships between the classes for this app, I verified what was suggested based on my understanding of the relationship that a pet can have 0 to many tasks, and an owner can have 0 to many pets. Therefore, while I would accept its suggestion for Owner.add_pet(), I would instead move add_task() to be a method for the Pet class.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
I tested if the mark_complete() method would update the status of a task, if an owner is able to add a pet with it being reflected in its attribute list of pets, and if the add_task() method adds the task to the pet's list of tasks. I also tested if the chronologically sorting and pet filtering methods worked correctly on the given tasks. 
- Why were these tests important?
These tests are important to ensure the methods mark_complete(), add_pet(), and add_task() are actually saving the input data to the attributes of the class. Testing for sorting and filtering is also important to ensure tasks can be correctly sorted and filtered by useful categories.

**b. Confidence**

- How confident are you that your scheduler works correctly?
On a scale of 1 to 5, 3 because the filtering and sorting work as intended, but for sorting, I need to also consider duration of the task.
- What edge cases would you test next if you had more time?
I would test if I can add pets with the same name and age. It should not accept that as an input if that pet already exists, and instead display "This pet already esists!"
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I am most satisfied with learning more about how to create various inputs in UI for the streamlit app. Specifically finding out about the time format and selectbox so that the user can add more attributes to the task. I am also really glad I independently figured out how to create a drop down of exisiting pets for when a user wants to link a task to a certain pet. 

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I would add the duration attribute to the task so that I can use it to improve the scheduler class. I would also implement the recurring tasks feature so that tasks categorized as daily or weekly frequency are reflected in the schedules. I would also implement all the sorting and filtering methods into the UI in the app. For a better user experience, I would design the schedule to have a calendar format and a list format for better readability.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
When debugging, always present the error output to the AI model if there is one so that you can get more specific solutions. When asking AI for improvements, make sure to be specific in what the goal is such as creating a sorting method for time. For designing the system, remember that the initial UML design will not necessarily be how you end up implementing the system, but rather be a guideline that allows you to improve as you code.
