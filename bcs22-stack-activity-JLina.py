class Task:
    def __init__(self, title, description):
        self.title, self.description, self.completed = title, description, False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        self.tasks.append(Task(title, description))
        print(f'Task "{title}" added successfully!')

    def mark_completed(self, task_index):
        task = self.tasks[task_index] if 0 <= task_index < len(self.tasks) else None
        if task:
            task.completed = True
            print(f'Task "{task.title}" marked as completed!')
        else:
            print('Invalid task index.')

    def display_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            print('Task List:')
            for i, task in enumerate(self.tasks, 1):
                print(f'{i}. {task.title} - {task.description} - {"Completed" if task.completed else "Not Completed"}')

    def run_task_manager(self):
        while True:
            print('\nTask Manager Menu:\n1. Add Task\n2. Mark Task as Completed\n3. Display Tasks\n4. Exit')
            choice = input('Enter your choice (1/2/3/4): ')

            if choice == '1':
                self.add_task(input('Enter task title: '), input('Enter task description: '))
            elif choice == '2':
                self.mark_completed(int(input('Enter the task index to mark as completed: ')) - 1)
            elif choice == '3':
                self.display_tasks()
            elif choice == '4':
                print('Exiting Task Manager. Goodbye!'); break
            else:
                print('Invalid choice. Please enter a valid option.')

if __name__ == "__main__":
    TaskManager().run_task_manager()

