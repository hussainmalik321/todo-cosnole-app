"""
Todo Service

This module provides the business logic for todo operations.
"""
from typing import List, Optional, Dict
from src.todo_app.models.task import Task
from src.todo_app.storage.in_memory_storage import InMemoryStorage


class TaskNotFoundError(Exception):
    """Exception raised when a task is not found."""
    pass


class InvalidTaskDataError(Exception):
    """Exception raised when task data is invalid."""
    pass


class TodoService:
    """Service layer for todo operations."""

    def __init__(self, storage: InMemoryStorage = None):
        """
        Initialize the TodoService.

        Args:
            storage: Storage instance (if None, creates a new one)
        """
        self.storage = storage or InMemoryStorage()

    def add_task(self, title: str, description: str = None) -> int:
        """
        Add a new task to the collection.

        Args:
            title: Task title (1-200 characters)
            description: Task description (0-1000 characters, optional)

        Returns:
            ID of the newly created task

        Raises:
            InvalidTaskDataError: If title is invalid
        """
        try:
            # Create a temporary task to validate the data
            temp_task = Task(task_id=0, title=title, description=description)
            # If validation passes, create the actual task with proper ID
            new_task = Task(task_id=self.storage.get_next_id(), title=temp_task.title,
                           description=temp_task.description, completed=False)
            return self.storage.add_task(new_task)
        except ValueError as e:
            raise InvalidTaskDataError(str(e))

    def list_tasks(self) -> List[Dict]:
        """
        Retrieve all tasks.

        Returns:
            List of task dictionaries containing id, title, description, and completed status
        """
        tasks = self.storage.list_all_tasks()
        return [task.to_dict() for task in tasks]

    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        """
        Update an existing task.

        Args:
            task_id: ID of the task to update
            title: New title if provided
            description: New description if provided

        Returns:
            True if update successful, False if task not found

        Raises:
            InvalidTaskDataError: If new title is invalid
        """
        task = self.storage.get_task(task_id)
        if task is None:
            return False

        try:
            # Validate new data if provided
            if title is not None:
                # Create a temporary task to validate the title
                temp_task = Task(task_id=0, title=title, description=task.description)
                title = temp_task.title

            if description is not None:
                # Create a temporary task to validate the description
                temp_task = Task(task_id=0, title=task.title, description=description)
                description = temp_task.description

            # Update the task
            task.update(title=title, description=description)
            return True
        except ValueError as e:
            raise InvalidTaskDataError(str(e))

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from the collection.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if deletion successful, False if task not found
        """
        return self.storage.delete_task(task_id)

    def toggle_task_completion(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.

        Args:
            task_id: ID of the task to toggle

        Returns:
            True if toggle successful, False if task not found
        """
        task = self.storage.get_task(task_id)
        if task is None:
            return False

        # Toggle the completion status
        task.completed = not task.completed
        return True