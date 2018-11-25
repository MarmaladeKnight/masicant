from flask import Flask, request
from message import VkApi
from os import getenv


api = VkApi(('7418d0b4d3258f30c143bad273f1e92e707edbf2bd136929734f04a4bcc305bab861de4068142e8fcc442'))


app = Flask(__name__)


@app.route('/vk/', method=['POST'])
def vk():
    message = request.json()

    if message.get('type') == 'confirmation':
        return 'c7fc81d0'

    if message.get('type') == 'message_new':
        api.message(
            message.get('object').get('from_id'), 
            message.get('object').get('text')
        )
