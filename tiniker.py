import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")


        self.tasks = [
            {"text": "Academia", "done": False},
            {"text": "Estudar", "done": False},
            {"text": "Passear com o cachorro", "done": False},
            {"text": "Estudar de novo", "done": False}
        ]
        self.xp = 0
        self.level = 1
        self.task_vars = []
        self.task_checks = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_list_frame = tk.Frame(self.frame)
        self.task_list_frame.pack()

        self.add_task_frame = tk.Frame(self.frame)
        self.add_task_frame.pack(pady=10)

        self.add_task_entry = tk.Entry(self.add_task_frame, width=50)
        self.add_task_entry.pack(side=tk.LEFT, padx=5)
        self.add_task_button = tk.Button(self.add_task_frame, text="Adicionar Tarefa", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT)

        self.xp_label = tk.Label(self.frame, text=f"XP: {self.xp} | Nível: {self.level}")
        self.xp_label.pack(pady=5)

        self.render_tasks()

    def render_tasks(self):
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()

        self.task_vars.clear()
        self.task_checks.clear()

        for index, task in enumerate(self.tasks):
            var = tk.BooleanVar(value=task["done"])
            check = tk.Checkbutton(self.task_list_frame, text=task["text"], variable=var, command=lambda i=index: self.toggle_task(i))
            if task["done"]:
                check.config(fg="gray")
            check.pack(anchor=tk.W)
            self.task_vars.append(var)
            self.task_checks.append(check)

    def toggle_task(self, index):
        task = self.tasks[index]
        task["done"] = not task["done"]
        if task["done"]:
            self.xp += 10
            self.task_checks[index].config(fg="gray")
        else:
            self.xp -= 10
            self.task_checks[index].config(fg="black")
        self.check_level_up()
        self.update_xp_label()

    def check_level_up(self):
        if self.xp >= 40:
            self.xp = 0
            self.level += 1
            messagebox.showinfo("Parabéns!", f"Você alcançou o nível {self.level}!")
        self.update_xp_label()

    def update_xp_label(self):
        self.xp_label.config(text=f"XP: {self.xp} | Nível: {self.level}")

    def add_task(self):
        task_text = self.add_task_entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "done": False})
            self.render_tasks()
            self.add_task_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()