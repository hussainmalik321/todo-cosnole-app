#!/usr/bin/env python3
"""
Todo Application Entry Point

This is the main entry point for the Todo console application.
"""
from src.todo_app.cli.todo_cli import TodoCLI


def main():
    """Main entry point for the application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()