import tkinter as tk 
import json
import os

class UserRegistration:
    def __init__(self):
        # Путь к файлу для хранения данных
        self.user_data_file = "user_data.json"
        self.user_name = self.load_user_name()

    def load_user_name(self):
        """Загружает имя пользователя из файла."""
        if not os.path.exists(self.user_data_file):
            # Если файл не существует, возвращаем пустую строку
            return ""
        
        with open(self.user_data_file, 'r') as file:
            try:
                data = json.load(file)
                return data.get('user_name', "")  # Возвращаем имя пользователя, если оно есть
            except json.JSONDecodeError:
                print("Ошибка в формате JSON. Файл пуст или поврежден.")
                return ""  # Если JSON поврежден, возвращаем пустое имя

    def save_user_name(self, user_name):
        """Сохраняет имя пользователя в файл."""
        data = {'user_name': user_name}
        with open(self.user_data_file, 'w') as file:
            json.dump(data, file)

    def show_registration_window(self, root):
        """Отображает окно регистрации."""
        registration_window = tk.Toplevel(root)
        registration_window.title("Регистрация")

        tk.Label(registration_window, text="Введите имя пользователя:").pack(pady=10)

        user_name_entry = tk.Entry(registration_window, font=("Arial", 14))
        user_name_entry.pack(pady=10)

        def on_register():
            user_name = user_name_entry.get()
            if user_name.strip():
                self.save_user_name(user_name)
                registration_window.destroy()  # Закрываем окно регистрации
            else:
                tk.Label(registration_window, text="Имя не может быть пустым!", fg="red").pack(pady=10)

        register_button = tk.Button(registration_window, text="Зарегистрироваться", command=on_register)
        register_button.pack(pady=20)