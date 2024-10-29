class Task:
    def __init__(self, title, description, priority="Média"):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
    
    def mark_as_completed(self):
        self.completed = True
    
    def __str__(self):
        status = "Concluido" if self.completed else "Pendente"
        return f"\nTask: {self.title}\nPrioridade: {self.priority}\nStatus: {status}\nDescrição: {self.description}"

    