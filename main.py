from aiogram import Bot, Dispatcher, F
from paswords import *
import asyncio
import yadisk
from datetime import datetime

token = codemashine_test
bot = Bot(token=token)
dp = Dispatcher()
# токен яндекс диска
y = yadisk.YaDisk(token=yadisk_token)


@dp.message(F.document, F.chat.type == 'private')
async def chek_message(v):
    await YaDisk(bot, v).save_doc()


@dp.message(F.photo, F.chat.type == 'private')
async def chek_message(v):
    await YaDisk(bot, v).save_photo()


@dp.message(F.video, F.chat.type == 'private')
async def chek_message(v):
    await YaDisk(bot, v).save_video()


class YaDisk:

    def __init__(self, bot, message):
        self.bot = bot
        self.message = message

    async def save_photo(self):
        file_id = self.message.photo[-1].file_id
        file = await self.bot.get_file(file_id)
        file_path = file.file_path
        src = f'/суетологи/{datetime.now().day}.{datetime.now().month}.{datetime.now().year}'
        if y.exists(src) is False:
            y.mkdir(src)
            y.upload(await self.bot.download_file(file_path),
                     f'{src}/{self.message.photo[-1].file_name}')

        else:
            y.upload(await self.bot.download_file(file_path),
                     f'{src}/{self.message.photo[-1].file_name}')

    async def save_doc(self):
        file_id = self.message.document.file_id
        file = await self.bot.get_file(file_id)
        file_path = file.file_path
        src = f'/суетологи/{datetime.now().day}.{datetime.now().month}.{datetime.now().year}'
        if y.exists(src) is False:
            y.mkdir(src)
            y.upload(await self.bot.download_file(file_path),
                     f'{src}/{self.message.document.file_name}')

        else:
            y.upload(await self.bot.download_file(file_path),
                     f'{src}/{self.message.document.file_name}')

    async def save_video(self):
        file_id = self.message.video.file_id
        file = await self.bot.get_file(file_id)
        file_path = file.file_path
        src = f'/суетологи/{datetime.now().day}.{datetime.now().month}.{datetime.now().year}'
        if y.exists(src) is False:
            y.mkdir(src)
            y.upload(await self.bot.download_file(file_path),
                     f'{src}/{self.message.video.file_name}')

        else:
            y.upload(await self.bot.download_file(file_path),
                     f'{src}/{self.message.video.file_name}')


async def main():
    await dp.start_polling(bot)


# Функция main() запускается только в случае если скрипт запущен с этого файла
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')