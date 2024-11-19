import tkinter as tk
from user import MoodTracker
from new_entry import NewEntryWindow
from calendar_view import CalendarWindow
from history_view import HistoryWindow

class MoodTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mood Tracker")

        # Открытие окна на весь экран
        self.root.attributes('-fullscreen', True)  # Включение полноэкранного режима

        # Инициализация MoodTracker
        self.mood_tracker = MoodTracker()

        # Переменная для хранения текущего активного окна
        self.active_window = None

        # Загружаем GIF изображение
        gif_path = "/Users/alexa/Downloads/улыбнись-подарок.gif"
        self.gif_image = tk.PhotoImage(file=gif_path)
        
        # Размещаем GIF изображение на главной странице
        self.gif_label = tk.Label(self.root, image=self.gif_image)
        self.gif_label.pack(pady=20)

        # Кнопка "Календарь"
        self.calendar_button = tk.Button(self.root, text="Календарь", font=("Arial", 20), width=20, height=2, command=self.open_calendar)
        self.calendar_button.pack(pady=20)

        # Кнопка "История записей"
        self.history_button = tk.Button(self.root, text="История записей", font=("Arial", 20), width=20, height=2, command=self.open_history)
        self.history_button.pack(pady=20)

        # Кнопка "Сделать новую запись"
        self.new_entry_button = tk.Button(self.root, text="Сделать новую запись", font=("Arial", 20), width=20, height=2, command=self.make_new_entry)
        self.new_entry_button.pack(pady=20)

    def open_calendar(self):
        """Открывает окно с календарем."""
        self.close_active_window()
        self.active_window = CalendarWindow(self.root, self.mood_tracker)

    def open_history(self):
        """Открывает окно с историей записей."""
        self.close_active_window()
        self.active_window = HistoryWindow(self.root, self.mood_tracker)

    def make_new_entry(self):
        """Открывает окно для создания новой записи."""
        self.close_active_window()
        self.active_window = NewEntryWindow(self.root, self.mood_tracker)

    def close_active_window(self):
        """Закрывает текущее активное окно, если оно открыто."""
        if self.active_window and hasattr(self.active_window, "window"):
            self.active_window.window.destroy()
        self.active_window = None

# Основное окно приложения
root = tk.Tk()
app = MoodTrackerApp(root)
root.mainloop()
