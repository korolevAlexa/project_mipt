import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox, ttk
from .user import MoodTracker

class CalendarWindow:
    def __init__(self, root, mood_tracker):
        self.root = root
        self.mood_tracker = mood_tracker
        self.window = tk.Toplevel(self.root)
        self.window.title("Календарь")

        # Устанавливаем размеры окна календаря
        self.window.geometry("800x600")
        
        self.create_widgets()

    def create_widgets(self):
        # Инициализация календаря с более крупным шрифтом и увеличенными размерами
        calendar = Calendar(self.window, selectmode='day', date_pattern='yyyy-mm-dd', font=("Arial", 16))
        calendar.pack(pady=20)

        # Кнопка "Вернуться в меню"
        back_button = tk.Button(self.window, text="Вернуться в меню", font=("Arial", 16), command=self.window.destroy)
        back_button.pack(pady=10)

        # Обработчик нажатия на дату
        calendar.bind("<<CalendarSelected>>", self.show_entries_for_selected_date)

    def show_entries_for_selected_date(self, event):
        """Показывает записи за выбранную дату."""
        selected_date = event.widget.get_date()  # Получаем выбранную дату в формате 'yyyy-mm-dd'
        
        # Проверяем записи, соответствующие выбранной дате
        entries = self.mood_tracker.get_entries_by_date(selected_date)

        if entries:
            # Создаём новое окно для отображения записей
            entries_window = tk.Toplevel(self.root)
            entries_window.title(f"Записи за {selected_date}")

            # Таблица для отображения записей
            tree = ttk.Treeview(entries_window, columns=("Timestamp", "Mood", "Comment"), show="headings", height=10)
            tree.heading("Timestamp", text="Время")
            tree.heading("Mood", text="Настроение")
            tree.heading("Comment", text="Комментарий")

            # Заполнение таблицы
            for entry in entries:
                tree.insert("", tk.END, values=(entry["timestamp"], entry["mood"], entry["comment"]))

            tree.pack(pady=20)

            # Кнопка "Вернуться в меню"
            back_button = tk.Button(entries_window, text="Вернуться в меню", font=("Arial", 16), command=entries_window.destroy)
            back_button.pack(pady=10)
        else:
            messagebox.showinfo("Информация", f"Записей на {selected_date} нет.")
