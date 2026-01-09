# Todo Service API Contract

## Purpose
Defines the interface between the CLI layer and the service layer for the Todo application.

## Service Interface

### TodoService Class

#### Methods

**`add_task(title: str, description: str = None) -> int`**
- **Purpose**: Add a new task to the collection
- **Parameters**:
  - `title` (str): Task title (1-200 characters)
  - `description` (str, optional): Task description (0-1000 characters)
- **Returns**: int - The ID of the newly created task
- **Raises**: ValueError if title is invalid
- **Post-condition**: Task exists in storage with 'completed' = False

**`list_tasks() -> List[dict]`**
- **Purpose**: Retrieve all tasks
- **Returns**: List of task dictionaries containing id, title, description, and completed status
- **Order**: Tasks listed in creation order
- **Empty case**: Returns empty list if no tasks exist

**`update_task(task_id: int, title: str = None, description: str = None) -> bool`**
- **Purpose**: Update an existing task
- **Parameters**:
  - `task_id` (int): ID of the task to update
  - `title` (str, optional): New title if provided
  - `description` (str, optional): New description if provided
- **Returns**: bool - True if update successful, False if task not found
- **Validation**: Title must follow same rules as add_task if provided

**`delete_task(task_id: int) -> bool`**
- **Purpose**: Remove a task from the collection
- **Parameters**: `task_id` (int): ID of the task to delete
- **Returns**: bool - True if deletion successful, False if task not found
- **Post-condition**: Task no longer exists in storage

**`toggle_task_completion(task_id: int) -> bool`**
- **Purpose**: Toggle the completion status of a task
- **Parameters**: `task_id` (int): ID of the task to toggle
- **Returns**: bool - True if toggle successful, False if task not found
- **Behavior**: If task was incomplete, marks as complete; if complete, marks as incomplete

## Storage Interface

### InMemoryStorage Class

#### Methods

**`add_task(task: dict) -> int`**
- **Purpose**: Store a new task
- **Parameters**: `task` (dict): Task dictionary with title, description, completed
- **Returns**: int - The assigned ID of the task
- **Post-condition**: Task is stored with unique ID

**`get_task(task_id: int) -> dict or None`**
- **Purpose**: Retrieve a task by ID
- **Parameters**: `task_id` (int): ID of the task to retrieve
- **Returns**: dict - Task data if found, None if not found

**`update_task(task_id: int, task_data: dict) -> bool`**
- **Purpose**: Update a task's data
- **Parameters**:
  - `task_id` (int): ID of the task to update
  - `task_data` (dict): New task data
- **Returns**: bool - True if update successful, False if task not found

**`delete_task(task_id: int) -> bool`**
- **Purpose**: Remove a task from storage
- **Parameters**: `task_id` (int): ID of the task to delete
- **Returns**: bool - True if deletion successful, False if task not found

**`list_all_tasks() -> List[dict]`**
- **Purpose**: Retrieve all stored tasks
- **Returns**: List of all task dictionaries in creation order