"""
Todo CLI Interface

This module provides the command-line interface for the todo application.
"""
from typing import Optional
from src.todo_app.services.todo_service import TodoService, InvalidTaskDataError
from src.todo_app.storage.in_memory_storage import InMemoryStorage


class TodoCLI:
    """Command-line interface for the todo application."""

    def __init__(self):
        """Initialize the CLI with a todo service."""
        storage = InMemoryStorage()
        self.service = TodoService(storage)

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*40)
        print("TODO APPLICATION")
        print("="*40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Exit Application")
        print("="*40)

    def get_user_choice(self) -> str:
        """
        Get user's menu choice.

        Returns:
            User's choice as a string
        """
        try:
            choice = input("Select an option (1-6): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\nApplication interrupted. Exiting...")
            return "6"  # Treat as exit choice

    def add_task(self):
        """Handle adding a new task."""
        print("\n--- Add New Task ---")
        try:
            title = input("Enter task title: ").strip()
            if not title:
                print("Error: Task title cannot be empty.")
                return

            description_input = input("Enter task description (optional, press Enter to skip): ").strip()
            description = description_input if description_input else None

            task_id = self.service.add_task(title, description)
            print(f"Task added successfully with ID: {task_id}")

        except InvalidTaskDataError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_tasks(self):
        """Handle viewing all tasks."""
        print("\n--- All Tasks ---")
        tasks = self.service.list_tasks()

        if not tasks:
            print("No tasks found.")
            return

        for task in tasks:
            status = "✓ Complete" if task['completed'] else "○ Incomplete"
            print(f"ID: {task['id']}, Title: {task['title']}, Status: {status}")
            if task['description']:
                print(f"     Description: {task['description']}")
            print()

    def update_task(self):
        """Handle updating an existing task."""
        print("\n--- Update Task ---")
        try:
            task_id_str = input("Enter task ID to update: ").strip()
            if not task_id_str:
                print("Error: Task ID cannot be empty.")
                return

            try:
                task_id = int(task_id_str)
            except ValueError:
                print("Error: Task ID must be a number.")
                return

            # Check if task exists
            tasks = self.service.list_tasks()
            task_exists = any(task['id'] == task_id for task in tasks)
            if not task_exists:
                print(f"Error: Task with ID {task_id} not found.")
                return

            title_input = input("Enter new title (or press Enter to keep current): ").strip()
            description_input = input("Enter new description (or press Enter to keep current): ").strip()

            # Prepare update parameters
            update_params = {}
            if title_input:
                update_params['title'] = title_input
            if description_input:  # Allow empty string to clear description
                update_params['description'] = description_input

            if not update_params:
                print("No changes provided. Task not updated.")
                return

            success = self.service.update_task(task_id, **update_params)
            if success:
                print(f"Task {task_id} updated successfully.")
            else:
                print(f"Error: Failed to update task {task_id}.")

        except InvalidTaskDataError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def delete_task(self):
        """Handle deleting a task."""
        print("\n--- Delete Task ---")
        try:
            task_id_str = input("Enter task ID to delete: ").strip()
            if not task_id_str:
                print("Error: Task ID cannot be empty.")
                return

            try:
                task_id = int(task_id_str)
            except ValueError:
                print("Error: Task ID must be a number.")
                return

            # Check if task exists before deletion
            tasks = self.service.list_tasks()
            task_exists = any(task['id'] == task_id for task in tasks)
            if not task_exists:
                print(f"Error: Task with ID {task_id} not found.")
                return

            success = self.service.delete_task(task_id)
            if success:
                print(f"Task {task_id} deleted successfully.")
            else:
                print(f"Error: Failed to delete task {task_id}.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def toggle_task_completion(self):
        """Handle toggling task completion status."""
        print("\n--- Toggle Task Completion ---")
        try:
            task_id_str = input("Enter task ID to toggle: ").strip()
            if not task_id_str:
                print("Error: Task ID cannot be empty.")
                return

            try:
                task_id = int(task_id_str)
            except ValueError:
                print("Error: Task ID must be a number.")
                return

            # Check if task exists before toggling
            tasks = self.service.list_tasks()
            task_exists = any(task['id'] == task_id for task in tasks)
            if not task_exists:
                print(f"Error: Task with ID {task_id} not found.")
                return

            success = self.service.toggle_task_completion(task_id)
            if success:
                # Get updated task to show new status
                updated_tasks = self.service.list_tasks()
                updated_task = next((t for t in updated_tasks if t['id'] == task_id), None)
                if updated_task:
                    status = "✓ Complete" if updated_task['completed'] else "○ Incomplete"
                    print(f"Task {task_id} status updated to: {status}")
            else:
                print(f"Error: Failed to toggle task {task_id} status.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def run(self):
        """Run the main application loop."""
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.toggle_task_completion()
            elif choice == "6":
                print("Thank you for using the Todo Application. Goodbye!")
                break
            else:
                print(f"Invalid choice: '{choice}'. Please select a number between 1 and 6.")