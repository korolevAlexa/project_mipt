import json
import os
from datetime import datetime

class MoodTracker:
    def __init__(self, file_path="mood_data.json"):
        self.file_path = file_path
        self.entries = self.load_entries_from_file()

    def load_entries_from_file(self):
        """Загружает записи из JSON-файла."""
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Если файл не существует или поврежден, возвращаем пустой список

    def save_entries_to_file(self):
        """Сохраняет записи в JSON-файл."""
        with open(self.file_path, "w") as file:
            json.dump(self.entries, file, ensure_ascii=False, indent=4)

    def add_entry(self, mood, comment, timestamp=None):
        """Добавляет новую запись в трекер."""
        if not timestamp:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Включаем секунды
        entry = {
            'mood': mood,
            'comment': comment,
            'timestamp': timestamp
        }
        self.entries.append(entry)
        self.save_entries_to_file()

    def get_entries_by_date(self, date):
        """Возвращает записи за указанную дату."""
        return [entry for entry in self.entries if entry['timestamp'].startswith(date)]

    def get_all_entries(self):
        """Возвращает все записи."""
        return self.entries

    def delete_entry_by_id(self, timestamp):
        """Удаляет запись из списка и сохраняет изменения в JSON-файл."""
        self.entries = list(filter(lambda entry: entry['timestamp'] != timestamp, self.entries))
        self.save_entries_to_file()

    def update_entry(self, timestamp, new_mood, new_comment):
        """Обновляет запись по заданному timestamp."""
        for entry in self.entries:
            if entry["timestamp"] == timestamp:
                entry["mood"] = new_mood
                entry["comment"] = new_comment
                self.save_entries_to_file()  # Используем save_entries_to_file, а не save_entries
                break
