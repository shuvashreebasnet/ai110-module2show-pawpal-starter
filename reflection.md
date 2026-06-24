# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
The purpose of the app is to make task-tracking for pets easy. The 3 core actions a user should be able to perform are create a task, add/edit basic user and pet information, and view the tasks of today. There are four classes: Owner, Pet, Task, and Scheduler. An Owner can have 0 to many Pets, and an Owner can have 0 to many Tasks. The Scheduler must have at least one task to create a schedule.

- What classes did you include, and what responsibilities did you assign to each?
 I included the Owner, Pet, Task, and Scheduler classes. The Owner class contains the attributes ownerID, owner_name, and email. It can update user information. The pet class contains attribute pet_name. It can add a new pet and update pet information. The task class contains task_name, task_time, task_duration, status, priority and date. The task class allows tasks to be added, updated (both in status and in information), and removed. The scheduler class has the attributes start_time, end_time, and duration. It has the attributes calculate_duration, validate_times, and create_schedule. 

**b. Design changes**(HERE)

- Did your design change during implementation?
Yes
- If yes, describe at least one change and why you made it.
(1) I moved the methods add_task(), and remove_task() to be functions for the Owner class rather than the Task class because (according to AI) "tasks are data objects, but the current design gives them manager-style methods." Therefore, giving the methods to the Owner class will maintain that the Owner is the only controller of the app.
(2) I updated the relationship between the classes. Task initally has no link to Owner or Pet. Therefore, a task should link to the Owner and the Pet that the task is for. The Pet class also needs an owner reference. Scheduler also needs a relationship back to Owner or Pet. The relationship between Scheduler and Task is updated so that the Scheduler must have at least 1 task (I had added this initally to my reflections doc, but AI did not show the relationship in the diagram).
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
