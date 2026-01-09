"""
In-Memory Storage

This module provides in-memory storage for tasks with basic CRUD operations.
"""
from typing import List, Optional, Dict
from src.todo_app.models.task import Task


class InMemoryStorage:
    """In-memory storage for tasks."""

    def __init__(self):
        """Initialize the in-memory storage."""
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1

    def add_task(self, task: Task) -> int:
        """
        Add a new task to storage.

        Args:
            task: Task to add

        Returns:
            ID of the added task
        """
        task_id = self._next_id
        task.id = task_id
        self._tasks[task_id] = task
        self._next_id += 1
        return task_id

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by ID.

        Args:
            task_id: ID of the task to retrieve

        Returns:
            Task if found, None otherwise
        """
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, task_data: dict) -> bool:
        """
        Update an existing task.

        Args:
            task_id: ID of the task to update
            task_data: Dictionary with new task data

        Returns:
            True if update successful, False if task not found
        """
        if task_id not in self._tasks:
            return False

        task = self._tasks[task_id]

        # Update fields if provided in task_data
        if 'title' in task_data:
            task.title = task_data['title']
        if 'description' in task_data:
            task.description = task_data['description']
        if 'completed' in task_data:
            task.completed = task_data['completed']

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from storage.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if deletion successful, False if task not found
        """
        if task_id not in self._tasks:
            return False

        del self._tasks[task_id]
        return True

    def list_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks in creation order.

        Returns:
            List of all tasks in creation order
        """
        # Sort tasks by ID to maintain creation order
        return [self._tasks[tid] for tid in sorted(self._tasks.keys())]

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new task.

        Returns:
            Next available task ID
        """
        return self._next_id