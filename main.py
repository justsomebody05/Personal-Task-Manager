class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.completed = False
        self.priority = priority
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, title, description, priority):
        task = Task(title, description, priority)
        self.tasks.append(task)
        self.save_to_file()
    def list_tasks(self):
        sorted_tasks = sorted(self.tasks, key=lambda t: t.priority, , reverse=True)
        for i, task in enumerate(sorted_tasks, 1):
            status = "✓" if task.completed else "✗"
            print(f"{i}. [{status}] {task.title} (Приоритет: {task.priority})")
    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            print(f"Задача '{removed.title}' удалена.")
            self.save_to_file()
        else:
            print("Ошибка: номер задачи вне допустимого диапазона.")
            
    def completed_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.completed = True
            print(f'Задача отмечена')
        else:
            print(f'Введите корректное число!')
    def search_for_task(self, query):
        found_something = []
        for task in self.tasks:
            if query.lower() in task.title.lower() or query.lower() in task.description.lower():
                found_something.append(task)
        return found_something
    def filter_by_priority(self, level):
        filter = []
        for task in self.tasks:
            if level == task.priority:
                filter.append(task)
        return filter

    def save_to_file(self):
        with open('taskmanager.txt', 'w') as file:
            for task in self.tasks:
                file.write(f"{task.title}|{task.description}|{task.completed}|{task.priority}\n")
    def load_tasks(self):
        try:
            with open('taskmanager.txt', 'r') as f:
                for line in f:
                    parts = line.strip().split('|')
                    if len(parts) == 4:
                        title, desc, completed, priority = parts
                        task = Task(title, desc, int(priority))
                        task.completed = (completed == "True")
                        self.tasks.append(task)
        except FileNotFoundError:
            pass
            
def main():
    manager = TaskManager()
    manager.load_tasks()
    
    while True: 
        print("\n1. Добавить задачу")
        print("2. Показать задачи") 
        print("3. Удалить задачу")
        print("4. Отметить как выполненную")
        print("5. Поиск")
        print("6. Филтрация по приоритету")
        print("7. Выйти")
        
        choice = input("Выберите: ")
        
        if choice == "1":
            title = input("Название: ")
            desc = input("Описание: ")
            priora = int(input("Введите приоритет задачи: "))
            manager.add_task(title, desc, priora)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            manager.list_tasks()
            try:
                task_number = int(input("Введите номер вашей задачи: "))
                manager.delete_task(task_number)
            except ValueError:
                print("Ошибка: введите целое число.")
        elif choice == "4":
            manager.list_tasks()
            try:
                task_number = int(input("Введите номер вашей задачи: "))
                manager.completed_task(task_number)
                manager.save_to_file()
                manager.list_tasks()
            except ValueError:
                print("Ошибка: введите корректный номер задачи.")
        elif choice == "5":
            search = input("Введите слово или фразу: ")
            s = manager.search_for_task(search)
            for task in s:
                print(f"- {task.title}: {task.description}")
        elif choice == "6":
            pr = int(input("Введите приоритет: "))
            s = manager.filter_by_priority(pr)
            for task in s:
                print(f"- {task.title}: {task.description}")
        elif choice == "7":
            manager.save_to_file()
            print("Задачи сохранены. Пока!")
            break
        
if __name__ == "__main__":
    main()