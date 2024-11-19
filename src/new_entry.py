import tkinter as tk
from tkinter import messagebox
from user import MoodTracker

class NewEntryWindow:
    def __init__(self, root, mood_tracker):
        self.root = root
        self.mood_tracker = mood_tracker
        self.window = tk.Toplevel(self.root)
        self.window.title("Сделать новую запись")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Метка и ползунок для выбора настроения
        mood_label = tk.Label(self.window, text="Выберите настроение (-2 до 2):", font=("Arial", 14))
        mood_label.pack(pady=20)

        self.mood_slider = tk.Scale(self.window, from_=-2, to=2, orient="horizontal", font=("Arial", 12), tickinterval=1)
        self.mood_slider.pack(pady=10)

        # Поле для ввода комментария (многострочный текст)
        comment_label = tk.Label(self.window, text="Комментарий:", font=("Arial", 14))
        comment_label.pack(pady=20)

        self.comment_text = tk.Text(self.window, font=("Arial", 14), wrap="word", width=40, height=5)
        self.comment_text.pack(pady=10)

        # Кнопка для сохранения записи
        save_button = tk.Button(self.window, text="Сохранить запись", font=("Arial", 16), command=self.save_entry)
        save_button.pack(pady=20)

        # Кнопка для возврата в меню
        back_button = tk.Button(self.window, text="Вернуться в меню", font=("Arial", 16), command=self.window.destroy)
        back_button.pack(pady=10)
    
    def save_entry(self):
        """Сохраняет новую запись и закрывает окно."""
        mood = self.mood_slider.get()
        comment = self.comment_text.get("1.0", "end").strip()  # Получаем весь текст из Text

        if not comment:
            messagebox.showerror("Ошибка", "Пожалуйста, введите комментарий!")
            return

        # Сохраняем запись через метод из MoodTracker
        self.mood_tracker.add_entry(mood, comment)

        # Закрываем окно и возвращаемся в главное меню
        self.window.destroy()

        # Сообщение о том, что запись сохранена
        messagebox.showinfo("Успех", "Запись успешно сохранена!")
