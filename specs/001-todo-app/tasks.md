# Implementation Tasks: Phase-1 Todo In-Memory Console Application

**Feature**: Phase-1 Todo In-Memory Console Application
**Branch**: 001-todo-app
**Created**: 2026-01-07
**Input**: Plan from `/specs/001-todo-app/plan.md`

## Dependencies

- **User Story 2** depends on **User Story 1** completion (requires core functionality)
- **User Story 3** depends on **User Story 1** completion (requires core functionality)

## Parallel Execution Examples

- Tasks T002-T006 (model, storage, service) can run in parallel as they create independent components
- Tasks T012, T015, T017 (different CLI menu options) can run in parallel as they implement separate features

## Implementation Strategy

- **MVP Scope**: Tasks T001-T011 (User Story 1 - Add and View Tasks)
- **Incremental Delivery**: Complete User Story 1 first, then add User Story 2, then User Story 3
- **Test-Driven**: Each user story includes validation of its acceptance criteria

---

## Phase 1: Project Setup

**Goal**: Initialize project structure and basic configuration files

- [X] T001 Create project directory structure in src/todo_app/ with models/, services/, storage/, cli/ subdirectories
- [X] T002 Create root __init__.py files for all directories (src/, src/todo_app/, and subdirectories)
- [X] T003 Create main.py entry point file with basic structure

---

## Phase 2: Foundational Components

**Goal**: Implement core data models, storage, and service layer

- [X] T004 [P] Create Task model in src/todo_app/models/task.py with id, title, description, completed fields and validation
- [X] T005 [P] Create in-memory storage in src/todo_app/storage/in_memory_storage.py with add, get, update, delete, list operations
- [X] T006 [P] Create todo service in src/todo_app/services/todo_service.py with add_task, list_tasks, update_task, delete_task, toggle_task_completion methods
- [X] T007 [P] Implement validation logic for task titles (1-200 chars) and descriptions (0-1000 chars) in service layer
- [X] T008 [P] Create custom exceptions for invalid task IDs and invalid task data in src/todo_app/services/todo_service.py

---

## Phase 3: User Story 1 - Add and View Tasks (P1)

**Goal**: Enable users to add new tasks and view all tasks (foundational functionality)

**Independent Test Criteria**:
- User can add a task with title and optional description
- User can view all tasks with ID, title, and completion status
- Tasks are stored in memory and listed in creation order

**Acceptance Scenarios**:
1. **Given** the application is running, **When** user selects "Add Task" and enters a valid title, **Then** a new task is created with a unique ID and shown as incomplete
2. **Given** tasks exist in the system, **When** user selects "View Tasks", **Then** all tasks are displayed with their ID, title, and completion status

- [X] T009 [US1] Create CLI interface in src/todo_app/cli/todo_cli.py with basic menu display functionality
- [X] T010 [US1] Implement Add Task functionality in CLI with user input validation and error handling
- [X] T011 [US1] Implement View Tasks functionality in CLI to display all tasks with ID, title, and completion status
- [X] T012 [US1] Create main application loop in main.py to handle menu selection and call appropriate CLI methods

---

## Phase 4: User Story 2 - Update and Delete Tasks (P2)

**Goal**: Enable users to modify or remove existing tasks from their list

**Independent Test Criteria**:
- User can update an existing task's title or description
- User can delete an existing task
- Changes persist in memory

**Acceptance Scenarios**:
1. **Given** a task exists in the system, **When** user selects "Update Task" and provides valid changes, **Then** the task is modified accordingly
2. **Given** a task exists in the system, **When** user selects "Delete Task", **Then** the task is removed from the list

- [X] T013 [US2] Implement Update Task functionality in CLI with user input for task ID, title, and description
- [X] T014 [US2] Add validation to update task functionality to ensure title meets requirements when provided
- [X] T015 [US2] Implement Delete Task functionality in CLI with user input for task ID
- [X] T016 [US2] Add error handling for invalid task IDs in update and delete operations

---

## Phase 5: User Story 3 - Mark Tasks Complete/Incomplete (P3)

**Goal**: Enable users to track which tasks they have completed

**Independent Test Criteria**:
- User can toggle task completion status
- Status updates correctly in memory

**Acceptance Scenarios**:
1. **Given** a task exists in the system, **When** user selects "Mark Task Complete/Incomplete", **Then** the task's completion status toggles appropriately

- [X] T017 [US3] Implement Mark Task Complete/Incomplete functionality in CLI with user input for task ID
- [X] T018 [US3] Add toggle logic to switch task completion status from complete to incomplete or vice versa

---

## Phase 6: Error Handling and Validation

**Goal**: Ensure robust error handling and input validation throughout the application

- [X] T019 Add validation for invalid menu choices in main application loop
- [X] T020 Implement friendly error messages for all error conditions
- [X] T021 Add validation to prevent application crashes from bad user input
- [X] T022 Ensure application continues running after displaying error messages

---

## Phase 7: Polish & Cross-Cutting Concerns

**Goal**: Finalize the application with proper user experience and edge case handling

- [X] T023 Add friendly message when viewing tasks with no tasks exist
- [X] T024 Implement proper exit functionality when user selects "Exit Application"
- [X] T025 Add input validation for very long titles or descriptions that exceed requirements
- [X] T026 Ensure menu repeats after each action as specified in requirements
- [X] T027 Test complete application flow to ensure all menu options work correctly
- [X] T028 Verify deterministic behavior with same inputs producing same outputs