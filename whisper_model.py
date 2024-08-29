import whisper

# Инициализация модели Whisper
model = whisper.load_model("small") # Загрузка модели для небольших аудио файлов
# NOTE: сильно нагружает процессор
