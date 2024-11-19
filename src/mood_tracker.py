class MoodTracker:
    def __init__(self, file_path="mood_data.json"):
        self.file_path = file_path
        self.entries = self.load_entries_from_file()

def load_entries(self):
    """Загружает записи в таблицу."""
    # Очищаем таблицу перед загрузкой новых записей
    for item in self.tree.get_children():
        self.tree.delete(item)

    # Загружаем записи из mood_tracker и добавляем их в таблицу
    for idx, record in enumerate(self.mood_tracker.entries):  # Индекс записи
        timestamp = record["timestamp"]  # Здесь должно быть время с секундами
        mood = record["mood"]
        comment = record["comment"]
        # Вставляем запись в таблицу с уникальным индексом (idx) для удаления
        self.tree.insert("", "end", values=(timestamp, mood, comment, "…"), tags=(idx,))

    def save_entries_to_file(self):
        """Сохраняет записи в JSON-файл."""
        with open(self.file_path, "w") as file:
            json.dump(self.entries, file, ensure_ascii=False, indent=4)

    def add_entry(self, mood, comment, timestamp=None):
        """Добавляет новую запись в трекер."""
        if not timestamp:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Добавляем секунды
        entry = {
            'mood': mood,
            'comment': comment,
            'timestamp': timestamp  # Секунды будут включены в timestamp
        }
        self.entries.append(entry)
        self.save_entries_to_file()

    def delete_entry_by_id(self, timestamp):
        """Удаляет запись по времени."""
        self.entries = [entry for entry in self.entries if entry["timestamp"] != timestamp]
        self.save_entries_to_file()