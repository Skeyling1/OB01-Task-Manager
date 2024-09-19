#Менеджер задач
# Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.


class Task:
    def __init__(self):
        self.task = []

    #Добавление новой задачи
    def add_task(self, description, deadline, status):
        self.description = description
        self.deadline = deadline
        self.status = status
        self.task.append((description, deadline, status))

    #меняет статус
    def change_status(self, task_number):
        selected_task = self.task.pop(task_number)
        print(f'\nзадача \'{selected_task[0]}\' отмечена как выполненная')
        renewed_task_description = selected_task[0]
        renewed_task_date = selected_task[1]
        renewed_task = (renewed_task_description, renewed_task_date, "выполненно")
        self.task.append(renewed_task)


    #показывает не выполненые
    def list_task(self):
        print("\nневыполненны задачи:")
        for i in self.task:
            if i[2] == 'не выполнено':
                print(i)

my_tasks = Task()
my_tasks.add_task("участие в семинаре", "12.10.24", "не выполнено")
my_tasks.add_task("подготовка к собеседованию", "13.12.24", "не выполнено")
my_tasks.add_task("собеседование", "14.12.24", "не выполнено")
my_tasks.list_task()
my_tasks.change_status(1)
my_tasks.list_task()


