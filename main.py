import aiogram
from aiogram.filters import BaseFilter, Text
from aiogram.types import Message


with open('API.txt', 'r', encoding='utf-8') as file:
    BOT_TOKEN: str = file.read()

bot: aiogram.Bot = aiogram.Bot(token=BOT_TOKEN)
dp: aiogram.Dispatcher = aiogram.Dispatcher()


class NumsInMsg(BaseFilter):
    async def __call__(self, msg: Message) -> bool | dict[str, list[int]]:
        nums = []
        for word in msg.text.split():
            w = word.replace('.', '').replace(',', '').strip()
            if w.isdigit():
                nums.append(int(w))
        if nums:
            return {'nums': nums}
        return False


@dp.message(Text(startswith='Ищи числа', ignore_case=True), NumsInMsg())
async def process_in_nums(message: Message, nums: list[int]):
    await message.answer(text=f'Нашел вот это: {", ".join(str(i) for i in nums)}')


@dp.message(Text(startswith='Ищи числа', ignore_case=True))
async def process_in_nums(message: Message):
    await message.answer(text='Нет тут ничего')


if __name__ == '__main__':
    dp.run_polling(bot)

