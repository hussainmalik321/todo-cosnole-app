# Phase-1 Todo In-Memory Console Application

A Python-based command-line todo application that stores all data in memory during runtime. No data persistence is required - all tasks are lost when the application exits.

## Features

- **Add Tasks**: Create new tasks with titles and optional descriptions
- **View Tasks**: Display all existing tasks with their status
- **Update Tasks**: Modify existing tasks by ID
- **Delete Tasks**: Remove tasks by ID
- **Toggle Completion**: Mark tasks as complete/incomplete
- **Input Validation**: Ensures titles are 1-200 characters, descriptions are 0-1000 characters
- **Error Handling**: Friendly error messages and prevents crashes
- **Menu-Driven Interface**: Simple numbered menu system for navigation

## Prerequisites

- Python 3.13 or higher

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <repository-name>
   ```

## Usage

Run the application:
```bash
python main.py
```

The application will display a menu with the following options:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit Application

Follow the on-screen prompts to interact with the application.

## Project Structure

```
├── main.py                 # Application entry point
├── src/
│   └── todo_app/
│       ├── __init__.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── task.py     # Task data model with validation
│       ├── services/
│       │   ├── __init__.py
│       │   └── todo_service.py  # Business logic layer
│       ├── storage/
│       │   ├── __init__.py
│       │   └── in_memory_storage.py  # In-memory storage implementation
│       └── cli/
│           ├── __init__.py
│           └── todo_cli.py   # Command-line interface
├── README.md
└── .gitignore
```

## Architecture

The application follows a layered architecture:
- **CLI Layer**: Handles user interaction and menu system
- **Service Layer**: Contains business logic for todo operations
- **Storage Layer**: Manages in-memory data storage
- **Model Layer**: Defines the Task data structure

## Data Model

- **Task**:
  - `id`: integer (unique, auto-increment)
  - `title`: string (required, 1-200 characters)
  - `description`: string | null (optional, 0-1000 characters)
  - `completed`: boolean (default: False)

## Error Handling

The application includes comprehensive error handling:
- Invalid menu choices show error and re-display menu
- Invalid task IDs show friendly error message
- Empty titles are rejected with explanation
- The application never crashes due to bad input

## Limitations

- Data is stored only in memory and is lost when the application exits
- Single-user application
- No external dependencies beyond Python standard library

## Development

This project was created using Spec-Driven Development methodology with the following phases:
1. Constitution
2. Specification
3. Planning
4. Tasks
5. Implementation

## Contributing

This project is part of Hackathon II: Spec-Driven Development and is in Phase-1. Contributions for future phases are welcome.

## License

[Specify license type if applicable]