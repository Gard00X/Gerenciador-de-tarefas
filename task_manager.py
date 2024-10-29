from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, priority="Média"):
        task = Task(title, description, priority)
        self.tasks.append(task)

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
        else:
            print("Tarefa não encontrada.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Tarefa não encontrada.")
