from flask import Flask, request
from message import VkApi
from os import getenv


api = VkApi(getenv('VK_TOKEN'))


app = Flask(__name__)


@app.route('/vk/')
def vk():
    message = request.json()

    if message.get('type') == 'message_new':
        api.message(
            message.get('object').get('from_id'), 
            message.get('object').get('text')
        )
