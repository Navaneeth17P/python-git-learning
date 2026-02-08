"""
Todo List Manager
Feature: Add, view, and complete tasks
"""

import json
from datetime import datetime

class TodoManager:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        """Load todos from file"""
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def save_todos(self):
        """Save todos to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add_todo(self, task):
        """Add a new todo"""
        todo = {
            'id': len(self.todos) + 1,
            'task': task,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"✓ Added: {task}")
    
    def view_todos(self):
        """Display all todos"""
        if not self.todos:
            print("No todos yet! Add some tasks.")
            return
        
        print("\n" + "=" * 60)
        print("YOUR TODO LIST")
        print("=" * 60)
        
        for todo in self.todos:
            status = "✓" if todo['completed'] else "○"
            print(f"{status} [{todo['id']}] {todo['task']}")
            print(f"   Created: {todo['created_at']}")
        print("=" * 60)
    
    def complete_todo(self, todo_id):
        """Mark todo as completed"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = True
                self.save_todos()
                print(f"✓ Completed: {todo['task']}")
                return
        print(f"Todo with ID {todo_id} not found")

def main():
    manager = TodoManager()
    
    while True:
        print("\n" + "=" * 40)
        print("TODO LIST MANAGER")
        print("=" * 40)
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Complete Todo")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ")
        
        if choice == '1':
            task = input("Enter task: ")
            manager.add_todo(task)
        elif choice == '2':
            manager.view_todos()
        elif choice == '3':
            manager.view_todos()
            try:
                todo_id = int(input("Enter todo ID to complete: "))
                manager.complete_todo(todo_id)
            except ValueError:
                print("Please enter a valid number")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()