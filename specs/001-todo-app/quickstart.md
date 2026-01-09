# Quickstart Guide: Phase-1 Todo In-Memory Console Application

## Prerequisites
- Python 3.13+ installed
- No external dependencies required

## Setup
1. Clone the repository
2. Navigate to the project directory
3. Run the application: `python main.py`

## Running the Application
```bash
python main.py
```

## Available Commands
Once the application starts, you'll see a menu with the following options:
1. Add Task - Create a new todo task
2. View Tasks - Display all existing tasks
3. Update Task - Modify an existing task
4. Delete Task - Remove a task from the list
5. Mark Task Complete/Incomplete - Toggle task completion status
6. Exit Application - Close the application

## Example Usage
1. Select "1. Add Task" to create a new task
2. Enter a title (required) and description (optional)
3. Use "2. View Tasks" to see all tasks
4. Use other menu options to manage your tasks

## Architecture Overview
- `main.py`: Entry point of the application
- `src/todo_app/cli/todo_cli.py`: Handles user interface and menu
- `src/todo_app/services/todo_service.py`: Contains business logic
- `src/todo_app/storage/in_memory_storage.py`: Manages in-memory task storage
- `src/todo_app/models/task.py`: Defines the Task data model

## Testing
Run the test suite using:
```bash
python -m pytest tests/
```

## Notes
- All data is stored in memory only and will be lost when the application closes
- The application validates all user inputs according to the specification
- Error handling prevents the application from crashing