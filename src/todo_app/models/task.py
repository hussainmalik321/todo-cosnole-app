"""
Task Model

This module defines the Task data model with validation.
"""
from typing import Optional


class Task:
    """Represents a single todo task."""

    def __init__(self, task_id: int, title: str, description: Optional[str] = None, completed: bool = False):
        """
        Initialize a Task instance.

        Args:
            task_id: Unique identifier for the task
            title: Task title (1-200 characters)
            description: Optional task description (0-1000 characters)
            completed: Task completion status (default: False)
        """
        self.id = task_id
        self.title = self._validate_title(title)
        self.description = self._validate_description(description)
        self.completed = completed

    def _validate_title(self, title: str) -> str:
        """
        Validate the task title.

        Args:
            title: Task title to validate

        Returns:
            Validated title

        Raises:
            ValueError: If title is invalid
        """
        if not title or not isinstance(title, str):
            raise ValueError("Task title must be a non-empty string")

        title = title.strip()
        if not title:
            raise ValueError("Task title cannot be empty or just whitespace")

        if len(title) > 200:
            raise ValueError(f"Task title exceeds maximum length of 200 characters: {len(title)} provided")

        return title

    def _validate_description(self, description: Optional[str]) -> Optional[str]:
        """
        Validate the task description.

        Args:
            description: Task description to validate (can be None)

        Returns:
            Validated description or None
        """
        if description is None:
            return None

        if not isinstance(description, str):
            raise ValueError("Task description must be a string or None")

        if len(description) > 1000:
            raise ValueError(f"Task description exceeds maximum length of 1000 characters: {len(description)} provided")

        return description

    def update(self, title: Optional[str] = None, description: Optional[str] = None) -> None:
        """
        Update task fields with validation.

        Args:
            title: New title (optional)
            description: New description (optional)
        """
        if title is not None:
            self.title = self._validate_title(title)

        if description is not None:
            self.description = self._validate_description(description)

    def to_dict(self) -> dict:
        """
        Convert the task to a dictionary representation.

        Returns:
            Dictionary representation of the task
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

    def __repr__(self) -> str:
        """String representation of the task."""
        status = "✓" if self.completed else "○"
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"

    def __eq__(self, other) -> bool:
        """Check equality with another task."""
        if not isinstance(other, Task):
            return False
        return self.id == other.id