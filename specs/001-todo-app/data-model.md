# Data Model: Phase-1 Todo In-Memory Console Application

## Task Entity

**Fields:**
- `id`: integer (unique, auto-increment)
- `title`: string (required, max 200 characters)
- `description`: string | null (optional, max 1000 characters)
- `completed`: boolean (default: False)

**Validation Rules:**
- `id`: Must be unique and auto-incremented
- `title`: Must not be empty, must be between 1-200 characters
- `description`: Optional, if provided must be 0-1000 characters
- `completed`: Boolean value, default False

**State Transitions:**
- `incomplete` → `completed` (when task is marked complete)
- `completed` → `incomplete` (when task is marked incomplete)

**Relationships:**
- None (standalone entity)

## TaskCollection (In-Memory Storage)

**Structure:**
- `tasks`: list of Task entities
- `next_id`: integer counter for auto-incrementing IDs

**Operations:**
- `add(task)`: Add a new task to the collection
- `get_by_id(id)`: Retrieve task by ID
- `update(task)`: Update an existing task
- `delete(id)`: Remove task by ID
- `list_all()`: Return all tasks in creation order

**Constraints:**
- All data exists only during runtime
- All data is lost when application exits
- IDs are unique within the session