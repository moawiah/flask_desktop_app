class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_id = 1

    def add_task(self, name):
        task = {'id': self.task_id, 'name': name}
        self.tasks.append(task)
        self.task_id += 1

    def get_tasks(self):
        return self.tasks

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
