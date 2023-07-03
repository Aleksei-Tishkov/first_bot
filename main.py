import aiogram, requests

with open('API.txt', 'r', encoding='utf-8') as file:
    BOT_TOKEN: str = file.read()

API_URL: str = 'https://api.telegram.org/bot'
API_DOGS_URL: str = 'https://random.dog/woof.json'
ERROR_TEXT: str = 'Тут должна была быть собащка, но пока не пришла...('

TEXT: str = 'Было совершено НОСИЛИЕ'
MAX_COUNTER = 100000
cat_response: requests.Response
cat_link: str

offset: int = -2
counter: int = 0
chat_id: int
timeout: int = 60


while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            dog_response = requests.get(API_DOGS_URL)
            if dog_response.status_code == 200:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={dog_response.json()["url"]}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
    counter += 1