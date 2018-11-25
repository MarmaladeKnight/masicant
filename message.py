#Добавление модулей
from requests import post


class VkApi:
    #Поля( = переменные) класса
    token = ''
    #https://api.vk.com/method/messages.send'
    url='https://api.vk.com/method/{}'

    #Методы( = Функция) класса
    #Метод инициализации
    def __init__(self, token):
        self.token = token
    
    #В этой функции мы добавляем обязательные параметры
    def exec(self, method, params):
        params = ({
            'v':'5.82',
            'access_token': self.token,
            **params
        })

        result = post(self.url.format(method), params)

        return result.json()

    #Отправка сообщения
    def message(self, user_id, text):
        return self.exec('messages.send', {
            'user_id': user_id,
            'message':text
        })

