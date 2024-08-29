import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from config import settings

import utils

bot = Bot(token=settings.bot_token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Отправь мне аудиофайл, и я его распознаю.")

@dp.message(F.audio)
async def handle_audio(message: types.Message):
    audio = message.audio

    if audio.duration > settings.max_audio_duration:
        await message.answer(f"Пожалуйста, отправьте аудиофайл длительностью не более {settings.max_audio_duration // 60} минут.")
        return

    file_path = utils.create_unique_file_path("downloads", audio.file_name)

    await utils.download_audio_file(bot, audio, file_path)

    # Распознавание аудиофайла
    recognized_text = await utils.transcribe_audio(file_path)

    # Отправка распознанного текста
    await message.answer(f"Распознанный текст:\n\n {recognized_text}")

    # Удаление файла после обработки
    os.remove(file_path)