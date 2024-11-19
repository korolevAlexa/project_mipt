import tkinter as tk
from tkinter import ttk, messagebox
from user import MoodTracker
from datetime import datetime

class HistoryWindow:
    def __init__(self, root, mood_tracker):
        self.root = root
        self.mood_tracker = mood_tracker
        self.window = tk.Toplevel(self.root)
        self.window.title("История записей")
        
        # Устанавливаем размер окна
        self.window.geometry("800x600")  # Размер окна можно изменять по желанию

        # Создание стиля для Treeview
        self.style = ttk.Style()
        self.style.configure("Treeview", rowheight=40)  # Устанавливаем большую высоту строки
        self.style.configure("Treeview.Heading", font=("Arial", 14, "bold"))  # Увеличиваем размер шрифта заголовков
        self.style.configure("Treeview", font=("Arial", 12), highlightthickness=0, bd=0)  # Устанавливаем шрифт для содержимого таблицы
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Визуальные элементы Treeview

        self.create_widgets()

    def create_widgets(self):
        # Создаем таблицу для отображения истории записей
        self.tree = ttk.Treeview(self.window, columns=("Timestamp", "Mood", "Comment", "Actions"), show="headings", height=15, style="Treeview")
        self.tree.heading("Timestamp", text="Время")
        self.tree.heading("Mood", text="Настроение")
        self.tree.heading("Comment", text="Комментарий")
        self.tree.heading("Actions", text="Действия")

        self.tree.column("Actions", width=100, anchor="center")

        # Загружаем записи и добавляем в таблицу
        self.load_entries()

        self.tree.pack(pady=20, padx=20, expand=True, fill="both")

        # Кнопка "Вернуться в меню"
        back_button = tk.Button(self.window, text="Вернуться в меню", font=("Arial", 16), command=self.window.destroy)
        back_button.pack(pady=10)

        # Привязываем обработчик кликов для всей таблицы, чтобы определить клик по троеточию
        self.tree.bind("<Button-1>", self.on_delete_button_click)

    def load_entries(self):
        """Загружает записи в таблицу."""
        # Очищаем таблицу перед загрузкой новых записей
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Загружаем записи из mood_tracker и добавляем их в таблицу
        for idx, record in enumerate(self.mood_tracker.entries):  # Индекс записи
            timestamp = record["timestamp"]
            mood = record["mood"]
            comment = record["comment"]
            # Вставляем запись в таблицу с уникальным индексом (idx) для удаления
            self.tree.insert("", "end", values=(timestamp, mood, comment, "…"), tags=(idx,))

    def on_delete_button_click(self, event):
        """Обрабатывает клик по кнопке '…' и вызывает окно для подтверждения удаления."""
        # Определяем, по какой ячейке был клик
        column = self.tree.identify_column(event.x)
        row_id = self.tree.identify_row(event.y)

        # Если клик был по колонке с действиями (т.е. "…")
        if column == "#4" and row_id:
            item_id = self.tree.item(row_id)["values"][0]  # Получаем timestamp записи
            self.confirm_delete(item_id)

    def confirm_delete(self, item_id):
        """Открывает окно с подтверждением удаления записи."""
        # Получаем данные записи для отображения в окне подтверждения
        for record in self.mood_tracker.entries:
            if record["timestamp"] == item_id:
                timestamp = record["timestamp"]
                mood = record["mood"]
                comment = record["comment"]
                break

        # Спрашиваем у пользователя подтверждение
        confirm = messagebox.askyesno("Удалить запись?", f"Вы уверены, что хотите удалить запись от {timestamp}?\nНастроение: {mood}\nКомментарий: {comment}")

        if confirm:
            # Удаляем запись из базы данных
            self.mood_tracker.delete_entry_by_id(item_id)
            # Перезагружаем записи в таблице
            self.load_entries()
