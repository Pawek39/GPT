import tkinter as tk
from tkinter import ttk


def load_steps(file_path):
    steps = []
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    i = 0
    while i < len(lines):
        if lines[i].startswith('#'):
            description = lines[i][1:].strip()
            command = ''
            if i + 1 < len(lines) and not lines[i + 1].startswith('#'):
                command = lines[i + 1]
                i += 1
            steps.append((description, command))
        i += 1
    return steps


class StepViewer(tk.Tk):
    def __init__(self, steps):
        super().__init__()
        self.steps = steps
        self.index = 0
        self.title("Instrukcje")
        self.geometry('500x200')

        self.desc_label = ttk.Label(self, text='', wraplength=480)
        self.desc_label.pack(pady=10)

        self.command_text = tk.Text(self, height=2, width=60)
        self.command_text.pack()

        frame = ttk.Frame(self)
        frame.pack(pady=10)
        self.prev_btn = ttk.Button(frame, text='Poprzedni', command=self.prev_step)
        self.prev_btn.grid(row=0, column=0, padx=5)
        self.next_btn = ttk.Button(frame, text='Nast\u0119pny', command=self.next_step)
        self.next_btn.grid(row=0, column=1, padx=5)
        self.show_step()

    def show_step(self):
        step = self.steps[self.index]
        self.desc_label.config(text=step[0])
        self.command_text.delete('1.0', tk.END)
        self.command_text.insert(tk.END, step[1])
        self.update_buttons()

    def next_step(self):
        if self.index < len(self.steps) - 1:
            self.index += 1
            self.show_step()

    def prev_step(self):
        if self.index > 0:
            self.index -= 1
            self.show_step()

    def update_buttons(self):
        self.prev_btn['state'] = tk.NORMAL if self.index > 0 else tk.DISABLED
        self.next_btn['state'] = tk.NORMAL if self.index < len(self.steps) - 1 else tk.DISABLED


if __name__ == '__main__':
    steps = load_steps('TEST')
    viewer = StepViewer(steps)
    viewer.mainloop()
