import os
import uuid
from whisper_model import model
from aiogram import types, Bot

def create_unique_file_path(directory: str, original_filename: str) -> str:
    """Создает уникальный путь для сохранения файла с использованием UUID."""
    file_extension = os.path.splitext(original_filename)[-1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    return os.path.join(directory, unique_filename)

async def download_audio_file(bot: Bot, audio: types.Audio, destination: str) -> str:
    """Загружает аудиофайл с сервера Telegram и сохраняет его в указанном пути."""
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    file = await bot.get_file(audio.file_id)
    await bot.download_file(file.file_path, destination)
    return destination

async def transcribe_audio(file_path: str) -> str:
    """Распознает текст из аудиофайла с помощью модели Whisper."""
    result = model.transcribe(file_path)
    return result["text"]
